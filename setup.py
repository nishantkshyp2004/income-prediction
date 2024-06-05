from setuptools import find_packages , setup
from typing import List

hypen_e = "-e ."

def get_requirements(filepath : str) -> List[str]:
    requirements = []

    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace("\n" , " ") for i in requirements]

        if hypen_e in requirements:
            requirements.remove(hypen_e)

setup(name='ML_pipeline_project',
      version='0.0.1',
      description='Python Ml Project',
      author='Shailesh Gaddam',
      author_email='shaileshgaddam10@gmail.com',
      packages=find_packages(),
      install_requires = get_requirements("requirements.txt") 
     )

