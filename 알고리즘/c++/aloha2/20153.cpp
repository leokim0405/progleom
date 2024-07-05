#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

long long a[2222224][23] = { 0 };

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	vector<int> numbers;

	cin >> N;
	int result = 0, temp;
	for (int i = 0; i < N; i++)
	{
		cin >> temp;
		numbers.push_back(temp);
		result ^= temp;
	}

	int result2 = result;

	for (int j = 0; j < N; j++)
	{
		result2 = max(result2, result^numbers[j]);
	}

	cout << result2 << result2;

	/*
	for (int i = 0; i < N; i++)
	{
		int temp, j = 0;
		cin >> temp;
		while (temp != 0)
		{
			if ((temp & 1) == 0)
			{
				a[i][j] = 0;
			}
			else
			{
				a[i][j] = 1;
			}
			j++;
			temp = temp >> 1;
		}
	}

	vector<int> result;

	for (int h = 0; h < N; h++)
	{

		int max = 0, sum = 1;

		for (int x = 0; x < 23; x++)
		{
			int isOdd = 0;
			for (int n = 0; n < N; n++)
			{
				isOdd ^= a[n][x];
			}

			if (isOdd)
			{
				cout << "x : " << x << endl;
				cout << "sum : " << sum << endl;
				max += sum;
			}

			sum = sum << 1;
		}
	}

	int answer = *max_element(result.begin(), result.end());
	cout << answer;*/

	return 0;
}