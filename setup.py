from setuptools import find_packages, setup
from typing import List

def get_requirements(filepath:str)->List[str]:
  
  HYPHEN_E_DOT = "-e ."
  
  requirements=[]
  
  with open(filepath) as file_object:
    requirements=[req.replace("\n", "") for req in file_object.readlines()]
    if HYPHEN_E_DOT in requirements:
      requirements.remove(HYPHEN_E_DOT)
    return requirements
  


setup(
  name="Machine Learning Project",
  version="0.0.1",
  author="Huraira",
  author_email="hurairahamid12@gmail.com",
  packages=find_packages(),
  install_requires=get_requirements("requirements.txt")
)