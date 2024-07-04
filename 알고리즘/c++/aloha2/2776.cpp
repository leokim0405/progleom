#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
vector <int> answer;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int T;
	cin >> T;

	for (int i = 0; i < T; i++)
	{
		vector <int> Ns;
		int N, M;

		cin >> N;
		for (int j = 0; j < N; j++)
		{
			int num;
			cin >> num;
			Ns.push_back(num);
		}
		sort(Ns.begin(), Ns.end());

		cin >> M;

		for (int l = 0; l < M; l++)
		{
			int num;
			cin >> num;
			if (binary_search(Ns.begin(), Ns.end(), num))
			{
				answer.push_back(1);
			}
			else
			{
				answer.push_back(0);
			}
		}

	}
	for (int k : answer)
	{
		cout << k << "\n";
	}



	return 0;
}