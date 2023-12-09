from setuptools import setup
setup(
    name='constructionist',
    version='0.0.1',
    packages=['constructionist'],
    entry_points = {
        'console_scripts': [
            'constructionist = constructionist.__main__:main'
        ]
    }
)