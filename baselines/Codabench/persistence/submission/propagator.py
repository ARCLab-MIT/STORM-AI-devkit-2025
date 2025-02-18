# Initialize orekit and JVM
import orekit
from orekit.pyhelpers import setup_orekit_curdir

from org.orekit.orbits import KeplerianOrbit, PositionAngleType
from org.orekit.frames import FramesFactory
from org.orekit.time import TimeScalesFactory, AbsoluteDate
from org.orekit.utils import Constants
from org.orekit.propagation.numerical import NumericalPropagator
from org.hipparchus.ode.nonstiff import DormandPrince853Integrator
from org.orekit.propagation import SpacecraftState
from org.orekit.bodies import OneAxisEllipsoid, CelestialBodyFactory, CelestialBody
from org.orekit.forces.gravity.potential import GravityFieldFactory
from org.orekit.forces.gravity import HolmesFeatherstoneAttractionModel, ThirdBodyAttraction, SolidTides
from java.util import ArrayList
from org.orekit.forces.radiation import SolarRadiationPressure, IsotropicRadiationSingleCoefficient
from org.orekit.models.earth.atmosphere.data import JB2008SpaceEnvironmentData
from org.orekit.forces.drag import IsotropicDrag, DragForce
from org.orekit.models.earth.atmosphere import JB2008
from org.orekit.utils import IERSConventions
from orekit import JArray_double, JArray

from org.hipparchus.geometry.euclidean.threed import Vector3D
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
from tqdm import tqdm

vm = orekit.initVM()
setup_orekit_curdir()

plt.rcParams.update({'font.size': 12})
  
# =============================================================================
# Constants/Basics
# =============================================================================
r_Earth = Constants.IERS2010_EARTH_EQUATORIAL_RADIUS #m
itrf    = FramesFactory.getITRF(IERSConventions.IERS_2010, True) # International Terrestrial Reference Frame, earth fixed
inertialFrame = FramesFactory.getEME2000()
earth = OneAxisEllipsoid(r_Earth,
                         Constants.IERS2010_EARTH_FLATTENING,
                         itrf)
mu = Constants.IERS2010_EARTH_MU #m^3/s^2
degree = 70
torder = 70
cr = 1.0
utc = TimeScalesFactory.getUTC()
sun = CelestialBodyFactory.getSun()
moon = CelestialBodyFactory.getMoon()
deg = np.pi / 180 # Degrees-Radians conversion


