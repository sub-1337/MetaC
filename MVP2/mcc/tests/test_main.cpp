#include <catch2/catch_test_macros.hpp>
#include "../src/lexer.h"
#include <string>

TEST_CASE("basic test") {
    lexer lex;
    lex.parse("let a = 10;");
    //REQUIRE(1 + 1 == 2);
}
