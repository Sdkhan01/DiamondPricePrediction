from setuptools import setup, find_packages
from typing import List

Hypen_dot = '-e .'
def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n","") for req in requirements]

        if Hypen_dot in requirements:
            requirements.remove(Hypen_dot)

    return requirements


setup (

    name = 'diamondPricePrediction',
    version = '0.1',
    author = 'shadab',
    author_email = 'khanshadab7860000@gmail.com',
    install_requires = get_requirements('requirements.txt'),
    packages = find_packages()
)