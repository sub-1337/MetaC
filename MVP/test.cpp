#include <iostream>
#include <string>

class Lexer
{

};

class Parser
{
public:
    std::wstring source;
};

int main()
{
    Parser parser;
    parser.source = L"let x = 10;";
    return 0;
}