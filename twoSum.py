 def twoSum(arr, target):
...     res = {}
...     for i in range(len(arr)):
...             if target - arr[i] in res:
...                     return [res[target - arr[i]], i]
...             else:
...                     res[arr[i]] = i
