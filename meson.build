project(
  'quasielasticbayes',
  'c',
  version: '0.3.0',
  license: 'BSD-3',
)

add_languages('fortran')

py3 = import('python').find_installation(pure: false)
py3_dep = py3.dependency()

incdir_numpy = run_command(
  py3,
  ['-c', 'import numpy; print(numpy.get_include())'],
  check : true
).stdout().strip()

incdir_f2py = run_command(
  py3,
  ['-c', 'import numpy.f2py; print(numpy.f2py.get_include())'],
  check : true
).stdout().strip()

inc_np = include_directories(incdir_numpy, incdir_f2py)

subdir('src/quasielasticbayes')