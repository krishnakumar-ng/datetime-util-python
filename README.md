# python-util

## Requirements
```commandline
python version 3.11
```

To resolve all the external libraries, run the virtual_environment_setup.sh file before starting the execution. It's a one time activity which must be done when the repo is cloned for the first time.

<details>

<summary>Virtual Environment Setup - Explanation</summary>

## Create virtual environment
``` sh
python3 -m venv <envirnonment_name>
```

This will create a virtual environment for you with the following files in the virtual environment directory <environment_name>:

bin
include
lib
pip-selfcheck.json
pyvenv.cfg

## Activate the virtual environment
``` sh
source <envirnonment_name>/bin/activate
```

This will start the virtual environment and you should see the name of the virtual environment added before the directory name as shown in the image below:

Now you can install anything in it, by running the pip3 install command
for example to install the requests module, run the following command:

``` sh
pip3 install requests
```

## To get out of the virtual environment

``` sh
exit
```
</details>