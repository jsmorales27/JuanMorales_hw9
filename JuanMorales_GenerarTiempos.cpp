#include <iostream>
#include <typeinfo>
#include <math.h>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <fstream>

using namespace std;
#define n 35
float get_time(int N);
int fibonacci(int No);

int main(){
	for (int j=0;j<=n;j=j+1){
		cout <<j<<","<<get_time(j)<<"\n";
	}
	return 0;
}

int fibonacci(int N){
	if (N<=1){
		return N;
	}
	else{
		return fibonacci(N-1)+fibonacci(N-2);
	}
}

float get_time(int No){
	clock_t t;
	t = clock();
	fibonacci(No);
	t = clock() - t;
	float time = ((float)t)/CLOCKS_PER_SEC;
	return time;
}










