#include <iostream>
#include <string>

int main(){
    std::string name = "Spot";
    int legs = 4;
    double speed = 1.5;
    bool is_walking = true;

    std::cout << is_walking << name << " has " << legs << " legs, speed =" << speed << std::endl;
    return 0;
}