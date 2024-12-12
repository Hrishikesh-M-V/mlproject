from setuptools import find_packages,setup
from typing import List
# the find_packages() goes to each folder and searches for __init__.py and builds the package, so
# that we can import it when required

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n"," ") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
name = 'mlproject',
version = '0.0.1',
author = 'Hrishikesh',
author_email = 'hrishi002237@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)