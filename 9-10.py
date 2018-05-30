import copy
s7seg_num = ["1 1 1 1 1 1 0", "0 1 1 0 0 0 0", "1 1 0 1 1 0 1","1 1 1 1 0 0 1","0 1 1 0 0 1 1","1 0 1 1 0 1 1","1 0 1 1 1 1 1","1 1 1 0 0 0 0","1 1 1 1 1 1 1","1 1 1 1 0 1 1"]
print("s7seg_num        s7seg_num_anode")
for i in range(0, len(s7seg_num)):
    s7seg_num_anode = copy.deepcopy(s7seg_num)
    s7seg_num_anode = s7seg_num[i].replace('1','2').replace('0','1').replace('2','0')
    print(s7seg_num[i],"  ",s7seg_num_anode)
    
