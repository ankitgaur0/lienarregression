from setuptools import setup,find_packages
import os

setup (
    name="diamondpriceprediction",
    versions='0.0.01',
    author="Ankit_gaur",
    author_email="ankitparashar000@gmail.com",
    install_requires=["pandas","numpy","scikit-learn","matplotlib","seaborn"],
    #install_requires=get_requirements=("requiements.txt"),
    packages=find_packages()
)