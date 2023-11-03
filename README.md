# LLVM JITLink AArch32 Execution Testsuite
This repository provides a convenient environment and tests to be executed in an AArch32 device. 

## Prerequisites
- lit 
- FileCheck
- clang

For a Raspberry Pi device, these commands can be run:
```
pip3 install lit
```
A Python venv might be required to be activated if pip is managed by system.

Since Clang or FileCheck won't be tested they can be installed through a package manager.

```
sudo apt install clang llvm
```
FileCheck might be versioned, depending on the package installed. If so you can soft link as such:
```
which FileCheck-14
  /usr/bin/FileCheck-14
sudo ln -s /usr/bin/FileCheck-14 /usr/bin/FileCheck
```
So that lit tests can refer to the FileCheck binary of the system. 
