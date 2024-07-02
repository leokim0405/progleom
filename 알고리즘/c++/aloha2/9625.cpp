#include <iostream>

using namespace std;

int K;
int answer[2];

void foo(int a, int b);

int main()
{
	cin >> K;
	answer[0] = 1;	//a
	answer[1] = 0;	//b
	
	for (int i = 0; i < K; i++)
	{
		foo(answer[0], answer[1]);
	}

	for(int k : answer)
	{
		cout << k << " ";
	}


	return 0;
}

void foo(int a, int b)
{
	answer[0] = b;			//a
	answer[1] = a + b;		//b

}