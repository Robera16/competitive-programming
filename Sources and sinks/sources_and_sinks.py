adj_matrix=[]
for i in range(int(input())):
    adj_matrix.append(list(map(int, input().split())))

source, sink = [], []

for i, row in enumerate(adj_matrix):
    if sum(row)==0:
        sink.append(i+1)
    
    col_sum = 0
    for j, row in enumerate(adj_matrix):
       col_sum += adj_matrix[j][i]
    
    if col_sum==0:
        source.append(i+1)
    
print(len(source), *source)
print(len(sink), *sink)