#!/bin/bash

TRANSFER_PATH="/usr/local/bin/transfer"

# Function to check if the transfer command exists and remove it
uninstall_transfer() {
    if [ -f "$TRANSFER_PATH" ]; then
        echo "Removing 'transfer' command from $TRANSFER_PATH..."
        sudo rm "$TRANSFER_PATH"
        
        if [ $? -eq 0 ]; then
            echo "'transfer' command successfully removed."
        else
            echo "Error: Failed to remove 'transfer' command."
            exit 1
        fi
    else
        echo "'transfer' command is not installed."
        exit 0
    fi
}

# Run the uninstall process
uninstall_transfer
