import os
from pathlib import Path

import logging

package_name="diamondpriceprediction"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/components/Data_Injestion.py",
    f"src/{package_name}/components/Data_preprocessing.py",
    f"src/{package_name}/components/Model_traning.py",
    f"src/{package_name}/Pipeline/__init__.py",
    f"src/{package_name}/Pipeline/training_pipeline.py",
    f"src/{package_name}/Pipeline/prediction_pipeline.py",
    f"src/{package_name}/Exceptionhandle.py",
    f"src/{package_name}/Logger.py",
    f"src/{package_name}/Util.py",
    "notebook/Research.ipynb",
    "notebook/data/.gitkeep",
    "init_setup.py",
    "setup.py",
    "__init__.py"
]

for filepath in list_of_files:
    filepath=Path(filepath)

    filedir,filename=os.path.split(filepath)

    if(filedir !=""):
        os.makedirs(filedir,exist_ok=True)

    if (not os.path.exists(filepath)) or(os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
    
    else:
        print("file is already exists!")