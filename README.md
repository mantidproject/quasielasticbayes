# quasielasticbayes

This package provides a convenient set of Python wrappers for a set of routines used to perform Bayesian analysis
on quasi-elastic neutron-scattering data. The original Fortran code was written by Dr. Devinder Silvia, with 
supervision from Dr. Spencer Howells, in the 1980's. The longevity of the package is owed to the efforts of
Dr. Spencer Howells, and members of the Mantid Project team.

## Building a Conda package

To create and activate the build environment, run

```sh
mamba env create -f conda/recipe/qeb-build-py310.yml && conda activate qeb-build-py310
```

To build a Conda package, run

```sh
conda build conda/recipe/ --output-folder .
```

## Building a PyPi package

To create and activate the build environment, run

```sh
mamba env create -f conda/develop/qeb-<os>-py310.yml && conda activate qeb-dev-py310
```

To build a wheel and the source distribution tarball, run

```sh
./scripts/rebuild.sh
```

## Run the Tests

To create and activate the test environment, run

```sh
mamba env create -f conda/recipe/qeb-ci-py310.yml && conda activate qeb-ci-py310
```

To install a locally-built Conda package, run

```sh
conda install --use-local *-64/quasielasticbayes-*.tar.bz2
```

To install a locally-built PyPi wheel, run

```sh
pip install --force-reinstall dist/quasielasticbayes-*.whl
```

To run the tests on the installed package

```sh
pytest quasielasticbayes/test
```
