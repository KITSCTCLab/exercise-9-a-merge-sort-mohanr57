from typing import List

def merge_sort(data) -> None:
  # Write code here
  if len(data) >1:
    mid = (len(data))//2
    data_left = data[:mid]
    data_right = data[mid:]
    merge_sort(data_left)
    merge_sort(data_right)
  
    l = 0 # This one is for left data
    r = 0 # This one is for right data
    m = 0 # The value m is for the main data

    while l<len(data_left) and r<len(data_right):
      if data_left[l] <= data_right[r]:
        data[m] = data_left[l]
        l+=1
      else:
        data[m] = data_right[r]
        r+=1
      m+=1

    while l < len(data_left):
      data[m] = data_left[l]
      l+=1
      m+=1
    while r < len(data_right):
      data[m] = data_right[r]
      r+=1
      m+=1
    return data
      
# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
merge_sort(data)
print(data)
