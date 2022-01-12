sequence_of_numbers = input("Введите числа через пробел:")

list_of_numbers = list(map(int, sequence_of_numbers.split()))

element = int(input("Введите число:"))


def sorting_the_list(list_of_numbers):
    for i in range(1, len(list_of_numbers)):
        x = list_of_numbers[i]
        idx = i
        while idx > 0 and list_of_numbers[idx-1] > x:
            list_of_numbers[idx] = list_of_numbers[idx-1]
            idx -= 1
        list_of_numbers[idx] = x
    return list_of_numbers


def binary_search(array, element, left, right): 
    if left > right:
        print( element, "нет в  списке")
        return False
    
    middle = (right+left) // 2
    
    if array[middle] == element: 
        return middle
    elif element < array[middle]: 
        return binary_search(array, element, left, middle-1)
    else: 
        return binary_search(array, element, middle+1, right)
    
array = sorting_the_list(list_of_numbers)

print('список:', array)


try:
    index_of_number = binary_search(array, element, 0, len(array))
    if index_of_number is not False :
     
       if (index_of_number -1) >=0:
           print("Индекс числа, который меньше введенного числа, будет", index_of_number -1)
       else:
           print("В списке нет числа меньше, чем введенное число")
    
except IndexError as e:
    print(e)
    print(element,"нет в списке")


