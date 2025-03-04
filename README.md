# quasielasticbayes

This package provides a convenient set of Python wrappers for a set of routines used to perform Bayesian analysis
on quasi-elastic neutron-scattering data. The original Fortran code was written by Dr. Devinder Sivia, with 
supervision from Dr. Spencer Howells, in the 1980's. The longevity of the package is owed to the efforts of
Dr. Spencer Howells, and members of the Mantid Project team.

The package is available on [conda-forge](https://anaconda.org/conda-forge/quasielasticbayes) and [PyPi](https://pypi.org/project/quasielasticbayes).

## Install the package

To install this package from conda-forge, run

```sh
conda install -c conda-forge quasielasticbayes
```

To install this package from PyPi, run

```sh
pip install quasielasticbayes
```

## Develop: Building the PyPi package

To create and activate the build environment, run (use `conda_envs/pypi-build-py310-win.yml` on Windows)

```sh
mamba env create -f conda_envs/pypi-build-py310.yml && conda activate qeb-pypi-build-py310
```

To build a wheel and the source distribution tarball, run

```sh
./scripts/rebuild.sh
```

To install a locally-built PyPi wheel for testing, run

```sh
pip install --force-reinstall dist/quasielasticbayes-*.whl
```

To run the tests on the installed package

```sh
pytest src/quasielasticbayes/test
```
