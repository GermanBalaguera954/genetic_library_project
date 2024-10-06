from setuptools import setup, find_packages

setup(
    name="genetic_library",  # Nombre libreria
    version="0.1",  # Versión inicial
    author="German Balaguera Yenifer Garcia",  # Nombres de los autores
    author_email="gbalaguera@ucundinamarca.edu.co",  # Email
    description="Una librería para implementar algoritmos genéticos",
    long_description=open('README.md').read(),  # Incluye la descripción larga desde README.md
    long_description_content_type="text/markdown",  #README
    url="https://github.com/GermanBalaguera954/genetic_library_project",  # URL del proyecto
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Licencia
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',  #Compatible con la versión de python 3.10
    install_requires=[
    ],
)
