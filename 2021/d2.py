with open("d2.txt") as raw:
    d2_data = raw.read().splitlines()

def d2p1(data):
    horiz = 0
    depth = 0
    
    for i in range(0,len(data)):
        command, n = data[i].split()
        if command == "down":
            depth += int(n)
        elif command == "up":
            depth -= int(n)
        else:
            horiz += int(n)
    
    return horiz * depth

def d2p2(data):
    horiz = 0
    depth = 0
    aim = 0
    
    for i in range(0,len(data)):
        command, n = data[i].split()
        if command == "down":
            aim += int(n)
        elif command == "up":
            aim -= int(n)
        else:
            horiz += int(n)
            depth += aim * int(n)
    
    return horiz * depth

d2p1(d2_data)
d2p2(d2_data)
