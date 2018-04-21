import os
import sys

PYTHON_PATH_ENVIRONMENT_VARIABLE = "PYTHONPATH"

def python_paths():
    """Returns the environment variable PYTHONPATH as a list
    """
    
    python_path = os.environ[PYTHON_PATH_ENVIRONMENT_VARIABLE]
    if python_path:
        python_paths = python_path.split(os.path.pathsep)
    else:
        python_paths = []

    return python_paths

def python_version_string():
    
    return str(sys.version_info.major) + "." + \
            str(sys.version_info.minor) + "." + \
            str(sys.version_info.micro)

def python_version_full_strings():
    
    return sys.version.split("\n")
