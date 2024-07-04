#include <iostream>
#include <vector>

using namespace std;

vector <int> answer;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int N, X;
	cin >> N >> X;

	for (int i = 0; i < N; i++)
	{
		int T;
		cin >> T;
		if (T < X)
		{
			answer.push_back(T);
		}
	}

	for (int i : answer)
	{
		cout << i << " ";
	}

	return 0;
}