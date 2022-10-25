def reverse_iterative(list , left , right):
    if(left > right):
        left , right = right , left
    if(left < 0 or right >= len(list)):
        return -1
    while(left < right):
        list[left] , list[right] = list[right] , list[left]
        left += 1
        right -= 1
    return list

def reverse_recursive(list , left , right):
    if(left > right):
        left , right = right , left
    if(left < 0 or right >= len(list)):
        return -1
    list[left] , list[right] = list[right] , list[left]
    if(left < right):
        reverse_recursive(list , left+1 , right-1)
    return list

list = [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
print(reverse_iterative(list , 0 , 9))
print(reverse_recursive(list , 1 , 8))