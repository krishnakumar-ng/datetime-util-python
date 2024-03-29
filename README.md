# python-util

## Requirements
```commandline
python version 3.11
```

Below is the command to run the program
```
python3 DateTime.py
```

## Create and Manage Python Virtual Environments

<details>
<summary>Click to see the complete documentation for python virtual environment setup</summary>


The create_virtual_environment.sh script helps you create and manage Python virtual environment for your project. It allows you to isolate project dependencies and avoid conflicts with system-wide Python installations.

## Prerequisites:

* Python 3 installed on your system.
* Script saved with a .sh extension (e.g: create_virtual_environment.sh).
* Script has executable permissions (use chmod +x create_virtual_environment.sh to set them).

Steps:

Open a terminal and Navigate to the directory where you saved the script using the cd command (e.g., cd my_project_dir).

## Run the script:

Bash
```
./create_virtual_environment.sh
```

## Output:

The script will:

Create a virtual environment in a sibling directory (one level up) with the provided name.
(Optional) Install dependencies listed in a requirements.txt file located in the same directory as the script (if the file exists).
Display information about the virtual environment location and installed dependencies.

## Additional Notes:

The script assumes python points to your Python 3 interpreter. If you have multiple versions or a different setup, modify the python -m venv command in the script to use the correct interpreter path.

</details>