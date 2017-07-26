import json
from setuptools import setup, find_packages


setup(
    name='canadian-nutrient-file',
    version='0.0.1',
    author='Cyril Robert',
    author_email='cyril@hippie.io',
    url='http://github.com/cyrilrbt/canadian-nutrient-file',
    install_requires=[
        'setuptools',
        'flask',
        'mongoengine',
        'flask-mongoengine',
        'flask-script',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'cnf = cnf.main:main',
        ]},
)
