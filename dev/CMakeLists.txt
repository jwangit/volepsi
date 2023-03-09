cmake_minimum_required(VERSION 3.15)
project(prf)

# set(CMAKE_PREFIX_PATH "/home/jwang/PSI/deps-vole/include")

find_package(cryptoTools  REQUIRED)

ADD_EXECUTABLE(prf prf.cpp)

target_link_libraries(prf oc::cryptoTools)