from struct import pack
from setuptools import setup

setup(
    name='Mensajes',
    version='3.0',
    description='Un paquete para saludar y despedir',
    author='Nirvana Belen González López',
    author_email='nivaniz2019@gmail.com',
    url='https://www.hektor.dev',
    packages=['mensajes', 'mensajes.hola', 'mensajes.adios'],
    scripts=['test.py']
)
