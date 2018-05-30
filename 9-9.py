data = [[21, 7, 43, 65], [2, 8, 72, 52]]

while True:
    num = int(input("찾을 값 : "))
    if(num in data[0] or num in data[1]):
        if(num in data[0]):
            r = 1
        else:
            r = 2
        c = data[r-1].index(num)
        print("위치 : %d행 %d열"%(r, c+1))
        continue
    else:
        print("찾지 못함")
        break
