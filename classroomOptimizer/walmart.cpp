#include <iostream>
#include <vector>
using namespace std;

int main(){
    vector<int> coins;
    coins.push_back(1);
    int amount = 1;
    int remainder;
    int index = coins.size() - 1;
    int temp = amount;
    int numcoins = 0;

    for(int i = 0; i < coins.size(); i++){
        while(temp > 0){
            numcoins++;
            temp = temp - coins[index - i];
        }
        remainder = temp % coins[index - i];
    }

    if(remainder != 0){
        numcoins = -1;
    }
    cout << numcoins << endl;

}