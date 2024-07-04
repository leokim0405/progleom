#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<long long> answer;

long long binary(vector<long long>& a, long long len, long x)
{
	long long low = 0, high = len - 1;

	while (low <= high)
	{
		long long mid = (low + high) / 2;

		if (a[mid] == x)
		{
			return mid;
		}
		else if (a[mid] > x)
		{
			high = mid - 1;
			continue;
		}
		else if (a[mid] < x)
		{
			low = mid + 1;
			continue;
		}
	}
	return -1;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	while (true)
	{
		long long n1, n2;
		vector<long long> a1;
		vector<long long> a2;

		cin >> n1;
		if (n1 == 0)
		{
			break;
		}

		for (long long i = 0; i < n1; i++)
		{
			long long temp;
			cin >> temp;
			a1.push_back(temp);
		}

		cin >> n2;

		for (long long j = 0; j < n2; j++)
		{
			long long temp;
			cin >> temp;
			a2.push_back(temp);
		}

		long long result = 0;
		long long startA = 0, startB = 0;

		for (long long k = 0; k < n1; k++)
		{
			long long cross = binary(a2, n2, a1[k]);	// 교점 구하기 (b의 교점 좌표)
			long long sumA = 0, sumB = 0;

			if (cross == -1)		// 겹치지 않음
			{
				/*
				if (k == n1 -1)		//끝 블록
				{
					for (long long n = startA; n < n1; n++)
					{
						sumA += a1[n];
					}
					for (long long o = startB; o < n2; o++)
					{
						sumB += a2[o];
					}
					result += max(sumA, sumB);
				}*/
				continue;	
			}
			else					// 교점 있음
			{
				for (long long l = startA; l < k; l++)
				{
					sumA += a1[l];
				}
				startA = k + 1;

				for (long long m = startB; m < cross; m++)
				{
					sumB += a2[m];
				}
				startB = cross + 1;

				result += max(sumA, sumB) + a1[k];
			}
		}
		/*
		if (isCross && startB < n2)
		{
			long long temp = 0;
			for (long long g = startB ; g < n2; g++)
			{
				temp += a2[g];
			}
			result = max(result, temp + result);
		}*/

		long long tempA = 0, tempB = 0;
		for (long long q = startA; q < n1; q++)
		{
			tempA += a1[q];
		}
		for (long long w = startB; w < n2; w++)
		{
			tempB += a2[w];
		}

		result = max(result, max(tempA, tempB) + result);

		answer.push_back(result);

	}


	for (long long an : answer)
	{
		cout << an << "\n";
	}

	return 0;
}

