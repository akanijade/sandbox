def binary_search(list, item):
    first = 0
    last = len(list) - 1
    found = False
    while( first <= last and found is False):
        mid = (first+last)//2
        if list[mid] == item:
            found = True
        else:
            if item < list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

list_2 = [2,4,8,1,5]
list_2.sort()
print(list_2)
print(binary_search(list_2,1))
print(binary_search(list_2,6))