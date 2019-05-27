from setuptools import setup

setup(
    name='5mzb',
    version='1.0.0',
    keywords=['money keeper'],
    description='5mzb: money keeper',
    long_description='',
    license='Apache Lisence 2.0',
    author='catroll',
    author_email='ninedoors@126.com',
    url='https://www.5mzb.com',
    packages=['5mzb'],
    entry_points={
            'console_scripts': [
                '5mzb = 5mzb.cli.main',
            ],
    }
)
