def cheat(K):
	N=len(K)
	maxc=max(K)
	mode=[]
	others=[]
	intervals=[[] for _ in range(maxc-1)]
	for i in range(N):
		if K[i]==maxc: mode.append(i)
		elif K[i]==maxc-1:
			for j in intervals: j.append(i)
		else: others = others + [i]*K[i]
	for i in range(len(others)):
		intervals[i%len(intervals)].append(others[i])
	res = mode[:]

	for i in range(len(intervals)):
		for j in intervals[i]: res.append(j)
		for j in mode: res.append(j)
	return res
