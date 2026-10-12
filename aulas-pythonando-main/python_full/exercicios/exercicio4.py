row_start = int(input())
colunm_start = int(input())
row_exit = int(input())
colunm_exit = int(input())
number_row = int(input())
number_colunns = int(input())

matrix = []
for c in range(number_colunns):
    row = []
    for r in range(number_row):
        num = int(input(f"coluna {c} linha {r}: "))
        row.append(num)
    matrix.append(row)

for c in range(len(matrix)):
    print(matrix[c])
start = matrix[colunm_start][row_start]
current_position = start
exit = matrix[colunm_exit][row_exit]
last_postition = current_position

while start != 0:
    
    