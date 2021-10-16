dict_cubes = {} # { (0,0) : BLACK, (1,1) : ORANGE}
BLACK = (0,0,0)
GREY = (10,10,10)

dict_cubes[(1,0)] = BLACK
#dict_cubes[(1,0)] = GREY

cube_1 = dict_cubes.get((1,0))
if cube_1 == BLACK:
    dict_cubes[(1,0)] = GREY

print(dict_cubes)
#print(cube_1)