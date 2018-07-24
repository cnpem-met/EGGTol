EGGTol: Error Generator for Geometric Tolerancing
=================================================

#### A simple program to discretize surfaces from simple CAD models.

![The splash screen](img/splash.png?raw=true "splash")

This is a full interface program that aims to discretize any kind of surface from
a CAD model in IGES (Initial Graphics Exchange Specification) format. The main goal
is to provide useful tools to create measurements errors and manufacturing errors,
which will be used to analyse how these erros affects the model or the assembly
in general.

It is currently under development, with this repo being used as the official repo.

![The current interface](img/interface.png?raw=true "interface")

### Instalation Instructions

The software is based on a CAD-Manipulation library: the PythonOCC wrapper of the OCCT (OpenCascade
Technology). All the dependencies can be installed via Conda Package Management System. After
installing [the Anaconda Software](https://www.continuum.io/downloads), simply run:
```bash
conda create -n env -c numpy -c pythonocc -c oce pythonocc-core==0.17.3 python=3
```
This will create a Python Environment (just a folder with a Python Interpreter with the dependencies
all set). This environment will contain, mainly:

* A Python binding for the Qt Platform (A GUI cross-platform framework) : PyQt
* A wrapper of the OCCT (OpenCascade Technology) : PythonOCC
* A package for numerical and scientific computing : NumPy

After installing the Python Environment, rename the generated folder to "env" and copy it to the
root folder of this project. The src\runMain.vbs is the script for launching the software.

### Binary Release

After a few months of work, finally a binary release is avaliable at https://hideak.github.io.
This binary file is a WinRAR Self-Extraction File, which is itself a .exe file containing an
Installation Wizard. Just download the file and follow the Setup Instruction on your display.

### License

This project is under the LGPL-3.0 (GNU Lesser General Public License), version 3 from 29 June
2007.

### Authors

This is an Undergraduate Project that aims developing a software to discretize most CAD surfaces
from CAD models.

Created mainly by **Willian Hideak Arita da Silva** under orientation of **Rodrigo Junqueira Leão**
and **Crhistian Raffaelo Baldo** in CNPEM (Centro Nacional de Pesquisa em Energia e Materiais) -
Campinas/SP, Brazil.
