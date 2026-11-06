#include <iostream>
#include <string>
#include <urllib.h>
#include <fstream>


int main() {
    std::string url = "https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/main/ch02/01_main-chapter-code/the-verdict.txt";
    std::string file_path = "the-verdict.txt";
    urllib::download(url, file_path);

    std::fstream file("the-verdict.txt", std::ios::in | std::ios::binary);
    std::string raw_text;
    //getline(file, raw_text, '\0');
    
    std::istringstream words(raw_text);
    std::string word;
    
    for (int i = 0; i < 99 && (words >> word); ++i){
        if (i > 0) std::cout << " ";
        std::cout << word;
    }
    std::cout << "\n";
    std::cout << "File length: " << file.tellg() << " bytes" << std::endl;

    
}