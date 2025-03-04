cmake_minimum_required(VERSION 3.17.2)
project(${SKBUILD_PROJECT_NAME} LANGUAGES C Fortran)

find_package(
  Python
  COMPONENTS Interpreter Development.Module NumPy
  REQUIRED)

# F2PY headers
execute_process(
  COMMAND "${PYTHON_EXECUTABLE}" -c
          "import numpy.f2py; print(numpy.f2py.get_include())"
  OUTPUT_VARIABLE F2PY_INCLUDE_DIR
  OUTPUT_STRIP_TRAILING_WHITESPACE)

add_library(fortranobject OBJECT "${F2PY_INCLUDE_DIR}/fortranobject.c")
target_link_libraries(fortranobject PUBLIC Python::NumPy)
target_include_directories(fortranobject PUBLIC "${F2PY_INCLUDE_DIR}")
set_property(TARGET fortranobject PROPERTY POSITION_INDEPENDENT_CODE ON)

function(build_library module_name main_file)
  add_custom_command(
    OUTPUT "${module_name}module.c" "${module_name}-f2pywrappers.f"
    DEPENDS "${main_file}"
    VERBATIM
    COMMAND "${Python_EXECUTABLE}" -m numpy.f2py
            "${main_file}" -m "${module_name}" --lower)

  # ARGN holds the aditional source files
  python_add_library(
      "${module_name}" MODULE "${CMAKE_CURRENT_BINARY_DIR}/${module_name}module.c"
      "${CMAKE_CURRENT_BINARY_DIR}/${module_name}-f2pywrappers.f"
      "${main_file}"
      "${ARGN}" WITH_SOABI)
  target_compile_options("${module_name}" PRIVATE $<$<COMPILE_LANGUAGE:Fortran>:-O1 -std=legacy>)
  target_link_libraries("${module_name}" PRIVATE fortranobject)
  IF (WIN32)
    target_link_options("${module_name}" PRIVATE -static -static-libfortran -static-libgcc)
  ENDIF()
  install(TARGETS "${module_name}" DESTINATION ${SKBUILD_PROJECT_NAME})
endfunction()

build_library(
  "ResNorm"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/ResNorm_main.f90"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/ResNorm_subs.f90"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/BlrRes.f90"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/Bayes.f90"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/Four.f90"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/Util.f90")

build_library(
  "Quest"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/Quest_main.f90"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/Quest_subs.f90"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/BlrRes.f90"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/Bayes.f90"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/Four.f90"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/Util.f90"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/Simopt.f90")

build_library(
  "QLse"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/QLse_main.f90"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/QLse_subs.f90"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/BlrRes.f90"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/Bayes.f90"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/Four.f90"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/Util.f90"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/Simopt.f90")

build_library(
  "QLres"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/QLres_main.f90"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/QLres_subs.f90"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/BlrRes.f90"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/Bayes.f90"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/Four.f90"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/Util.f90")

build_library(
  "QLdata"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/QLdata_main.f90"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/QLdata_subs.f90"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/Bayes.f90"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/Four.f90"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/Util.f90")

build_library(
  "Four"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/Four_main.f90"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/quasielasticbayes/Four.f90")
