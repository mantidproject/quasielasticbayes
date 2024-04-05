# quasielasticbayes

This package provides a convenient set of Python wrappers for a set of routines used to perform Bayesian analysis
on quasi-elastic neutron-scattering data. The original Fortran code was written by Dr. Devinder Silvia, with 
supervision from Dr. Spencer Howells, in the 1980's. The longevity of the package is owed to the efforts of
Dr. Spencer Howells, and members of the Mantid Project team.

## Setup

The simplest way to develop this package involves creating a [conda](https://docs.conda.io/en/latest/miniconda.html) 
developer environment. To create a conda environment, run

```sh
mamba env create -f conda/develop/qeb-<os>-py310.yml
```

To activate the environment, run

```sh
conda activate qeb-dev-py310
```

## Building for conda-forge

To create and activate the build environment, run

```sh
mamba env create -f conda/recipe/qeb-build-py310.yml && conda activate qeb-build-py310
```

Enter the `conda/recipe` directory. To build the package, run

```sh
conda build . --output-folder .
```

To install the package built locally, run

```sh
conda install --use-local *-64/quasielasticbayes-*.tar.bz2
```

To run the tests, you will also need to install `pytest` and `numpy`.

```sh
conda install -c conda-forge numpy pytest
```

## Building for PyPi

If this is your first time interacting with PyPi then please see [here](https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives) for instructions of how to setup accounts and API tokens. 

To build a wheel and the source distribution tarball, run

```sh
./scripts/rebuild.sh
```

To install the wheel, run

```sh
pip install --force-reinstall dist/quasielasticbayes-0.2.0-cp310-cp310-*.whl
```

Once built the wheel can be uploaded using twine:

```sh
twine upload ./dist/name_of_wheel
```

## Run the Tests

To run the tests

```sh
pytest quasielasticbayes/test
```
