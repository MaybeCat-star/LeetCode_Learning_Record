#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n = 20;
    int factorial = 1;
    for(int i = 1; i <=n; ++i){
        factorial *= i;
    }
    int a = 1;
    a = 1LL * a;
    for(int i = 1; i <= n; i++){
        a *= i;
    }
    if(typeid(a) == typeid(int)){
        cout << "int" << endl;
    }
    cout << a << endl;
    cout << factorial << endl;
}