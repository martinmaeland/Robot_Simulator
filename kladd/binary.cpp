#include <iostream>
#include <bitset>

int main() {

  const uint8_t channel = 3;
  const uint8_t a = 0b00001111;

  const uint8_t adcsra = 0b01000000;

  for (int i=0; i<8; i++) {
    std::cout << i << ":" << std::bitset<8>(0 | (1 << i)) << std::endl;
  }

}
