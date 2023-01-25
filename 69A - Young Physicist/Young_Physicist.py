n=int(input())
force_vector = [list(map(int,input().split())) for i in range(n)]
x_coordinates,y_coordinates,z_coordinates=0,0,0
for force in force_vector:
    x_coordinates+=force[0]
    y_coordinates+=force[1]
    z_coordinates+=force[2]
    
if x_coordinates==0 and y_coordinates==0 and z_coordinates==0:
    print('YES')
else:
    print('NO')