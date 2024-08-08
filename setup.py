from setuptools import find_packages
from setuptools import setup

setup(
    name='pre-commit-hooks-bandit',
    description='A pre-commit hook to parse branch name to find ticket id to prepend to commit message',
    url='https://github.com/lterray/pre-commit-hooks',
    version='0.0.3',
    py_modules=["prepend_numeric_ticket_id"],

    author='Laszlo Terray',

    platforms='linux',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],

    packages=find_packages('.'),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'prepend_numeric_ticket_id = prepend_numeric_ticket_id:main',
        ],
    },
)