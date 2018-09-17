board, re, cases, state = [0 for i in range(9)], ' XO', ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)), False
for i in range(9):
  pr = list(map(lambda x: re[x], board))
  [pr.insert(i, '\n') for i in (6, 3)]
  print('|'.join(pr), '\nturn:', re[i % 2 + 1])
  board[int(input('field: ')) - 1] = i % 2 + 1
  for x, y, z in cases:
    if board[x] != 0 and board[x] == board[y] and board[y] == board[z]: state = not print('you won', re[i % 2 + 1])
  if state: break
else: print('tie')
