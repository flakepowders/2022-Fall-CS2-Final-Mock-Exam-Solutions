def ribbonseasy(X, L, C):
	n = len(X)
	for i in range(n):
		for j in range(i + 1, n):
			if X[j] - X[i] <= L[i] + L[j] and C[i] != C[j]:
				return [i, j]
	return None
