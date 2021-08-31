import random


def get_all_path():
    s_rank = {0: [0, 1], 1: [2, 3], 2: [4], 3: [5]}
    li = [0, 1, 2, 3]

    paths = []
    for i1 in li:
        for i2 in li[:i1 + 1]:
            for i3 in li[:i1 + 1][:i2 + 1]:
                for i4 in li[:i1 + 1][:i2 + 1][:i3 + 1]:
                    # print(i1,i2,i3,i4)
                    for op1 in s_rank[i1]:
                        for op2 in s_rank[i2]:
                            for op3 in s_rank[i3]:
                                for op4 in s_rank[i4]:
                                    paths.append([op1, op2, op3, op4])
    return paths


def get_all_path_s2():
    s_rank = {0: [0, 1], 1: [2, 3], 2: [4], 3: [5]}
    li = [0, 1, 2, 3]

    paths = []
    for i1 in li:
        start = max(i1 - 1, 0)
        for i2 in li[start:i1 + 1]:
            start = max(i2 - 1, 0)
            for i3 in li[start:i2 + 1]:
                start = max(i3 - 1, 0)
                for i4 in li[start:i3 + 1]:
                    # print(i1,i2,i3,i4)
                    for op1 in s_rank[i1]:
                        for op2 in s_rank[i2]:
                            for op3 in s_rank[i3]:
                                for op4 in s_rank[i4]:
                                    paths.append([op1, op2, op3, op4])
    return paths


def get_all_path_16():
    li = [0, 1, 2, 3]
    for i1 in li:
        for i2 in li[max(i1 - 1, 0):i1 + 1]:
            for i3 in li[max(i2 - 1, 0):i2 + 1]:
                for i4 in li[max(i3 - 1, 0):i3 + 1]:
                    for i5 in li[max(i4 - 1, 0):i4 + 1]:
                        start = max(i5 - 1, 0)
                        for i6 in li[start:i5 + 1]:
                            start = max(i6 - 1, 0)
                            for i7 in li[start:i6 + 1]:
                                start = max(i7 - 1, 0)
                                for i8 in li[start:i7 + 1]:
                                    start = max(i8 - 1, 0)
                                    for i9 in li[start:i8 + 1]:
                                        start = max(i9 - 1, 0)
                                        for i10 in li[start:i9 + 1]:
                                            start = max(i10 - 1, 0)
                                            for i11 in li[start:i10 + 1]:
                                                start = max(i11 - 1, 0)
                                                for i12 in li[start:i11 + 1]:
                                                    start = max(i12 - 1, 0)
                                                    for i13 in li[start:i12 + 1]:
                                                        start = max(i13 - 1, 0)
                                                        for i14 in li[start:i13 + 1]:
                                                            start = max(i14 - 1, 0)
                                                            for i15 in li[start:i14 + 1]:
                                                                start = max(i15 - 1, 0)
                                                                for i16 in li[start:i15 + 1]:
                                                                    yield i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15, i16
                                                                    # num_paths+=1 # print(i1,i2,i3,i4)
                                                                    # num_paths=len(s_rank[i1])

                                                                                    # paths.append([op1, op2, op3, op4])
    # assert num_paths == len(paths)
    # return num_paths

def gap():
    s_rank = {0: [0, 1], 1: [2, 3], 2: [4], 3: [5]}

    paths = []
    num_paths = 0
    for (i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15, i16) in get_all_path_16():
        for op1 in s_rank[i1]:
            for op2 in s_rank[i2]:
                for op3 in s_rank[i3]:
                    for op4 in s_rank[i4]:
                        for op5 in s_rank[i5]:
                            for op6 in s_rank[i6]:
                                for op7 in s_rank[i7]:
                                    for op8 in s_rank[i8]:
                                        for op9 in s_rank[i9]:
                                            for op10 in s_rank[i10]:
                                                for op11 in s_rank[i11]:
                                                    for op12 in s_rank[i12]:
                                                        for op13 in s_rank[i13]:
                                                            for op14 in s_rank[i14]:
                                                                for op15 in s_rank[i15]:
                                                                    for op16 in s_rank[i16]:
                                                                        paths.append([op1, op2, op3, op4, op5, op6, op7, op8, op9, op10, op11, op12, op13, op14, op15, op16])
                                                                        num_paths += 1
    return num_paths, random.choice(paths)

# 201 129 80 16

