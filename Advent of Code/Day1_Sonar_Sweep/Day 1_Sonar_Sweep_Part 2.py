#depth_data = 199, 200, 208, 210, 200, 207, 240, 269, 260, 263
depth_data = open('Day1_Depths_Data.txt').read().split()
depth_data2 = depth_data[1:]
depth_data3 = depth_data[2:]
data_denoise = []
data_denoise_2 = []
greater_depth_denoise = 0

for i in range(len(depth_data[2:])):
    x = int(depth_data[i]) + int(depth_data2[i]) + int(depth_data3[i])
    data_denoise.append(x)

data_denoise_comparison = data_denoise[1:]

for i in range(len(data_denoise[1:])):
    if int(data_denoise[i]) < int(data_denoise_2[i]):
        greater_depth_denoise += 1
print(greater_depth_denoise)


