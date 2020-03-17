from distutils.core import setup

setup(
    name='mypy_r',
    version='1.0',
    description='Recursive mypy that find package directories',
    author='Joe Ceresini',
    author_email='joe@ceresini.com',
    packages=['mypy_r'],
    entry_points={
        'console_scripts': [
            'mypy-r=mypy_r.__main__:console_script',
        ]
    },
    install_requires=[
        'mypy',
    ],
)
