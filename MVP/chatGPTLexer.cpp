#include <iostream>
#include <string>
#include <vector>
#include <cctype>

enum class TokenType {
    Identifier,
    Number,
    Operator,
    Unknown
};

struct Token {
    TokenType type;
    std::string value;
};

class Lexer {
public:
    explicit Lexer(const std::string& input) : text(input), pos(0) {}

    std::vector<Token> tokenize() {
        std::vector<Token> tokens;
        while (pos < text.size()) {
            char current = text[pos];
            
            if (std::isspace(current)) {
                ++pos;
                continue;
            }

            if (std::isalpha(current)) {  
                tokens.push_back(readIdentifier());
            }
            else if (std::isdigit(current)) {  
                tokens.push_back(readNumber());
            }
            else if (isOperator(current)) {  
                tokens.push_back({TokenType::Operator, std::string(1, current)});
                ++pos;
            }
            else {  
                tokens.push_back({TokenType::Unknown, std::string(1, current)});
                ++pos;
            }
        }
        return tokens;
    }

private:
    std::string text;
    size_t pos;

    Token readIdentifier() {
        size_t start = pos;
        while (pos < text.size() && std::isalnum(text[pos])) ++pos;
        return {TokenType::Identifier, text.substr(start, pos - start)};
    }

    Token readNumber() {
        size_t start = pos;
        while (pos < text.size() && std::isdigit(text[pos])) ++pos;
        return {TokenType::Number, text.substr(start, pos - start)};
    }

    bool isOperator(char c) {
        return c == '+' || c == '-' || c == '*' || c == '/' || c == '=';
    }
};

int main() {
    std::string code = "x = 42 + y";
    Lexer lexer(code);
    auto tokens = lexer.tokenize();

    for (const auto& token : tokens) {
        std::cout << "Token: " << token.value << " (";
        switch (token.type) {
            case TokenType::Identifier: std::cout << "Identifier"; break;
            case TokenType::Number: std::cout << "Number"; break;
            case TokenType::Operator: std::cout << "Operator"; break;
            case TokenType::Unknown: std::cout << "Unknown"; break;
        }
        std::cout << ")\n";
    }
}