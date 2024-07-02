#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int N;
	cin >> N;
	int length = 2 * N - 1;

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < length; j++)
		{
			if (j > length /2 - i - 1 && j <length/2 + i + 1)
			{
				cout << "*";
			}
			else
			{
				cout << " ";
			}
		}
		cout << endl;
	}

	return 0;
}