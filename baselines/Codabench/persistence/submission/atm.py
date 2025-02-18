import pandas as pd
import numpy as np
import math
from pymsis import msis

# Orekit imports
import orekit
from org.orekit.time import AbsoluteDate
from org.orekit.utils import PVCoordinates, Constants
from org.orekit.frames import Frame
from org.orekit.models.earth.atmosphere import PythonAtmosphere
from org.hipparchus.geometry.euclidean.threed import Vector3D
from org.orekit.frames import FramesFactory, Frame
from org.orekit.bodies import OneAxisEllipsoid
from org.orekit.utils import IERSConventions

class PersistenceMSIS():
    def __init__(self, omni2_data):
        """
        Initialize the Persistence Model.

        Args:
          - omni2_data (pd.DataFrame): OMNI2 data containing Ap, F10.7, and other parameters.

        """
        self.initial_date = None
        self.omni2_data = omni2_data

    def run(self, dt, lon, lat, alt):
        """
        Runs the MSIS model for the initial date using OMNI2 data to avoid online calls.

        Parameters:
            datetime_input (datetime): Datetime for the simulation.
            lon (float): Longitude in degrees.
            lat (float): Latitude in degrees.
            alt (float): Altitude in km.

        Returns:
            np.ndarray: Output from the MSIS model.
        """
        # We want to replicate the initial state through the output so we only
        # keep the initial date
        if self.initial_date is None:
            self.initial_date = dt

        # Find the closest row in OMNI2 data
        row = self.omni2_data.loc[self.omni2_data['Timestamp'] == self.initial_date]
        
        f107_daily = row['f10.7_index'].values[0]
        ap_current = row['ap_index_nT'].values[0]

        # Prepare Ap indices using the helper function
        aps = self._prepare_ap_indices(self.initial_date, ap_current)

        # Run the MSIS model
        result = msis.run(
            dates=[self.initial_date],
            lons=[lon],
            lats=[lat],
            alts=[alt],
            f107s=[f107_daily],
            aps=[aps]
        )

        return result[0,0]  # Return the density for the specific point

    def _prepare_ap_indices(self, datetime_input, ap_current):
        """
        Private helper function to compute Ap indices and averages required for MSIS.

        Parameters:
            datetime_input (datetime): Datetime for the simulation.
            ap_current (float): Current daily Ap value.

        Returns:
            list: Prepared Ap array for MSIS input.
        """
        index = self.omni2_data.index[self.omni2_data['Timestamp'] == datetime_input][0]

        # Compute 3-hourly Ap indices
        ap_3hr_indices = [
            self.omni2_data.iloc[index - i]['ap_index_nT'] if (index - i) >= 0 else ap_current
            for i in range(0, 4)
        ]

        # Compute averages for specific periods
        ap_12_33_avg = np.mean([
            self.omni2_data.iloc[index - i]['ap_index_nT'] if (index - i) >= 0 else ap_current
            for i in range(12, 34, 3)
        ])
        ap_36_57_avg = np.mean([
            self.omni2_data.iloc[index - i]['ap_index_nT'] if (index - i) >= 0 else ap_current
            for i in range(36, 58, 3)
        ])

        # Prepare Ap array
        aps = [
            ap_current,  # Daily Ap
            ap_3hr_indices[0],  # Current 3-hour Ap
            ap_3hr_indices[1],  # 3 hours before
            ap_3hr_indices[2],  # 6 hours before
            ap_3hr_indices[3],  # 9 hours before
            ap_12_33_avg,       # Average of 12-33 hours prior
            ap_36_57_avg        # Average of 36-57 hours prior
        ]

        return aps


