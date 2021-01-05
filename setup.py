import pathlib
import subprocess

from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop


__requires__ = ['pipenv']

packages = find_packages(exclude=['tests'])
base_dir = pathlib.Path(__file__).parent

pipenv_command = ['pipenv', 'install']
pipenv_command_dev = ['pipenv', 'install', '--dev']


class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        subprocess.check_call(pipenv_command_dev)
        develop.run(self)


class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        subprocess.check_call(pipenv_command)
        install.run(self)


with open(base_dir / 'README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='riotwrapper',
    long_description='\n' + long_description,
    packages=packages,
    version='0.1.0',
    description='Unofficial wrapper for the developer Riot API.',
    author='Victor Aquiles Alencar',
    license='MIT',
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    },
)
