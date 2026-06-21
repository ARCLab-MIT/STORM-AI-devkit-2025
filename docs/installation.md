# Installation

To participate in this challenge, you will need to run your images within an **Anaconda environment**. As part of your submission, you must export the environment configuration and upload it. 

However, please note:
- The submission environment will be created using **Micromamba** (due to performance reasons). 
- If you choose to install only one of the tools, it should still work fine for exporting the necessary dependencies, as they share almost all commands.

**Why Anaconda and Micromamba?**
- **Anaconda** is the most comprehensive and robust tool for creating and managing environments.
- **Micromamba** is, for the most part, fully compatible with Anaconda `env` files, ensuring smooth transitions.

<div style="display: flex; flex-direction: column; background-color: #e7f3fe; border-left: 6px solid #646464; border-radius: 4px; padding: 15px; margin: 20px 0; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); font-family: Arial, sans-serif; color: #333;">
    <div style="font-size: 18px; font-weight: bold; color: #ffffff; background-color: #646464; display: inline-block; padding: 5px 10px; border-radius: 3px; margin-bottom: 10px;">💡 Recommendation</div>
    <ol style="font-size: 14px; margin: 0; padding-left: 20px; line-height: 1.5;">
        <li>Start by working with <strong>Anaconda</strong>.</li>
        <li>Test that <strong>Micromamba</strong> can import your environment locally before uploading it to the challenge.</li>
    </ol>
    <p style="font-size: 14px; margin: 0; line-height: 1.5;">
        This will ensure that your submission runs smoothly without issues.
    </p>
</div>

Additionally, you can recreate the container where your submission will be executed using Docker. The prebuilt container is available on **Docker Hub** and can be pulled with the following command:

```bash
docker pull arclab/AI-Challenge/mamba-submission:latest 
```

This container includes NVIDIA drivers, **Micromamba**, and essential scientific libraries such as `numpy` and `pandas`. 

## Install Anaconda 🐍

Follow the Anaconda installation guide [here](https://docs.anaconda.com/free/anaconda/install/index.html). The devkit is tested for **Python 3.9+** on **Ubuntu** and **macOS**.

<div style="display: flex; flex-direction: column; background-color: #e7f3fe; border-left: 6px solid #2196f3; border-radius: 4px; padding: 15px; margin: 20px 0; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); font-family: Arial, sans-serif; color: #333;">
    <div style="font-size: 18px; font-weight: bold; color: #ffffff; background-color: #1265c0; display: inline-block; padding: 5px 10px; border-radius: 3px; margin-bottom: 10px;"> ℹ️ Info</div>
    <p style="font-size: 14px; margin: 0; line-height: 1.5;">
        Anaconda includes a built-in Python installation. The container runs <strong>Python 3.9.21</strong>, so make sure you are not using an older version.
    </p>
</div>

## Install Micromamba 𓆙

Refer to the Micromamba installation guide [here](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html). 

## Install Docker 🐋

If you want to test your submission in the same environment it will be executed in, you need to install **Docker**.

### 1. Docker Prerequisites

- **Windows**: WSL2
    1. Open PowerShell as Administrator and run:  
       ```powershell
       wsl --install
       ```
    2. Restart your computer when prompted.
    3. Install a Linux distro from Microsoft Store (e.g., **Ubuntu**).
    4. Set WSL 2 as the default:  
       ```powershell
       wsl --set-default-version 2
       ```
    5. Verify WSL installation:  
       ```powershell
       wsl --list --verbose
       ```

- **macOS**: Install **Homebrew**  
- **Linux**: Update and upgrade system packages:  
    ```bash
    sudo apt update && sudo apt upgrade
    ```

### 2. Download Docker Installer

- **Windows**: Download **Docker Desktop** from the official site.
- **macOS**: Install using Homebrew:  
    ```bash
    brew install --cask docker
    ```
- **Linux**: Install Docker with:  
    ```bash
    sudo apt install docker.io
    ```

### 3. Run the Installer

- **Windows**: Double-click the `.exe` file and follow the instructions.
- **macOS**: Follow the Homebrew prompts.
- **Linux**: Start Docker service and enable it on boot:  
    ```bash
    sudo systemctl start docker && sudo systemctl enable docker
    ```

### 4. Verify Installation

Run the following commands to ensure Docker is installed correctly:

```bash
docker --version
docker run hello-world
```

### [Optional] Install NVIDIA Container Toolkit

If your submission requires GPU acceleration and you want to test it locally, install the [NVIDIA container toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html).

## Download the Devkit

Download the devkit using the terminal and move into the newly created folder:

```bash
cd && git clone https://github.com/ARCLab-MIT/STORM-AI-devkit-2025.git && cd STORM-AI-devkit-2025
```

This command will clone the repository into your home directory. While you can place it in another directory, the rest of our tutorials assume you are working from your home directory.


<!--
## Download the dataset

The challenge dataset can be downloaded from [here](). Please store the downloaded dataset into the `~/strorm-ai-devkit/dataset` folder. All the information about it can be found on the [STORM-AI dataset page](https://2025-ai-challenge.readthedocs.io/en/latest/dataset.html).

-->