all_path_ = {
    4:[[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1], [2, 0, 0, 0], [2, 0, 0, 1], [2, 0, 1, 0], [2, 0, 1, 1], [2, 1, 0, 0], [2, 1, 0, 1], [2, 1, 1, 0], [2, 1, 1, 1], [3, 0, 0, 0], [3, 0, 0, 1], [3, 0, 1, 0], [3, 0, 1, 1], [3, 1, 0, 0], [3, 1, 0, 1], [3, 1, 1, 0], [3, 1, 1, 1], [2, 2, 0, 0], [2, 2, 0, 1], [2, 2, 1, 0], [2, 2, 1, 1], [2, 3, 0, 0], [2, 3, 0, 1], [2, 3, 1, 0], [2, 3, 1, 1], [3, 2, 0, 0], [3, 2, 0, 1], [3, 2, 1, 0], [3, 2, 1, 1], [3, 3, 0, 0], [3, 3, 0, 1], [3, 3, 1, 0], [3, 3, 1, 1], [2, 2, 2, 0], [2, 2, 2, 1], [2, 2, 3, 0], [2, 2, 3, 1], [2, 3, 2, 0], [2, 3, 2, 1], [2, 3, 3, 0], [2, 3, 3, 1], [3, 2, 2, 0], [3, 2, 2, 1], [3, 2, 3, 0], [3, 2, 3, 1], [3, 3, 2, 0], [3, 3, 2, 1], [3, 3, 3, 0], [3, 3, 3, 1], [2, 2, 2, 2], [2, 2, 2, 3], [2, 2, 3, 2], [2, 2, 3, 3], [2, 3, 2, 2], [2, 3, 2, 3], [2, 3, 3, 2], [2, 3, 3, 3], [3, 2, 2, 2], [3, 2, 2, 3], [3, 2, 3, 2], [3, 2, 3, 3], [3, 3, 2, 2], [3, 3, 2, 3], [3, 3, 3, 2], [3, 3, 3, 3], [4, 0, 0, 0], [4, 0, 0, 1], [4, 0, 1, 0], [4, 0, 1, 1], [4, 1, 0, 0], [4, 1, 0, 1], [4, 1, 1, 0], [4, 1, 1, 1], [4, 2, 0, 0], [4, 2, 0, 1], [4, 2, 1, 0], [4, 2, 1, 1], [4, 3, 0, 0], [4, 3, 0, 1], [4, 3, 1, 0], [4, 3, 1, 1], [4, 2, 2, 0], [4, 2, 2, 1], [4, 2, 3, 0], [4, 2, 3, 1], [4, 3, 2, 0], [4, 3, 2, 1], [4, 3, 3, 0], [4, 3, 3, 1], [4, 2, 2, 2], [4, 2, 2, 3], [4, 2, 3, 2], [4, 2, 3, 3], [4, 3, 2, 2], [4, 3, 2, 3], [4, 3, 3, 2], [4, 3, 3, 3], [4, 4, 0, 0], [4, 4, 0, 1], [4, 4, 1, 0], [4, 4, 1, 1], [4, 4, 2, 0], [4, 4, 2, 1], [4, 4, 3, 0], [4, 4, 3, 1], [4, 4, 2, 2], [4, 4, 2, 3], [4, 4, 3, 2], [4, 4, 3, 3], [4, 4, 4, 0], [4, 4, 4, 1], [4, 4, 4, 2], [4, 4, 4, 3], [4, 4, 4, 4], [5, 0, 0, 0], [5, 0, 0, 1], [5, 0, 1, 0], [5, 0, 1, 1], [5, 1, 0, 0], [5, 1, 0, 1], [5, 1, 1, 0], [5, 1, 1, 1], [5, 2, 0, 0], [5, 2, 0, 1], [5, 2, 1, 0], [5, 2, 1, 1], [5, 3, 0, 0], [5, 3, 0, 1], [5, 3, 1, 0], [5, 3, 1, 1], [5, 2, 2, 0], [5, 2, 2, 1], [5, 2, 3, 0], [5, 2, 3, 1], [5, 3, 2, 0], [5, 3, 2, 1], [5, 3, 3, 0], [5, 3, 3, 1], [5, 2, 2, 2], [5, 2, 2, 3], [5, 2, 3, 2], [5, 2, 3, 3], [5, 3, 2, 2], [5, 3, 2, 3], [5, 3, 3, 2], [5, 3, 3, 3], [5, 4, 0, 0], [5, 4, 0, 1], [5, 4, 1, 0], [5, 4, 1, 1], [5, 4, 2, 0], [5, 4, 2, 1], [5, 4, 3, 0], [5, 4, 3, 1], [5, 4, 2, 2], [5, 4, 2, 3], [5, 4, 3, 2], [5, 4, 3, 3], [5, 4, 4, 0], [5, 4, 4, 1], [5, 4, 4, 2], [5, 4, 4, 3], [5, 4, 4, 4], [5, 5, 0, 0], [5, 5, 0, 1], [5, 5, 1, 0], [5, 5, 1, 1], [5, 5, 2, 0], [5, 5, 2, 1], [5, 5, 3, 0], [5, 5, 3, 1], [5, 5, 2, 2], [5, 5, 2, 3], [5, 5, 3, 2], [5, 5, 3, 3], [5, 5, 4, 0], [5, 5, 4, 1], [5, 5, 4, 2], [5, 5, 4, 3], [5, 5, 4, 4], [5, 5, 5, 0], [5, 5, 5, 1], [5, 5, 5, 2], [5, 5, 5, 3], [5, 5, 5, 4], [5, 5, 5, 5]],
    3:[[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1], [2, 0, 0, 0], [2, 0, 0, 1], [2, 0, 1, 0], [2, 0, 1, 1], [2, 1, 0, 0], [2, 1, 0, 1], [2, 1, 1, 0], [2, 1, 1, 1], [3, 0, 0, 0], [3, 0, 0, 1], [3, 0, 1, 0], [3, 0, 1, 1], [3, 1, 0, 0], [3, 1, 0, 1], [3, 1, 1, 0], [3, 1, 1, 1], [2, 2, 0, 0], [2, 2, 0, 1], [2, 2, 1, 0], [2, 2, 1, 1], [2, 3, 0, 0], [2, 3, 0, 1], [2, 3, 1, 0], [2, 3, 1, 1], [3, 2, 0, 0], [3, 2, 0, 1], [3, 2, 1, 0], [3, 2, 1, 1], [3, 3, 0, 0], [3, 3, 0, 1], [3, 3, 1, 0], [3, 3, 1, 1], [2, 2, 2, 0], [2, 2, 2, 1], [2, 2, 3, 0], [2, 2, 3, 1], [2, 3, 2, 0], [2, 3, 2, 1], [2, 3, 3, 0], [2, 3, 3, 1], [3, 2, 2, 0], [3, 2, 2, 1], [3, 2, 3, 0], [3, 2, 3, 1], [3, 3, 2, 0], [3, 3, 2, 1], [3, 3, 3, 0], [3, 3, 3, 1], [2, 2, 2, 2], [2, 2, 2, 3], [2, 2, 3, 2], [2, 2, 3, 3], [2, 3, 2, 2], [2, 3, 2, 3], [2, 3, 3, 2], [2, 3, 3, 3], [3, 2, 2, 2], [3, 2, 2, 3], [3, 2, 3, 2], [3, 2, 3, 3], [3, 3, 2, 2], [3, 3, 2, 3], [3, 3, 3, 2], [3, 3, 3, 3], [4, 0, 0, 0], [4, 0, 0, 1], [4, 0, 1, 0], [4, 0, 1, 1], [4, 1, 0, 0], [4, 1, 0, 1], [4, 1, 1, 0], [4, 1, 1, 1], [4, 2, 0, 0], [4, 2, 0, 1], [4, 2, 1, 0], [4, 2, 1, 1], [4, 3, 0, 0], [4, 3, 0, 1], [4, 3, 1, 0], [4, 3, 1, 1], [4, 2, 2, 0], [4, 2, 2, 1], [4, 2, 3, 0], [4, 2, 3, 1], [4, 3, 2, 0], [4, 3, 2, 1], [4, 3, 3, 0], [4, 3, 3, 1], [4, 2, 2, 2], [4, 2, 2, 3], [4, 2, 3, 2], [4, 2, 3, 3], [4, 3, 2, 2], [4, 3, 2, 3], [4, 3, 3, 2], [4, 3, 3, 3], [4, 4, 0, 0], [4, 4, 0, 1], [4, 4, 1, 0], [4, 4, 1, 1], [4, 4, 2, 0], [4, 4, 2, 1], [4, 4, 3, 0], [4, 4, 3, 1], [4, 4, 2, 2], [4, 4, 2, 3], [4, 4, 3, 2], [4, 4, 3, 3], [4, 4, 4, 0], [4, 4, 4, 1], [4, 4, 4, 2], [4, 4, 4, 3], [4, 4, 4, 4]],
    2:[[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1], [2, 0, 0, 0], [2, 0, 0, 1], [2, 0, 1, 0], [2, 0, 1, 1], [2, 1, 0, 0], [2, 1, 0, 1], [2, 1, 1, 0], [2, 1, 1, 1], [3, 0, 0, 0], [3, 0, 0, 1], [3, 0, 1, 0], [3, 0, 1, 1], [3, 1, 0, 0], [3, 1, 0, 1], [3, 1, 1, 0], [3, 1, 1, 1], [2, 2, 0, 0], [2, 2, 0, 1], [2, 2, 1, 0], [2, 2, 1, 1], [2, 3, 0, 0], [2, 3, 0, 1], [2, 3, 1, 0], [2, 3, 1, 1], [3, 2, 0, 0], [3, 2, 0, 1], [3, 2, 1, 0], [3, 2, 1, 1], [3, 3, 0, 0], [3, 3, 0, 1], [3, 3, 1, 0], [3, 3, 1, 1], [2, 2, 2, 0], [2, 2, 2, 1], [2, 2, 3, 0], [2, 2, 3, 1], [2, 3, 2, 0], [2, 3, 2, 1], [2, 3, 3, 0], [2, 3, 3, 1], [3, 2, 2, 0], [3, 2, 2, 1], [3, 2, 3, 0], [3, 2, 3, 1], [3, 3, 2, 0], [3, 3, 2, 1], [3, 3, 3, 0], [3, 3, 3, 1], [2, 2, 2, 2], [2, 2, 2, 3], [2, 2, 3, 2], [2, 2, 3, 3], [2, 3, 2, 2], [2, 3, 2, 3], [2, 3, 3, 2], [2, 3, 3, 3], [3, 2, 2, 2], [3, 2, 2, 3], [3, 2, 3, 2], [3, 2, 3, 3], [3, 3, 2, 2], [3, 3, 2, 3], [3, 3, 3, 2], [3, 3, 3, 3]],
    1:[[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]]
}

