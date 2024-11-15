x, y, z = map(int, input().split())
remaining_weight = z - y
max_mangoes = remaining_weight // x 
print(max_mangoes)
