python_sources = [
  '__init__.py',
  'testing.py'
]

py3.install_sources(
  python_sources,
  pure: false,
  subdir: 'quasielasticbayes'
)

add_project_arguments('-O1', language: 'fortran')
ff = meson.get_compiler('fortran')
if ff.get_id() == 'gcc'
  add_project_arguments('-std=legacy', language: 'fortran')
endif

# module_name: [main_file, [additional_sources]]
module_map = {
  'ResNorm': ['ResNorm_main.f90', ['ResNorm_subs.f90', 'BlrRes.f90', 'Bayes.f90', 'Four.f90', 'Util.f90']],
  'Quest': ['Quest_main.f90', ['Quest_subs.f90', 'BlrRes.f90', 'Bayes.f90', 'Four.f90', 'Util.f90', 'Simopt.f90']],
  'QLse': ['QLse_main.f90', ['QLse_subs.f90', 'BlrRes.f90', 'Bayes.f90', 'Four.f90', 'Util.f90', 'Simopt.f90']],
  'QLres': ['QLres_main.f90', ['QLres_subs.f90', 'BlrRes.f90', 'Bayes.f90', 'Four.f90', 'Util.f90']],
  'QLdata': ['QLdata_main.f90', ['QLdata_subs.f90', 'Bayes.f90', 'Four.f90', 'Util.f90']],
  'Four': ['Four_main.f90', ['Four.f90']]
}

foreach name, sources : module_map

  gen_fwrappers = custom_target(
    f'gen-@name@-fwrappers',
    input: sources[0],
    output: [f'@name@module.c', f'@name@-f2pywrappers.f'],
    command: [py3, '-m', 'numpy.f2py', '@INPUT@', '-m', name, '--build-dir', '@OUTDIR@', '--backend', 'meson', '--lower'])

  sources = [sources[0], gen_fwrappers[0], gen_fwrappers[1]] + sources[1]

  py3.extension_module(
    name,
    sources,
    incdir_f2py / 'fortranobject.c',
    include_directories: inc_np,
    dependencies: py3_dep,
    install: true,
    subdir: 'quasielasticbayes')

endforeach