# =============================================================================
# Propagator
# =============================================================================
def prop_orbit(initial_state, CustomAtmosphere, plot_trajectory=True, **kwargs):
    """
    Propagates the orbit of a satellite over a given duration using a high-fidelity numerical propagator.

    Parameters:
        initial_orbit (Orbit): The initial orbit of the satellite.
        CustomAtmosphere (class): A custom atmosphere model class to be used for drag force calculations.

    Keyword Arguments:
        satellite_mass (float): Mass of the satellite in kg (default: 260.0).
        cross_section (float): Cross-sectional area in m^2 (default: 5.12).
        srp_area (float): Area for solar radiation pressure in m^2 (default: 30.0).
        drag_coeff (float): Drag coefficient (default: 2.2).
        atm_model_data (object): Data for the atmospheric model (default: JB2008SpaceEnvironmentData).
        step (float): Time step for propagation in seconds (default: 600.0).
        horizon (float): Propagation horizon in seconds (default: 3 * 86400.0).

    Returns:
        tuple: A tuple containing:
            - states (list of SpacecraftState): The spacecraft states during propagation.
            - densities (list of float): Atmospheric densities at each spacecraft state.
    """

    # Integrator settings
    minStep = 1e-6
    maxstep = 100.0
    initStep = 1.0
    positionTolerance = 1e-4

    # Satellite variables
    satellite_mass = kwargs.get('satellite_mass', 260.0) 
    crossSection = kwargs.get('cross_section', 3.2 * 1.6) # In m^2
    srpArea = kwargs.get('srp_area', 30.0) # In m^2
    dragCoeff = kwargs.get('drag_coeff', 2.2)

    # Atmospheric model instantiation
    data = kwargs.get('atm_model_data', JB2008SpaceEnvironmentData("SOLFSMY.TXT", "DTCFILE.TXT"))  
    atmosphere = CustomAtmosphere(data)
    
    # Start date calculation
    tmstp = initial_state.get('Timestamp', pd.Timestamp('2013-11-30 00:00:00.00000'))
    initialDate = AbsoluteDate(
        tmstp.year,
        tmstp.month,
        tmstp.day,
        0,
        0,
        00.000,
        utc
    )
        
    
    # Propagation time steps calculation
    step = kwargs.get('step', 600.0) # Step of 10 minutes in seconds 
    horizon = kwargs.get('horizon', 3 * 86400.0) # Propagation horizon of 3 days in seconds
    tspan1 = [initialDate.shiftedBy(step*n) for n in range(int(horizon / step))]

    # Initial Orbit preparation
    rp0 = r_Earth + 400 * 1e3 # perigee radius (m)
    rap0 = r_Earth + 600 * 1e3 # apogee radius (m)

    a0 = initial_state.get('Semi-major Axis (km)', None)
    semi_major_axis = a0 * 1e3 if a0 is not None else (rp0 + rap0) / 2
    
    initial_orbit = KeplerianOrbit(
        semi_major_axis,
        initial_state.get('Eccentricity', (rap0 - rp0) / (rap0 + rp0)),
        initial_state.get('Inclination (deg)', 45) * deg,
        initial_state.get('Argument of Perigee (deg)', 30) * deg,
        initial_state.get('RAAN (deg)', 0) * deg,
        initial_state.get('True Anomaly (deg)', 0) * deg, 
        PositionAngleType.TRUE, 
        inertialFrame, 
        initialDate,
        mu
    )
    
    
    satmodel = IsotropicDrag(crossSection, dragCoeff) # Cross sectional area and the drag coefficient

    orbitType = initial_orbit.getType()
    initialState = SpacecraftState(initial_orbit, satellite_mass)
    tol = NumericalPropagator.tolerances(positionTolerance, initial_orbit, orbitType)

    integrator = DormandPrince853Integrator(minStep, maxstep, JArray_double.cast_(tol[0]), JArray_double.cast_(tol[1]))
    integrator.setInitialStepSize(initStep)

    propagator_num = NumericalPropagator(integrator)
    propagator_num.setOrbitType(orbitType)
    propagator_num.setInitialState(initialState)

    # Add Solar Radiation Pressure
    spacecraft = IsotropicRadiationSingleCoefficient(srpArea, cr)
    srpProvider = SolarRadiationPressure(sun, earth, spacecraft)
    propagator_num.addForceModel(srpProvider)

    # Add Gravity Force
    gravityProvider = GravityFieldFactory.getConstantNormalizedProvider(degree, torder, initialDate)
    gravityForce = HolmesFeatherstoneAttractionModel(earth.getBodyFrame(), gravityProvider)
    propagator_num.addForceModel(gravityForce)

    # Add Solid Tides
    solidTidesBodies = ArrayList().of_(CelestialBody)
    solidTidesBodies.add(sun)
    solidTidesBodies.add(moon)
    solidTidesBodies = solidTidesBodies.toArray()
    solidTides = SolidTides(earth.getBodyFrame(), 
                            gravityProvider.getAe(), gravityProvider.getMu(),
                            gravityProvider.getTideSystem(), 
                            IERSConventions.IERS_2010,
                            TimeScalesFactory.getUT1(IERSConventions.IERS_2010, True), 
                            solidTidesBodies)
    propagator_num.addForceModel(solidTides)

    # Add Third Body Attractions
    propagator_num.addForceModel(ThirdBodyAttraction(sun))
    propagator_num.addForceModel(ThirdBodyAttraction(moon)) 

    # Add Custom Drag Force
    dragForce = DragForce(atmosphere, satmodel)
    propagator_num.addForceModel(dragForce)

    # Results generation
    tic = time.time()
    steps = tqdm(range(len(tspan1) - 1))
    steps.set_description("Starting propagation...")
    
    states = [initialState]    
    for i1 in steps:
        try:
            propagator_it = propagator_num.propagate(tspan1[i1], tspan1[i1 + 1])
            states.append(propagator_it)
        except Exception as e:
            if states[-1] is not None:
                print(f"Eccentricity error: {initial_state.get('Eccentricity', (rap0 - rp0) / (rap0 + rp0))}. Error: {e}") 
            # Append a placeholder state with None or handle accordingly
            states.append(None)  # Add None to maintain alignment with densities
            continue
    
    densities = [
        9.99e+32 if state is None else atmosphere.getDensity(
            state.getDate(), state.getPVCoordinates().getPosition() / 1e3, state.getFrame()
        ) for state in states
    ]

    
    toc = time.time()

    if(plot_trajectory):
        posvel = [state.getPVCoordinates() for state in states]
        poss = [state.getPosition() for state in posvel]
        vels = [state.getVelocity() for state in posvel]
        px = [pos.getX() * 1e-3 for pos in poss]
        py = [pos.getY() * 1e-3 for pos in poss]
        pz = [pos.getZ() * 1e-3 for pos in poss]
        vx = [vel.getX() * 1e-3 for vel in vels]
        vy = [vel.getY() * 1e-3 for vel in vels]
        vz = [vel.getZ() * 1e-3 for vel in vels]
        stat_list = [horizon, toc - tic, px[-1], py[-1], pz[-1], vx[-1], vy[-1], vz[-1], step]
        print("Time interval [s]:", stat_list[0])
        print("Time step [s]:", stat_list[8])
        print("CPU time [s]:", stat_list[1])
        print("Final Pos [km]:", np.linalg.norm([px[-1], py[-1], pz[-1]]))
        print("Final Vel [km]:", np.linalg.norm([vx[-1], vy[-1], vz[-1]]))
    
        # Plot the satellite trajectory
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(px, py, pz, label='Trajectory')
        
        # plot earth
        phi = np.linspace(-np.pi, np.pi, 100)
        theta = np.linspace(-np.pi/2, np.pi/2, 50)
        X_Earth = r_Earth*1e-3 * np.outer(np.cos(phi), np.cos(theta)).T
        Y_Earth = r_Earth*1e-3 * np.outer(np.sin(phi), np.cos(theta)).T
        Z_Earth = r_Earth*1e-3 * np.outer(np.ones(np.size(phi)), np.sin(theta)).T
        ax.plot_surface(X_Earth, Y_Earth, Z_Earth, cmap='binary', alpha=0.35, antialiased=False, zorder = 1)
        
        ax.set_xlabel('X [km]')
        ax.set_ylabel('Y [km]')
        ax.set_zlabel('Z [km]')
        ax.set_aspect('equal', adjustable='box')
        ax.set_title('Satellite Trajectory')
        ax.legend()
        plt.show()

    return states, densities
