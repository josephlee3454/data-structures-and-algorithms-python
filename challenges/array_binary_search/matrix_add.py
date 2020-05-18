first_array = [1,2,3,4,5,6]
second_array = [4,-2,7,9]
third_array = [7,10,50,7]
major_array =[first_array,second_array,third_array]

def sum_first_arr(first_array):
  first_array_total = 0
  for value in first_array:
    first_array_total += value
  print(first_array_total)
  print(major_array)
  
  return first_array_total


def sum_second_arr(second_array):
  second_array_total = 0
  for value in second_array:
    second_array_total += value
  print(second_array_total)
  
  return second_array_total


def sum_third_arr(third_array):
  third_array_total = 0
  for value in third_array:
    third_array_total += value
  print(third_array_total)
  return third_array_total
def sum_major_arr(major_array):
    major_array_total = 0
    for value in major_array:
      major_array_total += value
    print(major_array_total)
    return major_array_total
sum_first_arr(first_array)
sum_second_arr(second_array)
sum_third_arr(third_array)
sum_major_arr(major_array)

