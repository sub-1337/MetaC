cmake_minimum_required(VERSION 3.5)

project(mcc LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)


include(FetchContent)

FetchContent_Declare(
    spdlog
    GIT_REPOSITORY https://github.com/gabime/spdlog.git
    GIT_TAG v1.x
)

FetchContent_Declare(
    Catch2
    GIT_REPOSITORY https://github.com/catchorg/Catch2.git
    GIT_TAG v3.8.1
)

FetchContent_MakeAvailable(spdlog Catch2)

#find_package(spdlog REQUIRED)

add_executable(mcc "src/main.cpp" "src/lexer.cpp" "src/lexer.h")

target_link_libraries(mcc PRIVATE spdlog::spdlog)

include(GNUInstallDirs)

install(TARGETS mcc
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

# tests
enable_testing()

add_executable(mcc_tests
    tests/test_main.cpp
 "src/lexer.cpp" "src/lexer.h")

target_link_libraries(mcc_tests PRIVATE
    Catch2::Catch2WithMain spdlog::spdlog
)

list(APPEND CMAKE_MODULE_PATH ${catch2_SOURCE_DIR}/extras)
include(Catch)
catch_discover_tests(mcc_tests)

include(GNUInstallDirs)

install(TARGETS mcc
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)


