from setuptools import setup, find_packages
import sys, os

version = '0.1.0'

setup(
    name='chainedrandom',
    version=version,
    description="Chained Random Numbers",
    long_description="""
Simple chained random number generator.
For repeatable stochastic modeling.""",
    classifiers=[],
    author='Anders Pearson',
    author_email='anders@columbia.edu',
    url='',
    license='BSD',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    entry_points="""
      # -*- Entry points: -*-
      """,
)
