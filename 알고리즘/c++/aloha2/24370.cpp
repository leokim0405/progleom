#include <iostream>
#include <cmath>

using namespace std;

float d1(int a, int b, int c)
{
	return (-b + sqrt(b * b - 4 * a * c)) / 2 * a;
}

float d2(int a, int b, int c)
{
	return (-b - sqrt(b * b - 4 * a * c)) / 2 * a;
}

float d(int a2, int a1, int a0, int c)
{
	if (a2 - c > 0)
	{
		if( (a1 * a1 - 4 * (a2-c) * c ) < 0)
		{
			return 0;
		}
		else
		{
			return 1;
		}
	}
	else
	{
		if ( ( a1 * a1 - 4 * (c - a2) * (-a0) ) < 0 )
		{
			return 0;
		}
		else
		{
			return 1;
		}
	}
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int a2, a1, a0, c1,c2, n0;
	cin >> a2 >> a1 >> a0;			//a2 n^2 + a1 n + a0
	cin >> c1 >> c2;				// c1*n^2  c2*n^2
	cin >> n0;

	if (c1 == c2)
	{
		if (a2 == c1 && a1 == 0 && a0 == 0)
		{
			cout << 1;
		}
		cout << 0;
	}
	else if ( !(c1 <= a2 && a2 <= c2) )
	{
		cout << 0;
	}
	else				// c1 <= a2 <= c2
	{
		if (d(a2, a1, a0, c2))		// �� �� ����
		{
			int crossUp = d1(a2 - c2, a1, a0);

			if (n0 >= crossUp)
			{
				if (d(a2, a1, a0, c1))		// �Ʒ��� ����
				{
					int crossDown = d1(a2 - c1, a1, a0);

					if (n0 > crossDown)
					{
						cout << 1;
					}
					else
					{
						cout << 0;
					}
				}
				else						// �Ʒ��� ����x
				{
					cout << 1;
				}
			}
			else
			{
				cout << 0;
			}
		}
		else						// ���� ���� x
		{
			if (d(a2, a1, a0, c1))	// �Ʒ��� ����
			{
				if (n0 > d1(a2 - c1, a1, a0))
				{
					cout << 1;
				}
				else
				{
					cout << 0;
				}
			}
			else						//�Ʒ��� ���� x
			{
				cout << 0;
			}
		}
		
	}

	/*
	int func = (a2 * n0 * n0 + a1 * n0 + a0);

	if (!(c1 <= a2 && c2 >= a2))
	{
		cout << 0;
	}
	else if ( !(( c1 * n0 * n0 <= func) && (func <= c2 * n0 * n0)) )
	{
		cout << 0;
	}
	else
	{
		int a3, a4, b, c;
		a3 = a2 - c1;		// a3 �� ��
		a4 = a2 - c2;		// a4 �� ��
		b = a1;
		c = a0;

		if (b*b - 4 * a4 * c < 0)		//�� �Լ��� ������ ����
		{
			if (b*b - 4 * a3 * c < 0)	// �Ʒ� �Լ��� ���� ����
			{
				cout << 0;
			}
			else						// �Ʒ� �Լ� ���� ����
			{
				float crossDown1 = d1(a3, b, c);

				if (crossDown1 < n0)
				{
					cout << 1;
				}
				else
				{
					cout << 0;
				}
			}
		}
		else							// �� �Լ��� ���� ����
		{
			float crossUp1 = d1(a4, b, c);

			if (b * b - 4 * a3 * c < 0)	// �Ʒ� �Լ��� ���� ����
			{
				if (crossUp1 < n0)
				{
					cout << 1;
				}
				else
				{
					cout << 0;
				}
			}
			else						// �Ʒ� �Լ� ���� ����
			{
				
				float crossDown1 = d1(a3, b, c);
				
				if (crossDown1 < n0)
				{
					cout << 1;
				}
				else
				{
					cout << 0;
				}
			}			
		}
	}*/

	return 0;
}