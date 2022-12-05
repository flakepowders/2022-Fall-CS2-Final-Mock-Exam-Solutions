def cake(P):
	N = len(P)
	res = 0
	for i in range(1, N-1):
		for j in range(1, N-1):
			for k in range(1, N-1):
				if P[i][j][k] == 1:
					if P[i+1][j][k] == 1 and P[i-1][j][k] == 1 and\
					 P[i][j+1][k] == 1 and P[i][j-1][k] == 1 and\
					  P[i][j][k+1] == 1 and P[i][j][k-1] == 1:
						res += 1
	return res
