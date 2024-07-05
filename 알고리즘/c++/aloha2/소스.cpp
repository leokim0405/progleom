#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int C; cin >> C;

	vector<string> input;
	vector<int> answer;

	for (int i = 0; i < C; i++)
	{
		string sentence;
		cin >> sentence;
		input.push_back(sentence);
	}

	for (string str : input)
	{
		int length = str.length(), score = 0, temp = 1;
		for (int j = 0; j < length; j++)
		{
			if (str[j] == 'O')
			{
				score += temp++;

			}
			else
			{
				temp = 1;
			}
		}
		answer.push_back(score);
	}

	for (int x : answer)
	{
		cout << x << "\n";
	}


	return 0;
}