from setuptools import setup, find_packages


setup(
    name='singlebar',
    version='0.0.3',
    description='Single update progress bar',
    author='Eric Edem',
    author_email='ericedem@gmail.com',
    url='https://github.com/ericedem/singlebar',
    packages=find_packages(exclude=('tests', 'docs'))
)
