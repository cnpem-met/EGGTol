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