all_path = {
    4:[[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1], [2, 0, 0, 0], [2, 0, 0, 1], [2, 0, 1, 0], [2, 0, 1, 1], [2, 1, 0, 0], [2, 1, 0, 1], [2, 1, 1, 0], [2, 1, 1, 1], [3, 0, 0, 0], [3, 0, 0, 1], [3, 0, 1, 0], [3, 0, 1, 1], [3, 1, 0, 0], [3, 1, 0, 1], [3, 1, 1, 0], [3, 1, 1, 1], [2, 2, 0, 0], [2, 2, 0, 1], [2, 2, 1, 0], [2, 2, 1, 1], [2, 3, 0, 0], [2, 3, 0, 1], [2, 3, 1, 0], [2, 3, 1, 1], [3, 2, 0, 0], [3, 2, 0, 1], [3, 2, 1, 0], [3, 2, 1, 1], [3, 3, 0, 0], [3, 3, 0, 1], [3, 3, 1, 0], [3, 3, 1, 1], [2, 2, 2, 0], [2, 2, 2, 1], [2, 2, 3, 0], [2, 2, 3, 1], [2, 3, 2, 0], [2, 3, 2, 1], [2, 3, 3, 0], [2, 3, 3, 1], [3, 2, 2, 0], [3, 2, 2, 1], [3, 2, 3, 0], [3, 2, 3, 1], [3, 3, 2, 0], [3, 3, 2, 1], [3, 3, 3, 0], [3, 3, 3, 1], [2, 2, 2, 2], [2, 2, 2, 3], [2, 2, 3, 2], [2, 2, 3, 3], [2, 3, 2, 2], [2, 3, 2, 3], [2, 3, 3, 2], [2, 3, 3, 3], [3, 2, 2, 2], [3, 2, 2, 3], [3, 2, 3, 2], [3, 2, 3, 3], [3, 3, 2, 2], [3, 3, 2, 3], [3, 3, 3, 2], [3, 3, 3, 3], [4, 2, 0, 0], [4, 2, 0, 1], [4, 2, 1, 0], [4, 2, 1, 1], [4, 3, 0, 0], [4, 3, 0, 1], [4, 3, 1, 0], [4, 3, 1, 1], [4, 2, 2, 0], [4, 2, 2, 1], [4, 2, 3, 0], [4, 2, 3, 1], [4, 3, 2, 0], [4, 3, 2, 1], [4, 3, 3, 0], [4, 3, 3, 1], [4, 2, 2, 2], [4, 2, 2, 3], [4, 2, 3, 2], [4, 2, 3, 3], [4, 3, 2, 2], [4, 3, 2, 3], [4, 3, 3, 2], [4, 3, 3, 3], [4, 4, 2, 0], [4, 4, 2, 1], [4, 4, 3, 0], [4, 4, 3, 1], [4, 4, 2, 2], [4, 4, 2, 3], [4, 4, 3, 2], [4, 4, 3, 3], [4, 4, 4, 2], [4, 4, 4, 3], [4, 4, 4, 4], [5, 4, 2, 0], [5, 4, 2, 1], [5, 4, 3, 0], [5, 4, 3, 1], [5, 4, 2, 2], [5, 4, 2, 3], [5, 4, 3, 2], [5, 4, 3, 3], [5, 4, 4, 2], [5, 4, 4, 3], [5, 4, 4, 4], [5, 5, 4, 2], [5, 5, 4, 3], [5, 5, 4, 4], [5, 5, 5, 4], [5, 5, 5, 5]],
    3:[[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1], [2, 0, 0, 0], [2, 0, 0, 1], [2, 0, 1, 0], [2, 0, 1, 1], [2, 1, 0, 0], [2, 1, 0, 1], [2, 1, 1, 0], [2, 1, 1, 1], [3, 0, 0, 0], [3, 0, 0, 1], [3, 0, 1, 0], [3, 0, 1, 1], [3, 1, 0, 0], [3, 1, 0, 1], [3, 1, 1, 0], [3, 1, 1, 1], [2, 2, 0, 0], [2, 2, 0, 1], [2, 2, 1, 0], [2, 2, 1, 1], [2, 3, 0, 0], [2, 3, 0, 1], [2, 3, 1, 0], [2, 3, 1, 1], [3, 2, 0, 0], [3, 2, 0, 1], [3, 2, 1, 0], [3, 2, 1, 1], [3, 3, 0, 0], [3, 3, 0, 1], [3, 3, 1, 0], [3, 3, 1, 1], [2, 2, 2, 0], [2, 2, 2, 1], [2, 2, 3, 0], [2, 2, 3, 1], [2, 3, 2, 0], [2, 3, 2, 1], [2, 3, 3, 0], [2, 3, 3, 1], [3, 2, 2, 0], [3, 2, 2, 1], [3, 2, 3, 0], [3, 2, 3, 1], [3, 3, 2, 0], [3, 3, 2, 1], [3, 3, 3, 0], [3, 3, 3, 1], [2, 2, 2, 2], [2, 2, 2, 3], [2, 2, 3, 2], [2, 2, 3, 3], [2, 3, 2, 2], [2, 3, 2, 3], [2, 3, 3, 2], [2, 3, 3, 3], [3, 2, 2, 2], [3, 2, 2, 3], [3, 2, 3, 2], [3, 2, 3, 3], [3, 3, 2, 2], [3, 3, 2, 3], [3, 3, 3, 2], [3, 3, 3, 3], [4, 2, 0, 0], [4, 2, 0, 1], [4, 2, 1, 0], [4, 2, 1, 1], [4, 3, 0, 0], [4, 3, 0, 1], [4, 3, 1, 0], [4, 3, 1, 1], [4, 2, 2, 0], [4, 2, 2, 1], [4, 2, 3, 0], [4, 2, 3, 1], [4, 3, 2, 0], [4, 3, 2, 1], [4, 3, 3, 0], [4, 3, 3, 1], [4, 2, 2, 2], [4, 2, 2, 3], [4, 2, 3, 2], [4, 2, 3, 3], [4, 3, 2, 2], [4, 3, 2, 3], [4, 3, 3, 2], [4, 3, 3, 3], [4, 4, 2, 0], [4, 4, 2, 1], [4, 4, 3, 0], [4, 4, 3, 1], [4, 4, 2, 2], [4, 4, 2, 3], [4, 4, 3, 2], [4, 4, 3, 3], [4, 4, 4, 2], [4, 4, 4, 3], [4, 4, 4, 4]],
    2:[[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1], [2, 0, 0, 0], [2, 0, 0, 1], [2, 0, 1, 0], [2, 0, 1, 1], [2, 1, 0, 0], [2, 1, 0, 1], [2, 1, 1, 0], [2, 1, 1, 1], [3, 0, 0, 0], [3, 0, 0, 1], [3, 0, 1, 0], [3, 0, 1, 1], [3, 1, 0, 0], [3, 1, 0, 1], [3, 1, 1, 0], [3, 1, 1, 1], [2, 2, 0, 0], [2, 2, 0, 1], [2, 2, 1, 0], [2, 2, 1, 1], [2, 3, 0, 0], [2, 3, 0, 1], [2, 3, 1, 0], [2, 3, 1, 1], [3, 2, 0, 0], [3, 2, 0, 1], [3, 2, 1, 0], [3, 2, 1, 1], [3, 3, 0, 0], [3, 3, 0, 1], [3, 3, 1, 0], [3, 3, 1, 1], [2, 2, 2, 0], [2, 2, 2, 1], [2, 2, 3, 0], [2, 2, 3, 1], [2, 3, 2, 0], [2, 3, 2, 1], [2, 3, 3, 0], [2, 3, 3, 1], [3, 2, 2, 0], [3, 2, 2, 1], [3, 2, 3, 0], [3, 2, 3, 1], [3, 3, 2, 0], [3, 3, 2, 1], [3, 3, 3, 0], [3, 3, 3, 1], [2, 2, 2, 2], [2, 2, 2, 3], [2, 2, 3, 2], [2, 2, 3, 3], [2, 3, 2, 2], [2, 3, 2, 3], [2, 3, 3, 2], [2, 3, 3, 3], [3, 2, 2, 2], [3, 2, 2, 3], [3, 2, 3, 2], [3, 2, 3, 3], [3, 3, 2, 2], [3, 3, 2, 3], [3, 3, 3, 2], [3, 3, 3, 3]],
    1:[[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]]
}

