def gugu_vertical():
    for i in range(2,10):
        for j in range(1,10):
            print(f"{i} x {j} = {i*j}")
        print('-' * 30)

def gugu_horizontal():
    for i in range(1,10):
        for j in range(2,10):
            print(f"{j} x {i} = {j*i}", end='\t')
        print()