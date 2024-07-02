#include <iostream>
#include <vector>

using namespace std;

int N,Q;
/*
vector<int> holes;
vector<int> dotoris;
*/
vector<int> answer;


int holes[100005] = { 0, };
int dotoris[100005] = { 0, };

int main()
{
	ios::sync_with_stdio(false);

	cin >> N;

	//
	//
	for (int i = 0; i < N; i++)
	{
		cin >> holes[i];
	}

	cin >> Q;

	for (int i = 0; i < Q; i++)
	{
		int input, temp;
		cin >> input;
		temp = input + i;

		if (true)
		{

		}
	}

	for (int i = 0; i < Q; i++)
	{
		int dotori = dotoris[i];

		for (int j = 0; j < N; j++)
		{
			if (holes[j] >= dotori - j)
			{
				answer.push_back(j + 1);
				break;
			}
		}
	}




	//
	//
	/*
	for (int i = 0; i < N; i++)
	{
		int temp;
		cin >> temp;
		holes.push_back(temp);
	}

	cin >> Q;

	for (int i = 0; i < Q; i++)
	{
		int temp;
		cin >> temp;
		dotoris.push_back(temp);
	}

	
	for (int j = 0; j < Q; j++)
	{
		for (int i = 0; i < N; i++)
		{
			if (holes[i] >= dotoris[j] - i)
			{
				answer.push_back(i + 1);
				break;
			}
		}
	}*/

	for (int k : answer)
	{
		cout << k << " ";
	}
	
	return 0;
}