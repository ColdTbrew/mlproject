from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(path:str) -> List[str]:
    '''
    Read requirements.txt file and return it as a list of strings
    '''
    with open(path) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
    
setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Coldbrew',
    author_email= 'shchoi8687@hotmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt'),

)