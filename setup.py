import json
from setuptools import setup, find_packages


setup(
    name='canadian-nutrient-file',
    version='0.0.5',
    author='Cyril Robert',
    author_email='cyril@hippie.io',
    url='http://github.com/cyrilrbt/canadian-nutrient-file',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Natural Language :: French',
        'Programming Language :: Python :: 3',
        'Topic :: Database',
    ],
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
