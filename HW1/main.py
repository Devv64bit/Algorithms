def selection_sort(arr, size):
    for step in range(size):
        min_idx = step

        for c in range(step + 1, size):
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if arr[c] < arr[min_idx]:
                min_idx = c

        # put min at the correct position
        (arr[step], arr[min_idx]) = (arr[min_idx], arr[step])


arrs = [-3, 55, 11, 0, -2]
sizes = len(arrs)
print('Sorted Array in Ascending Order:')
selection_sort(arrs, sizes)
print(arrs)


def insertion_sort(arr):
    for step in range(1, len(arr)):
        key = arr[step]
        k = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[k] to key>array[k].
        while k >= 0 and key < arr[k]:
            arr[k + 1] = arr[k]
            k -= 1

        arr[k + 1] = key


n_arrs = [-5, 66, 3, 0, 22]
insertion_sort(n_arrs)
print('Sorted Array in Ascending Order: ')
print(n_arrs)


def bubble_sort(arr):

  # loop to access each array element
    for d in range(len(arr)):

        # make boolean to keep track of swaps
        swapped = False

        # loop to compare array elements
        for x in range(0, len(arr) - d - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if arr[d] > arr[x + 1]:

                # swapping elements if elements
                # are not in the intended order
                tmp = arr[x]
                arr[x] = arr[x + 1]
                arr[x + 1] = tmp

                swapped = True

        if not swapped:
            break


n_arr = [-7, 99, 1, -2, 45]
bubble_sort(n_arr)
print('Sorted Array in Ascending Order:')
print(n_arr)
