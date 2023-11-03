# -*- Python -*-

# Configuration file for the 'lit' test runner.

import os

import lit.formats

# name: The name of this test suite.
config.name = "jitlink-aarch32-testsuite"

# testFormat: The test format to use to interpret tests.
config.test_format = lit.formats.ShTest(True)

# suffixes: A list of file extensions to treat as test files. This is overriden
# by individual lit.local.cfg files in the test subdirectories.
config.suffixes = [".c"]

# excludes: A list of directories to exclude from the testsuite. The 'Inputs'
# subdirectories contain auxiliary inputs for various tests in their parent
# directories.
config.excludes = ["Inputs", "CMakeLists.txt", "README.txt", "LICENSE.txt"]

# test_source_root: The root path where tests are located.
config.test_source_root = os.path.dirname(__file__)

# test_exec_root: The root path where tests should be run.
config.test_exec_root = os.path.join(config.my_src_root, "test")


config.substitutions.append(('%llvm-jitlink',
    os.path.join(config.my_src_root, 'bin/llvm-jitlink')))

config.substitutions.append(('%FileCheck',
    os.path.join(config.my_src_root, 'bin/FileCheck')))
