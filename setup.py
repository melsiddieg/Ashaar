import os
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(name='Ashaar',
      version='0.0.2',
      url='https://github.com/ARBML/Ashaar',
      description="Arabic poetry analysis and generation library",
      long_description=readme,
      long_description_content_type='text/markdown',
      author_email='arabicmachinelearning@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=required,
      python_requires=">=3.9",
      include_package_data=True,
      zip_safe=False,
      )
