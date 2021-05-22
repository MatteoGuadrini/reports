from setuptools import setup

__version__ = '0.0.9'

with open("README.md") as fh:
    long_description = fh.read()

setup(
    name='pyreports',
    version=__version__,
    packages=['pyreports'],
    url='https://github.com/MatteoGuadrini/pyreports',
    license='GNU General Public License v3.0',
    author='Matteo Guadrini',
    author_email='matteo.guadrini@hotmail.it',
    keywords='pyreports reports report csv yaml export excel database ldap dataset file executor book',
    maintainer='Matteo Guadrini',
    maintainer_email='matteo.guadrini@hotmail.it',
    install_requires=['ldap3', 'pymssql', 'mysql-connector-python', 'psycopg2-binary', 'tablib', 'tablib[xlsx]'],
    description='pyreports is a python library that allows you to create complex report from various sources',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Operating System :: OS Independent",
        ],
    python_requires='>=3.6'
)
