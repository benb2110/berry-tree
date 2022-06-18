depth_data = open('Day1_Depths_Data.txt').read().split()
#depth_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]  #testing, should == 7
deeper_count = 0

depth_data2 = depth_data[1:]

for i in range(len(depth_data[1:])):
    if int(depth_data[i]) < int(depth_data2[i]):
        deeper_count += 1
print(deeper_count)