class MSISPersistenceAtmosphere(PythonAtmosphere):
    """
    CustomAtmosphere is a custom implementation of the PythonAtmosphere class
    that uses the PersistenceModel to compute atmospheric density and velocity.

    Attributes:
        atm (PersistenceModel): An instance of the PersistenceModel.
        earth (Body): The central body (Earth) for the atmospheric model.

    Methods:
        getMSISPersistence(input_df: pd.DataFrame) -> pd.DataFrame:
            Generates persistent MSIS data using the PersistenceModel.

        getDensity(date: AbsoluteDate, position: Vector3D, frame: Frame) -> float:
            Computes the atmospheric density at a given date, position, and frame
            using the PersistenceModel output.

        _position_to_geo(position: Vector3D) -> Tuple[float, float, float]:
            Helper method to convert position to latitude, longitude, and altitude.
    """
    def __init__(self, omni2, **kwargs):
        super().__init__()
        self.atm = PersistenceMSIS(omni2)
        r_Earth = Constants.IERS2010_EARTH_EQUATORIAL_RADIUS #m
        self.itrf = FramesFactory.getITRF(IERSConventions.IERS_2010, True) # International Terrestrial Reference Frame, earth fixed
        self.earth = OneAxisEllipsoid(
                         r_Earth,
                         Constants.IERS2010_EARTH_FLATTENING,
                         self.itrf
                    )

    def getDensity(self, date: AbsoluteDate, position: Vector3D, frame: Frame) -> float:
        """
        Compute the atmospheric density at a given date, position, and frame using the PersistenceModel output.

        Args:
            date (AbsoluteDate): The date for which to compute density.
            position (Vector3D): The position in the given frame.
            frame (Frame): The reference frame.

        Returns:
            float: The computed atmospheric density.
        """
        # Convert position to latitude, longitude, and altitude
        # bodyToFrame = self.earth.getBodyFrame().getKinematicTransformTo(frame, date)
        # posInBody = bodyToFrame.getStaticInverse().transformPosition(position)
        lat, lon, alt = self._position_to_geo(position, date)

        # Convert date
        time_str = date.toString(0)
        dt = pd.to_datetime(time_str).tz_localize(None)

        # Get persistence model output
        density = self.atm.run(dt, lon, lat, alt)


        return float(density)


    def getVelocity(self, date: AbsoluteDate, position: Vector3D, frame: Frame):
        '''
        Get the inertial velocity of atmosphere molecules.
        By default, atmosphere is supposed to have a null
        velocity in the central body frame.</p>
        '''
        # get the transform from body frame to the inertial frame
        bodyToFrame = self.earth.getBodyFrame().getKinematicTransformTo(frame, date)
        # Inverse transform the position to the body frame
        posInBody = bodyToFrame.getStaticInverse().transformPosition(position)
        # Create PVCoordinates object assuming zero velocity in body frame
        pv_body = PVCoordinates(posInBody, Vector3D.ZERO)
        # Transform the position/velocity (PV) coordinates to the given frame
        pvFrame = bodyToFrame.transformOnlyPV(pv_body)
        # Return the velocity in the current frame
        return pvFrame.getVelocity()

    def _position_to_geo(self, positionICRF, date):
            """
            Converts a position vector (in ICRF frame) to geodetic coordinates (lat, lon, alt).
    
            Parameters:
            positionICRF: Vector3D, position vector in ICRF frame.
            date: AbsoluteDate, the date of the position.
    
            Returns:
            tuple: (latitude, longitude, altitude) in degrees and kilometers.
            """
            # Create a PVCoordinates object (assuming zero velocity)
            pvICRF = PVCoordinates(positionICRF, Vector3D.ZERO)
    
            # Transform position from ICRF to ECEF (ITRF)
            transform = self.earth.getBodyFrame().getTransformTo(self.itrf, date)
            pvECEF = transform.transformPVCoordinates(pvICRF)
            positionECEF = pvECEF.getPosition()
    
            # Convert the ECEF position to geodetic coordinates
            geodeticPoint = self.earth.transform(positionECEF, self.itrf, date)
    
            # Extract latitude, longitude, and altitude
            latitude = geodeticPoint.getLatitude()  # radians
            longitude = geodeticPoint.getLongitude() # radians
            altitude = geodeticPoint.getAltitude() / 1e3  # kilometers
    
            # Convert radians to degrees for latitude and longitude
            latitudeDeg = math.degrees(latitude)
            longitudeDeg = math.degrees(longitude)
    
            return latitudeDeg, longitudeDeg, altitude
