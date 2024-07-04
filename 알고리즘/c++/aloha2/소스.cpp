#include <iostream>
#include <vector>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int board[9][9];

	for (int i = 0; i < 9; i++)
	{
		for (int j = 0; j < 9; j++)
		{
			cin >> board[i][j];
		}
	}
	int max = board[0][0];
	int x =0 , y=0;

	for (int i = 0; i < 9; i++)
	{
		for (int j = 0; j < 9; j++)
		{
			if (max < board[i][j])
			{
				max = board[i][j];
				x = i;
				y = j;
			}
		}

	}

	cout << max << "\n" << x+1 << " " << y+1;

	return 0;
}