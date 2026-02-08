from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    """
    Esta funcion regresa la lista de requerimientos
    """
    requirements=[] #lista vacia que se llenara con las librerias de requirements.txt
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name = "ml_age_crabs_project",
    version = "0.0.1",
    author = "Alejandro Santos",
    author_email = "alejandrosantosgg1930@gmail.com",
    packages = find_packages(),
    install_requirements = get_requirements('requirements.txt'),
)
