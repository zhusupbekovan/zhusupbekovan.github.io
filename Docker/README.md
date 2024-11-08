# Docker installationS

## Assignment Instructions
The assignment for this module is to set up an application using Docker and Docker Compose and document the process and any files used or created along the way (such as a docker-compose.yml or Dockerfile - if applicable). In other words, a fellow student of this course should be able to loosely follow your instructions to install the application themselves. After completing this assignment, post your documentation to you GitHub Pages website. Do not delete your Arch Assignment documentation. You may create an additional page or an index page to link to your projects if desired.

This assignment is not prescriptive in terms of which application is set up, although I encourage students to choose an application that is relevant to their interests is appropriate for their comfort level. Many open-source options exist on GitHub (and often include docker-compose.yml files).

If a student has an application they would like to Dockerize (like a web app from a personal project), then this could be used as an opportunity (or an excuse) to do so.

Below are a few ideas to look into, although students are not limited to this list:

- WordPress (very easy)
- PiHole
- Greenbone (formerly OpenVAS)
- This Example Voting App
- Gotify
- Uptime Kuma
- Bookstack
- Nextcloud
- Seafile
- Gitea
- GitLab
- SnipeIT

More inspiration can be gleaned from Awesome-FOSS/Awesome-Sysadmin and Awesome-Compose as well as many other online resources (link1), although be wary not to dive too deep for the sake of this assignment.



Note: do not run the result of this assignment in a production environment without properly securing your services (proper HTTPS, access control, etc.).
## Table of Contents
- [Assignment Instructions](#assignment-instructions)
- [Table of Contents](#table-of-contents)
- [System Prerequisites](#system-prerequisites)
- [Deployment description](#deployment-description)
    - [Functional requirenments](#functional-requirenments)
    - [Additional features](#additional-features)
- [Installing docker and docker-compose](#installing-docker-and-docker-compose)
- [Setup](#setup)
    - [Folder structure](#folder-structure)
    - [Setup Docker-Compore File](#setup-docker-compore-file)
    - [Setup python](#setup-python)
    - [Setup Nginx](#setup-nginx)
    - [Additional Configurations](#additional-configurations)
- [Running deployment](#running-deployment)
    - [Scenario 1](#scenario-1)
- [Troubleshooting](#troubleshooting)
- [References](#references)

## System Prerequisites
This project is deployed in Ubuntu 22.04 using WSL in Windows (see [How to install Linux on Windows using WSL](https://learn.microsoft.com/en-us/windows/wsl/install)). Make sure everything is installed before you start building the project. 

## Deployment description
### Functional requirenments
### Additional features

## Installing docker and docker-compose
Install docker and docker-compose. Use the following commands:
```bash 
sudo apt-get update && sudo apt-get install -y docker.io docker-compose
```
Make sure docker is installed:
```bash 
sudo docker --version
```
Something like this
```bash 
Docker version 24.0.7
```
should be printed.

## Setup
This section explains step by step for what is each file/folder.
### Folder structure
The following is the folder structure of the deployment:
```bash
.
├── docker-compose.yml
├── grafana.ini
├── nginx
│   ├── Dockerfile
│   └── index.html
└── python
    ├── Dockerfile
    └── sensor_data_generator.py
```   
Later, make sure you are running docker-compose in this derectory.

### Setup Docker-Compore File
### Setup python
### Setup Nginx
### Additional Configurations
## Running deployment
### Scenario 1
## Troubleshooting
## References
