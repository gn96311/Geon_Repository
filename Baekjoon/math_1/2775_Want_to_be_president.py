import sys

def next_floor(down_floor):
    up_floor = []
    people_count = 0
    for i in range(len(down_floor)):
        people_count += down_floor[i]
        up_floor.append(people_count)
    return up_floor

for i in range(int(sys.stdin.readline())):
    k = sys.stdin.readline()
    n = sys.stdin.readline()
    first_floor = []

    for j in range(int(n)):
        first_floor.append(j+1)

    for floor in range(int(k)):
        up_floor = next_floor(first_floor)
        first_floor = up_floor
    
    print(first_floor[-1])