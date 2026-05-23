from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_req(file_path:str)->List[str]:
    requirements = []

    with open(file_path) as fileobj:
        requirements = fileobj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name="Wine Predicition",
    version='0.0.1',
    author='Nishit',
    author_email='nishitmalkania@gmail.com',
    packages=find_packages(),
    install_requires = get_req('requirements.txt')

)
