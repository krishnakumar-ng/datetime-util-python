#!/bin/bash

# Define virtual environment name (optional, uncomment to set a default)
venv_name="datetime_env"  

# Get the project directory (script location)
project_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Create the virtual environment directory (sibling to project)
venv_dir="$project_dir/../$venv_name"  # Create directory one level up with the same name as the virtual environment

# Function to create virtual environment
create_venv() {
  python3 -m venv "$venv_dir"
}

# Function to install dependencies (assuming requirements.txt is in project dir)
install_dependencies() {
  if [ -f "$project_dir/requirements.txt" ]; then
    pip3 install -r "$project_dir/requirements.txt" -t "$venv_dir/lib/python3.11/site-packages"  # Replace 'python3.x' with your Python version
  else
    echo "Warning: No requirements.txt file found. Skipping dependency installation."
  fi
}

# Check if virtual environment directory exists
if [ -d "$venv_dir" ]; then
  echo "Virtual environment '$venv_name' already exists. Skipping creation."
else
  # Create virtual environment
  create_venv

  # Check for virtual environment creation errors
  if [[ $? -ne 0 ]]; then
    echo "Error: Failed to create virtual environment '$venv_name'."
    exit 1
  fi

  echo "Virtual environment '$venv_name' created successfully in a sibling directory."
fi

# Install dependencies (assuming requirements.txt is present)
install_dependencies

# Activate the virtual environment (for potential one-time tasks within the script)
source "$venv_dir/bin/activate"  # Modify for Windows if needed

# Perform actions within the activated virtual environment (if needed)
# For example, you could run a script or test something here


#To check whether all the requirements are installed: 
pip3 list

# Deactivate the virtual environment
deactivate

echo "**Important:**"
echo " - The virtual environment is located in '$venv_dir'."
echo " - Dependencies (if any) are installed within the virtual environment."
