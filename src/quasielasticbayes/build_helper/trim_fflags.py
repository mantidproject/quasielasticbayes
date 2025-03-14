import os


def filter_fflags():
    """
    Using the 'gfortran_linux-64' and 'gfortran_osx-64' conda packages gives poor fit results by default
    because they set several optimization compiler flags which alter the operation of the Fortran code. We
    must therefore remove these flags from the 'FFLAGS' environment variable before performing the compilation.
    """
    fflags_value = os.environ.get('FFLAGS')
    if isinstance(fflags_value, str):
        fflags_value = fflags_value.replace("-fstack-protector ", "")
        fflags_value = fflags_value.replace("-fstack-protector-strong ", "")
        os.environ['FFLAGS'] = fflags_value


if __name__ == '__main__':
    filter_fflags()
