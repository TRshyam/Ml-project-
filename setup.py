from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)-> List[str]:
    requirements=[]
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[ele.replace("\n","") for ele in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")


setup(
    name="mlproject",
    version='0.0.1',
    author='Shyam',
    author_email='t.r.shyam0007@gmail.com',
    package=find_packages(),
    install_requires=get_requirements('requirements.txt')
)