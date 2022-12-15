#include <iostream>

int multiply(int x, int y)
{
  int product = x * y;
  return product;
}


int main()
{
  int x = 5;
  int y = 10;
  int result = multiply(x, y);
  int z = 0;
  for(int i = 0; i < 10; i++){
    z = z + i;
  }
  std::cout << z << std::endl;
  std::cout << "Hello, World!" << "\n" << "Hello, New Line!" << std::endl;
  std::cout << result << std::endl;
  
  return 0;
}
