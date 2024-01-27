#!/bin/bash

# Configuration Parameters
XAMPP_CONF_FILE="/path/to/xampp/apache/conf/httpd.conf"
FIREWALL_RULE_NAME="Allow_HTTP"
ROUTER_IP="192.168.1.1"
ROUTER_USERNAME="your_router_username"
ROUTER_PASSWORD="your_router_password"

# Function to update XAMPP configuration
update_xampp_config() {
    # Enable external access in XAMPP configuration
    sed -i 's/Listen 80/Listen 0.0.0.0:80/' "$XAMPP_CONF_FILE"
}

# Function to update Windows Firewall rules
update_firewall_rules() {
    # Check if the rule already exists
    existing_rule=$(netsh advfirewall firewall show rule name="$FIREWALL_RULE_NAME" | grep "Rule Name")
    if [ -z "$existing_rule" ]; then
        # Create a new rule to allow incoming traffic on port 80
        netsh advfirewall firewall add rule name="$FIREWALL_RULE_NAME" dir=in action=allow protocol=TCP localport=80
    else
        echo "Firewall rule '$FIREWALL_RULE_NAME' already exists."
    fi
}

# Function to configure port forwarding on the router
configure_port_forwarding() {
    # Use a tool or library to interact with the router's API for port forwarding
    # Alternatively, consider using a router with UPnP support for automatic port forwarding
    # This example assumes a hypothetical tool named 'router-tool' is used
    router-tool configure-port-forwarding --router-ip "$ROUTER_IP" --username "$ROUTER_USERNAME" --password "$ROUTER_PASSWORD" --external-port 80 --internal-ip <your_internal_ip> --internal-port 80
}

# Main Script
echo "Updating XAMPP configuration..."
update_xampp_config

echo "Updating Windows Firewall rules..."
update_firewall_rules

echo "Configuring port forwarding on the router..."
configure_port_forwarding

echo "Script execution completed."
