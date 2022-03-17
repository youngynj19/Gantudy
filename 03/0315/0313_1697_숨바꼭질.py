def bfs():
	global cnt
	# print(order[cnt], queue)
	v = queue.pop(0)
	visited.append(v)
	if v == K:
		print(order[cnt])
		return
	else:
		if v+1 not in visited:
			queue.append(v+1)
			order.append(order[cnt]+1)
		if v-1 not in visited:
			queue.append(v-1)
			order.append(order[cnt]+1)
		if 2*v not in visited:
			queue.append(2*v)
			order.append(order[cnt]+1)
		cnt += 1
		bfs()
	return


N, K = map(int, input().split())

queue = [N]
order = [0]
# [0, 1, 1, 1, 2, 2, 2, 2, 2, 2]
cnt = 0
visited = []
bfs()