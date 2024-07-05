#include <iostream>
#include <vector>

using namespace std;

int fingers[6] = { 0, };

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N; cin >> N;
	int check1 = 0, check2 = 0, check3 = 0;

	for (int i = 0; i < N; i++)
	{
		int f1, f2;
		cin >> f1 >> f2;
		fingers[f1]++; fingers[f2]++;
		
		if ((f1 == 1 && f2 == 3) || (f1 == 3 && f2 ==1))
		{
			check1 = 1;
		}
		else if ((f1 == 4 && f2 == 3) || (f1 == 3 && f2 == 4))
		{
			check2 = 1;
		}
		else if ((f1 == 1 && f2 == 4) || (f1 == 4 && f2 == 1))
		{
			check3 = 1;
		}

	}

	if (fingers[2] == 0 && fingers[5] == 0)
	{
		if (check1 * check2 * check3 > 0)
		{
			cout << "Wa-pa-pa-pa-pa-pa-pow!";
		}
		else
		{
			cout << "Woof-meow-tweet-squeek";
		}
	}
	else
	{
		cout << "Woof-meow-tweet-squeek";
	}
}