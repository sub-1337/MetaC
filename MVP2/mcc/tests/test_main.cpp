#include <catch2/catch_test_macros.hpp>
#include "../src/lexer.h"
#include <spdlog/spdlog.h>
#include <string>

TEST_CASE("basic test") {
    mc::lexer lex;
    auto res = lex.parse("let a = 10;");
    for (auto it : res)
    {
        spdlog::info(it.getValue<mc::str>());
    }
    //REQUIRE(1 + 1 == 2);
}

TEST_CASE("basic value test") {
    mc::token token;
    token.setValue(mc::token_type::teminal, mc::terminal::none);
    if (token.type == mc::token_type::teminal)
    {
        auto val = token.getValue<mc::terminal>();
        REQUIRE(val == mc::terminal::none);
    }
    else
    {
        FAIL("error - wrong type has set");
    }
}

TEST_CASE("basic value test 2") {
    mc::token token;
    token.setValue(mc::token_type::teminal, mc::terminal::let);
    if (token.type == mc::token_type::teminal)
    {
        auto val = token.getValue<mc::terminal>();
        REQUIRE(val == mc::terminal::let);
    }
    else
    {
        FAIL("error - wrong type has set");
    }
}

TEST_CASE("basic value test 3") {
    mc::token token;
    token.setValue(mc::token_type::object, mc::str("a"));
    if (token.type == mc::token_type::object)
    {
        auto val = token.getValue<mc::str>();
        REQUIRE(val == mc::str("a"));
    }
    else
    {
        FAIL("error - wrong type has set");
    }
}