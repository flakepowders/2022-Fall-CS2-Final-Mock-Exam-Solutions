def ribbonshard(X, L, C):
	n = len(X)
	INF = 10 ** 20
	r_mx, r_pos = -INF, -1
	b_mx, b_pos = -INF, -1
	y_mx, y_pos = -INF, -1
	for i in range(n):
		x, l, c = X[i], L[i], C[i]
		if c == 'R':
			if r_mx < x + l:
				r_mx = x + l
				r_pos = i
			if b_pos != -1 and b_mx >= x - l:
				return [b_pos, i]
			if y_pos != -1 and y_mx >= x - l:
				return [y_pos, i]
		elif c == 'B':
			if b_mx < x + l:
				b_mx = x + l
				b_pos = i
			if y_pos != -1 and y_mx >= x - l:
				return [y_pos, i]
			if r_pos != -1 and r_mx >= x - l:
				return [r_pos, i]
		else:
			if y_mx < x + l:
				y_mx = x + l
				y_pos = i
			if r_pos != -1 and r_mx >= x - l:
				return [r_pos, i]
			if b_pos != -1 and b_mx >= x - l:
				return [b_pos, i]
	return None
