# import sys
# input = sys.stdin.readline

# #######################################

# boxes = [list(map(int, input().split())) for _ in range(4)]

# ########################################

# transposed_boxes = [[0] * 4 for _ in range(4)]
# for i in range(4):
#   for j in range(4):
#     transposed_boxes[i][j] = boxes[j][i]


# max_x = 0
# max_y = 0
# for i in range(0,3,2):
#     if max_x < max(transposed_boxes[i]):
#         max_x = max(transposed_boxes[i])
# for i in range(1,4,2):
#     if max_y < max(transposed_boxes[i]):
#         max_y = max(transposed_boxes[i])


# graph = [[0]*(max_y+1) for _ in range(max_x+1)]

# ############################################

# for i in boxes:
#     for x in range(i[0],i[2]):
#         for y in range(i[1],i[3]): 
#             graph[x][y] = 1

# print(sum(map(sum, graph)))

grid = [[0]*101 for _ in range(101)]

for i in range(4):
    a, b, c, d = map(int, input().split())
    for j in range(a, c):
        for k in range(b, d):
            grid[j][k] = 1

print(sum(map(sum, grid)))