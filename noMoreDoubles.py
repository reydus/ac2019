series = [266666, 266667, 266668, 266669, 266677]


for i in series:
    i = str(i)
    filtered = []
    length = [0] * len(i)
    skipper = []
    for k in  range(0, len(i)):
        j = 1
        count = 1
        if not k in skipper:
            out = 0
            while k+j <= len(i)-1 and out ==0:
                    if i[k] == i[k+j]:
                        skipper.append(k+j)
                        j += 1
                        count += 1
                    else:
                        out = 1
            if count == 2:
                filtered.append(int(i))

print(filtered)