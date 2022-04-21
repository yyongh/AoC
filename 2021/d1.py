with open("d1test.txt") as raw:
    test_data = [int(i) for i in raw.read().split("\n")]

def d1p1(data):
    x = 0
    for i in range(1,len(data)):
        if data[i] > data[i-1]:
            x += 1
    return x

def d1p2(data):
    x = 0
    for i in range(0,len(data)-3):
        if data[i+3] > data[i]:
            x += 1
    return x

d1p1(d1_data)
d1p2(d1_data)
