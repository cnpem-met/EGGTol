### Instalation Instructions

At the moment, there aren't any releases for this project.
It's based on a CAD-Manipulation library: the PythonOCC wrapper of the OCCT (OpenCasCADe Technology). All the dependencies can be installed via Conda Package Management System. After installing the Anaconda Software from https://www.continuum.io/downloads, simply run:
```bash
conda create -n env -c numpy -c pythonocc -c oce pythonocc-core==0.17.3 python=3
```
Further instructions and a binary for Windows will be released soon.
