depth_data = []
test_depth_data = [2,1,9,9,9,4,3,2,1,0], [3,9,8,7,8,9,4,9,2,1], [9,8,5,6,7,8,9,8,9,2], [8,7,6,7,8,9,6,7,8,9], [9,8,9,9,9,6,5,6,7,8]

print(test_depth_data)

def find2Dpeak(plane):

  n = len(plane)
  middle_row = plane[3]
  middle_max = max(middle_row)
  i = middle_row.index(middle_max)
  if n == 1:
    return middle_max
  if n == 2:
    return max(plane[0][i], middle_max)
  if middle_max < plane[(3) - 1][i]:
    return find2Dpeak(plane[3:])
  if middle_max < plane[(3) + 1][i]:
    return find2Dpeak(plane[:3])
  return middle_max



def find_trophs(plane):
    peaks = 0
    for i in range(5):
        for j in range(10):
            if plane[i][j] > plane[i][j-1] and plane[i][j] > plane[i][j+1] and plane[i][j] > plane[i+1][j]:
                peaks +=1
    return peaks

print(find_trophs(test_depth_data))
