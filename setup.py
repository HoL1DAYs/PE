from setuptools import setup


APP_NAME = 'PE'
APP = ['pe.py']

setup(
    app=APP,
    name=APP_NAME,
    setup_requires=['py2exe'],
)