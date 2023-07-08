def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + equal + quicksort(right)


def is_anagram(first_string, second_string):
    if first_string == '' and second_string == '':
        return ('', '', False)
    order_first_string = quicksort(first_string.lower())
    order_second_string = quicksort(second_string.lower())
    order_first_string = ''.join(order_first_string)
    order_second_string = ''.join(order_second_string)
    if order_first_string == order_second_string:
        return (order_first_string, order_second_string, True)
    return (order_first_string, order_second_string, False)
