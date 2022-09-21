#1st problem 
min_num = float("inf")

def getMaxSum(arr , k):
    max_len = -min_num
    for i in range(len(arr) - k + 1):
        sum_ = 0
        for j in range(i, i + k):
            sum_ += arr[j]
        max_len = max(max_len, sum_)
    return max_len


n , k = map(int, input().split())
arr = list(map(int , input().split()))
print(getMaxSum(arr, k))

# 2nd problem

def getAllTriplets(arr):
	n = len(arr)
	main_list = []
	for i in range(0, n-1):
		l = i + 1
		r = n - 1
		x = arr[i]
		sub_list = []
		while (l < r):
			if (x + arr[l] + arr[r] == 0):
			    list_a = [x,arr[l],arr[r]]
			    sub_list.append(list_a)
				l += 1
				r -= 1
			elif (x + arr[l] + arr[r] < 0):
				l += 1
			else:
				r -= 1
		main_list.append(sub_list)
    return main_list

arr = [ -1, 0, 1, 2, -1, 4]
arr.sort()
list_a = getAllTriplets(arr)
set_a = set(list_a)
for i in set_a:
    print(i)

# 3rd problem
string = input()
rev_string = ""
for i in string:
    rev_string = i + rev_string
print(string == rev_string)
