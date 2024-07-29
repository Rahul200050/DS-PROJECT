from setuptools import find_packages,setup
from typing import List



def get_requirements(file_path:str)->List[str]:
    '''  this function will return list of requirement '''
    requirements=[]

    with open(file_path) as file_obj:
         requirements=file_obj.readlines()
         requirements=[req.replace('\n',"") for req in requirements]

    return requirements


setup(
name='mlproject',
version='0.0.01',
author='rahul',
author_email='rahulgupta200050@gmail.com',
packages=find_packages(),
install_require=get_requirements('requirements.txt')
)