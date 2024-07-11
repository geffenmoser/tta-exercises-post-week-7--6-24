import numpy as np

#exercise 1
array_1d = np.arange(10, dtype=np.uint8)
print(array_1d)

#exercise 2
l = [3.14, 2.17, 0, 1, 2]

l_arr = np.array(l)
print(l_arr)
print("Data Type:", l_arr.dtype)

l_arr = l_arr.astype(np.int8)
print(l_arr)
print("Data Type:", l_arr.dtype)

#exercise 3
array_3 = array_1d[1:]
array_3 = array_3.reshape(3, 3)
print(array_3)

#exercise 4
array_4 = np.round(np.random.rand(4, 5), 2)
print(array_4)

#exercise 5
print(array_4[1])

#exercise 6
reversed_array = array_1d[::-1]
print(reversed_array)

#exercise 7
array_7 = np.eye(4, dtype=float)
print(array_7)

#exercise 8
array_sum = np.sum(array_1d)
array_mean = np.mean(array_1d)
print(f"Sum: {array_sum}")
print(f"Mean: {array_mean}")

#exercise 9
array_9 = np.arange(1, 21, dtype=np.uint8)
array_9 = array_9.reshape(4, 5)
print(array_9)

#exercise 10
array_10 = array_1d[array_1d % 2 == 1]
print(array_10)
