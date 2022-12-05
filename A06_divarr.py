def divarr(N, K):
	minlen = K[0][1]-K[0][0]+1
	for i in range(len(K)):
		minlen = min(minlen, K[i][1]-K[i][0]+1)
	res = []
	for i in range(N):
		res.append(i % minlen + 1)
	return res
