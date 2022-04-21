with open("d3.txt") as raw:
    d3_data = raw.read().splitlines()

def d3p1(data):
    bits = len(data[0])
    count = [0] * bits

    for i in range(bits):
        count[i] = sum((n[i] == '1') for n in data)
  
    gamma = ''
    epsilon = ''
    half = len(data) / 2

    for c in count:
        if c > half:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    
    return int(gamma, 2) * int(epsilon, 2)

def d3p2(data):
    
    def separate_common(num_list, i):
        ones = []
        zeros = []
        
        for n in num_list:
            if n[i] == '1':
                ones.append(n)
            else:
                zeros.append(n)
        return ones if len(ones) >= len(zeros) else zeros

    def separate_uncommon(num_list, i):
        ones = []
        zeros = []
        
        for n in num_list:
            if n[i] == '1':
                ones.append(n)
            else:
                zeros.append(n)
        return zeros if len(zeros) <= len(ones) else ones

    bits = len(data[0])
    common = data
    uncommon = data
    
    while len(common) > 1:
        for i in range(bits):
            common = separate_common(common, i)
            if len(common) == 1:
                break
    
    while len(uncommon) > 1:
        for i in range(bits):
            uncommon = separate_uncommon(uncommon, i)
            if len(uncommon) == 1:
                break

    return int(common[0], 2) * int(uncommon[0], 2)

d3p1(d3_data)
d3p2(d3_data)