restricted_path = {
    4:[[4, 2, 0, 0], [4, 2, 0, 1], [4, 2, 1, 0], [4, 2, 1, 1], [4, 3, 0, 0], [4, 3, 0, 1], [4, 3, 1, 0], [4, 3, 1, 1], [4, 2, 2, 0], [4, 2, 2, 1], [4, 2, 3, 0], [4, 2, 3, 1], [4, 3, 2, 0], [4, 3, 2, 1], [4, 3, 3, 0], [4, 3, 3, 1], [4, 2, 2, 2], [4, 2, 2, 3], [4, 2, 3, 2], [4, 2, 3, 3], [4, 3, 2, 2], [4, 3, 2, 3], [4, 3, 3, 2], [4, 3, 3, 3], [4, 4, 2, 0], [4, 4, 2, 1], [4, 4, 3, 0], [4, 4, 3, 1], [4, 4, 2, 2], [4, 4, 2, 3], [4, 4, 3, 2], [4, 4, 3, 3], [4, 4, 4, 2], [4, 4, 4, 3], [4, 4, 4, 4], [5, 4, 2, 0], [5, 4, 2, 1], [5, 4, 3, 0], [5, 4, 3, 1], [5, 4, 2, 2], [5, 4, 2, 3], [5, 4, 3, 2], [5, 4, 3, 3], [5, 4, 4, 2], [5, 4, 4, 3], [5, 4, 4, 4], [5, 5, 4, 2], [5, 5, 4, 3], [5, 5, 4, 4], [5, 5, 5, 4], [5, 5, 5, 5]],
    3:[[2, 0, 0, 0], [2, 0, 0, 1], [2, 0, 1, 0], [2, 0, 1, 1], [2, 1, 0, 0], [2, 1, 0, 1], [2, 1, 1, 0], [2, 1, 1, 1], [3, 0, 0, 0], [3, 0, 0, 1], [3, 0, 1, 0], [3, 0, 1, 1], [3, 1, 0, 0], [3, 1, 0, 1], [3, 1, 1, 0], [3, 1, 1, 1], [2, 2, 0, 0], [2, 2, 0, 1], [2, 2, 1, 0], [2, 2, 1, 1], [2, 3, 0, 0], [2, 3, 0, 1], [2, 3, 1, 0], [2, 3, 1, 1], [3, 2, 0, 0], [3, 2, 0, 1], [3, 2, 1, 0], [3, 2, 1, 1], [3, 3, 0, 0], [3, 3, 0, 1], [3, 3, 1, 0], [3, 3, 1, 1], [2, 2, 2, 0], [2, 2, 2, 1], [2, 2, 3, 0], [2, 2, 3, 1], [2, 3, 2, 0], [2, 3, 2, 1], [2, 3, 3, 0], [2, 3, 3, 1], [3, 2, 2, 0], [3, 2, 2, 1], [3, 2, 3, 0], [3, 2, 3, 1], [3, 3, 2, 0], [3, 3, 2, 1], [3, 3, 3, 0], [3, 3, 3, 1], [2, 2, 2, 2], [2, 2, 2, 3], [2, 2, 3, 2], [2, 2, 3, 3], [2, 3, 2, 2], [2, 3, 2, 3], [2, 3, 3, 2], [2, 3, 3, 3], [3, 2, 2, 2], [3, 2, 2, 3], [3, 2, 3, 2], [3, 2, 3, 3], [3, 3, 2, 2], [3, 3, 2, 3], [3, 3, 3, 2], [3, 3, 3, 3], [4, 2, 0, 0], [4, 2, 0, 1], [4, 2, 1, 0], [4, 2, 1, 1], [4, 3, 0, 0], [4, 3, 0, 1], [4, 3, 1, 0], [4, 3, 1, 1], [4, 2, 2, 0], [4, 2, 2, 1], [4, 2, 3, 0], [4, 2, 3, 1], [4, 3, 2, 0], [4, 3, 2, 1], [4, 3, 3, 0], [4, 3, 3, 1], [4, 2, 2, 2], [4, 2, 2, 3], [4, 2, 3, 2], [4, 2, 3, 3], [4, 3, 2, 2], [4, 3, 2, 3], [4, 3, 3, 2], [4, 3, 3, 3], [4, 4, 2, 0], [4, 4, 2, 1], [4, 4, 3, 0], [4, 4, 3, 1], [4, 4, 2, 2], [4, 4, 2, 3], [4, 4, 3, 2], [4, 4, 3, 3], [4, 4, 4, 2], [4, 4, 4, 3], [4, 4, 4, 4]],
    2:[[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1], [2, 0, 0, 0], [2, 0, 0, 1], [2, 0, 1, 0], [2, 0, 1, 1], [2, 1, 0, 0], [2, 1, 0, 1], [2, 1, 1, 0], [2, 1, 1, 1], [3, 0, 0, 0], [3, 0, 0, 1], [3, 0, 1, 0], [3, 0, 1, 1], [3, 1, 0, 0], [3, 1, 0, 1], [3, 1, 1, 0], [3, 1, 1, 1], [2, 2, 0, 0], [2, 2, 0, 1], [2, 2, 1, 0], [2, 2, 1, 1], [2, 3, 0, 0], [2, 3, 0, 1], [2, 3, 1, 0], [2, 3, 1, 1], [3, 2, 0, 0], [3, 2, 0, 1], [3, 2, 1, 0], [3, 2, 1, 1], [3, 3, 0, 0], [3, 3, 0, 1], [3, 3, 1, 0], [3, 3, 1, 1], [2, 2, 2, 0], [2, 2, 2, 1], [2, 2, 3, 0], [2, 2, 3, 1], [2, 3, 2, 0], [2, 3, 2, 1], [2, 3, 3, 0], [2, 3, 3, 1], [3, 2, 2, 0], [3, 2, 2, 1], [3, 2, 3, 0], [3, 2, 3, 1], [3, 3, 2, 0], [3, 3, 2, 1], [3, 3, 3, 0], [3, 3, 3, 1], [2, 2, 2, 2], [2, 2, 2, 3], [2, 2, 3, 2], [2, 2, 3, 3], [2, 3, 2, 2], [2, 3, 2, 3], [2, 3, 3, 2], [2, 3, 3, 3], [3, 2, 2, 2], [3, 2, 2, 3], [3, 2, 3, 2], [3, 2, 3, 3], [3, 3, 2, 2], [3, 3, 2, 3], [3, 3, 3, 2], [3, 3, 3, 3]],
    1:[[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]]
}

if __name__ == '__main__':
    print(gap())
