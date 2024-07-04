#include <iostream>
#include <vector>

using namespace std;

long long odd[100005] = { 0, };	//odd
long long even[100005] = { 0, };	//even

vector<long long> answer;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	long long T;
	cin >> T;

	odd[1] = 1;
	odd[2] = 1;
	odd[3] = 2;

	even[1] = 0;
	even[2] = 1;
	even[3] = 2;

	for (int i = 0; i < T; i++)
	{
		long long N;
		cin >> N;
		answer.push_back(N);

		if (N < 4)
		{
			continue;
		}

		for (int j = 4; j < N+1; j++)
		{
			odd[j] = (even[j - 1] + even[j - 2] + even[j - 3])%1000000009;
			even[j] = (odd[j - 1] + odd[j - 2] + odd[j - 3])%1000000009;
		}
	}


	for (int i = 0; i < T ; i++)
	{
		cout << odd[answer[i]] << " " << even[answer[i]];
		if (i != T-1)
		{
			cout << "\n";
		}
	}

	return 0;
}