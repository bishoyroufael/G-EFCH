from setuptools import setup, find_packages

# https://stackoverflow.com/questions/14417236/setup-py-renaming-src-package-to-project-name
setup(name='GEFCH', version='1.0', packages=["schemas"], package_dir={'':'src'})