#include <iostream>
#include <spdlog/spdlog.h>

using namespace std;

int main()
{
    spdlog::set_level(spdlog::level::debug);
    spdlog::warn("fuck");
    cout << "Hello World!" << endl;
    return 0;
}
