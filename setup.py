from setuptools import setup, find_packages

setup(
    name='MoneyMe',
    version='0.0.0',
    description='Simple Money Management',
    author='Trevor Hiebert',
    url='https://github.com/Funnnnn/MoneyManager',
    packages=find_packages(exclude='tests'),
    entry_points={
        'console_scripts': [
            'moneyme = moneyme.__main__:main',
        ],
    },
)
