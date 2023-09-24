#include <iostream>
#include <vector>
#include <string>

int main() {
    int x, y;
    std::cin >> x >> y;
    int z = 2 * (x + y);
    std::vector<std::string> arr;
    arr.push_back(std::to_string(x));
    arr.push_back(std::to_string(y));
    arr.push_back(std::to_string(z));

    for (int i = 0; i < 3; i++) {
        std::cout << arr[i] << ":   " << std::oct << int(arr[i][0]) << "   " << int(arr[i][0]) << "   " << std::hex << int(arr[i][0]) << std::endl;
    }

    return 0;
}