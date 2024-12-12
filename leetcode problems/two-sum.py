# solve two sum problem in O(n) time complexity

def twosum(list,target):
    pair_index = {}
    for i ,num in enumerate(list):
        if target - num in pair_index:
            return[i,pair_index[target - num]]
        pair_index[num] = i

numbers = [3,2,4]
target = 6

pair = twosum(numbers,target)
print(pair)