#include <string>
#include <vector>
#include <cctype>

class SimpleTokenizer {
public:
    explicit SimpleTokenizer(const std::string& text) {
        tokenize(text);
    }

    const std::vector<std::string>& tokens() const {
        return tokens_;
    }

private:
    std::vector<std::string> tokens_;

    void tokenize(const std::string& text) {
        std::string current;

        for (char ch : text) {
            const unsigned char uc = static_cast<unsigned char>(ch);

            if (std::isspace(uc) || std::strchr(",.!?;:()\"'", ch) != nullptr) {
                if (!current.empty()) {
                    tokens_.push_back(current);
                    current.clear();
                }
                continue;
            }

            current += ch;
        }

        if (!current.empty()) {
            tokens_.push_back(current);
        }
    }
};