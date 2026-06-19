# Multi-Server DevOps Monitoring & CI/CD Platform

## Project Overview

Designed and implemented a complete DevOps lab environment using three Ubuntu Linux virtual machines.

The project demonstrates:

* Continuous Integration and Deployment using Jenkins
* Dockerized application deployment
* GitHub source control integration
* Multi-server monitoring using Prometheus and Grafana
* Infrastructure monitoring with Node Exporter
* Health check validation
* Linux system administration
* Service management using systemd

---

## Infrastructure

### Jenkins Server

IP Address: 192.168.109.51

Services:

* Jenkins
* Node Exporter

Responsibilities:

* Source code integration
* Pipeline execution
* Automated deployment
* Git repository monitoring

---

### Application Server

IP Address: 192.168.109.52

Services:

* Docker Engine
* Docker Compose
* Flask Application Container
* MySQL Container
* Node Exporter

Responsibilities:

* Application hosting
* Database hosting
* Container lifecycle management

---

### Monitoring Server

IP Address: 192.168.109.53

Services:

* Prometheus
* Grafana
* Node Exporter

Responsibilities:

* Metrics collection
* Dashboard visualization
* Alert generation
* Infrastructure monitoring

---

## CI/CD Workflow

Developer
↓
Git Push
↓
GitHub Repository
↓
Jenkins SCM Polling
↓
Jenkins Pipeline
↓
SSH Deployment
↓
Application Server
↓
git pull
↓
docker compose up -d --build
↓
Health Check Validation

---

## Jenkins Pipeline

Deployment Stage:

* SSH connection from Jenkins Server to Application Server
* Pull latest source code from GitHub
* Rebuild Docker images
* Restart containers using Docker Compose

Health Check Stage:

* Verify Flask application accessibility
* Validate deployment success

---

## Monitoring Stack

Monitoring Components:

* Prometheus
* Grafana
* Node Exporter

Monitored Servers:

* Jenkins Server
* Application Server
* Monitoring Server

Configured Dashboards:

* CPU Usage
* Memory Usage
* Disk Usage
* Server Status

---

## Alerting

Configured in Grafana:

* Server Status Monitoring
* Infrastructure Health Monitoring

---

## Container Configuration

Application Container:

* Flask Application

Database Container:

* MySQL

Restart Policy:

* unless-stopped

---

## Linux Administration Tasks Performed

* Static IP configuration using Netplan
* SSH configuration
* Service management using systemctl
* Process management
* Network troubleshooting
* Route troubleshooting
* Container troubleshooting
* Monitoring stack troubleshooting

---

## Technologies Used

### Operating System

* Ubuntu Linux

### DevOps

* Jenkins
* Git
* GitHub

### Containers

* Docker
* Docker Compose

### Monitoring

* Prometheus
* Grafana
* Node Exporter

### Application

* Flask
* MySQL

### Linux

* SSH
* systemd
* Netplan

---

## Key Achievements

* Built and managed a 3-server DevOps environment
* Implemented automated deployment pipeline
* Deployed containerized web application
* Implemented centralized monitoring
* Configured infrastructure dashboards
* Configured automated container recovery
* Implemented deployment health checks

---
