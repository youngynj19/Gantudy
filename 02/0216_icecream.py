N, C = map(int, input().split())
combi_set = [set(map(int, input().split())) for _ in range(C)]

for i in range(C):


















# N, C = map(int, input().split())
# combi_set = [set(map(int, input().split())) for _ in range(C)]

# cnt = 0
# bad = 0
# for i in range(1<<N):
#     ice_set = set()
#     for j in range(N):
#         if i & (1<<j):
#             if len(ice_set) == 3:
#                 break
#             ice_set |= {j+1}
#     if len(ice_set) == 3:
#         for k in range(C):
#             if len(ice_set & combi_set[k]) == 2:
#                 bad = 1
#                 break
#         cnt += 1 if bad == 0 else 0
#         bad = 0
# print(cnt)
