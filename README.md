pointCloudGenerator
===================

#### A simple program to discretize surfaces from simple CAD models.

This is a full interface program that aims to discretize any kind of surface from
a CAD model in IGES (Initial Graphics Exchange Specification) format. The main goal
is to provide useful tools to create measurements errors and manufacturing errors,
which will be used to analyse how these erros affects the model or the assembly
in general.

It is currently under development, with this repo being used as the official repo.

![Alt text](img/interface.png?raw=true "interface")

### Instalation Instructions

At the moment, there aren't any releases for this project.
It's based on a CAD-Manipulation library: the PythonOCC wrapper of the OCCT (OpenCascade Technology). All the dependencies can be installed via Conda Package Management System. After installing the Anaconda Software from https://www.continuum.io/downloads, simply run:
```bash
conda create -n env -c numpy -c pythonocc -c oce pythonocc-core==0.17.3 python=3
```
This will create a Python Environment (just a folder with a Python Interpreter with the dependencies all set). This environment will contain, mainly:
* A Python binding for the Qt Platform (A GUI cross-platform framework) : PyQt
* A wrapper of the OCCT (OpenCascade Technology) : PythonOCC
* A package for numerical and scientific computing : NumPy

Further instructions and a binary for Windows based on the WinRAR Self-Extraction File (SFX) will be released soon.
