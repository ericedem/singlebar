from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='singlebar',
    version='0.0.1',
    description='Single update progress bar',
    long_description=readme,
    author='Eric Edem',
    author_email='ericedem@gmail.com',
    url='https://github.com/ericedem/singlebar',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
