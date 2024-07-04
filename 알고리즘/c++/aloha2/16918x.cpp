#include <iostream>
#include <string>

using namespace std;

int R, C, N;
int board[205][205] = { 0, };

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> R >> C >> N;

	for (int i = 0; i < R; i++)
	{
		for (int j = 0; j < C; j++)
		{
			string temp;
			cin >> temp;
			
			if (temp.compare("."))
			{

			}
			cin >> board[i][j];
		}
	}

	return 0;
}