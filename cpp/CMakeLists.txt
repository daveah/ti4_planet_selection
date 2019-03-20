cmake_minimum_required(VERSION 3.12.0)

# Project settings
project(ti4_planet_selection VERSION 0.1 LANGUAGES CXX)

# Global Settings
message("CMAKE_BUILD_TYPE is ${CMAKE_BUILD_TYPE}")
set(CMAKE_INSTALL_PREFIX "${CMAKE_SOURCE_DIR}/install/${CMAKE_BUILD_TYPE}"
  CACHE PATH "default install path" FORCE)
message("CMAKE_INSTALL_PREFIX is ${CMAKE_INSTALL_PREFIX}")

# Compile flags
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Werror -Wno-attributes")
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# Global search directories
set(BOOST_ROOT /home/u91dah/lib/boost)
set(GTEST_ROOT /usr/local)
set(pybind11_DIR /usr/local)
set(PYTHON3_ROOT_DIR /home/u91dah/anaconda3)

# Boost
find_package(Boost 1.67.0 REQUIRED COMPONENTS
  program_options
  )

# GTest
find_package(GTest REQUIRED)
include(CTest)
include(GoogleTest)

# Python
find_package(Python3 COMPONENTS Development REQUIRED)

# Pybind11
set(PYBIND11_CPP_STANDARD -std=c++1z)
set(PYBIND11_PYTHON_VERSION ${PYTHONLIBS_VERSION_STRING})
find_package(pybind11 REQUIRED)

# Bash
find_program(BASH_PROGRAM bash)

# Include all libraries

# Executable
file(GLOB ALL_SOURCES CONFIGURE_DEPENDS "*.cpp")
add_executable(ti4_planet_selection ${ALL_SOURCES})
target_include_directories(ti4_planet_selection PUBLIC
  $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}>)
target_link_libraries(ti4_planet_selection
  Boost::boost
  Boost::program_options)

# Installation
install(
  TARGETS ti4_planet_selection
  DESTINATION bin
  )
