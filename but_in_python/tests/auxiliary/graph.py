#     >(1)<--->(4) ---->(5)
#    /          |       /|
# (0)     ------|------- |
#    \   v      v        v
#     >(2) --> (3) <----(6)

def get_test_matrix_2():
    return [
        [0, 3, 1,  0,  0,  0,  0],
        [0, 0, 0,  0,  1,  0,  0],
        [0, 0, 7,  0,  0,  0,  0],
        [0, 0, 0,  0,  0,  0,  0],
        [0, 1, 0,  5,  0,  2,  0],
        [0, 0, 18, 0,  0,  0,  1],
        [0, 0, 0,  1,  0,  0,  1]
    ]