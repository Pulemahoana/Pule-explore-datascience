from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Pulemahoana/Pule-explore-datascience.git',
    author='Pule Mahoana',
    author_email='Pulemahoana1@gmail.com'
)