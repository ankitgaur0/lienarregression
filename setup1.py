from setuptools import setup,find_packages
import os
from typing import List


HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="diamondpriceprediction",
    versions='0.0.0.1',
    author="Ankit_gaur",
    author_email="ankitparashar000@gmail.com",
    #install_requires=["pandas","numpy","scikit-learn","matplotlib","seaborn"],
    install_requires= get_requirements("requirements.txt"),
    packages=find_packages()

)