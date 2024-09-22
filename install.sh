#!/bin/bash

TRANSFER_PATH="/usr/local/bin/transfer"
SCRIPT_PATH=$(readlink -f transfer.py)

# Function to check if the transfer command is already installed
check_setup() {
    if [ -f "$TRANSFER_PATH" ]; then
        echo "'transfer' command is already set up."
        exit 0
    fi
}

# Function to install the transfer command globally
setup_transfer() {
    echo "Setting up global 'transfer' command..."
    
    # Copy the transfer.py script to /usr/local/bin/transfer
    sudo cp "$SCRIPT_PATH" "$TRANSFER_PATH"
    
    # Make it executable
    sudo chmod +x "$TRANSFER_PATH"
    
    if [ $? -eq 0 ]; then
        echo "'transfer' command has been set up successfully at $TRANSFER_PATH."
    else
        echo "Error: Failed to set up 'transfer' command."
        exit 1
    fi
}

# Check if already installed
check_setup

# If not set up, perform the setup
setup_transfer
