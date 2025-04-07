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

To create and activate the build environment, run

```sh
mamba env create -f conda_envs/qeb-build-env-[os].yml && conda activate qeb-build-env-[os]
```

To build and install the package locally, run

```sh
./scripts/rebuild.sh
```

To run the tests on the installed package

```sh
pytest src/quasielasticbayes/test
```
