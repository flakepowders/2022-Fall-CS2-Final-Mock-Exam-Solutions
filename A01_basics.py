def P1(N):
	return "odd" if N%2 else "even"

def P2(A, B):
	res = 1
	for i in range(A, B+1): res *= i
	return res

def P3(N, M):
	res = [[1] * M for i in range(N)]
	for i in range(1, N):
		for j in range(1, M):
			res[i][j] = res[i-1][j] + res[i][j-1]
	return res

def P4(A, B):
	l1 = []
	l2 = []
	for i in range(len(A)):
		l1.append(A[i])
	for i in range(len(B)):
		l2.append(B[i])
	l1.sort()
	l2.sort()
	return l1 == l2

def next_alphabet(x):
	# parameter x : one lowercase English alphabet, string of length 1
	# return value : next alphabet of x, string of length 1
	return chr(((ord(x) - 96) % 26) + 97)

def P5(S, K):
	res = ''
	for i in range(len(S)):
		next = S[i]
		for j in range(K): next = next_alphabet(next)
		res = res + next
	return res
