# Automated Web Server Configuration Script

## Overview

This Bash script automates the setup of a local web server using XAMPP, updates Windows Firewall rules, and configures port forwarding on a router.

## Configuration Parameters

Before running the script, ensure to configure the following parameters in the script:

- `XAMPP_CONF_FILE`: Path to XAMPP Apache configuration file.
- `FIREWALL_RULE_NAME`: Desired name for the Windows Firewall rule.
- `ROUTER_IP`: IP address of the router.
- `ROUTER_USERNAME`: Username for router login.
- `ROUTER_PASSWORD`: Password for router login.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/MrBug123/automated-web-server-configuration.git
   cd automated-web-server-configuration
