import random
import time
import matplotlib.pyplot as plt

def selection_sort(arr):
    swap_count = 0
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swap_count += 1
    return swap_count

def insertion_sort(arr):
    swap_count = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            swap_count += 1
            j -= 1
        arr[j + 1] = key
    return swap_count

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left_half, left_swaps = merge_sort(arr[:mid])
    right_half, right_swaps = merge_sort(arr[mid:])
    merged, merge_swaps = merge(left_half, right_half)

    return merged, left_swaps + right_swaps + merge_swaps

def merge(left, right):
    result = []
    i = j = 0
    swap_count = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        swap_count += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result, swap_count

def quick_sort_fixed(arr):
    def _quick_sort(arr, swap_count):
        if len(arr) <= 1:
            return arr, swap_count

        pivot = arr[len(arr) // 2]
        left = []
        middle = []
        right = []

        for x in arr:
            if x < pivot:
                left.append(x)
                swap_count += 1 
            elif x == pivot:
                middle.append(x)
            else:
                right.append(x)
                swap_count += 1  

        sorted_left, left_swaps = _quick_sort(left, swap_count)
        sorted_right, right_swaps = _quick_sort(right, swap_count)
        
        return sorted_left + middle + sorted_right, left_swaps + right_swaps

    sorted_array, swap_count = _quick_sort(arr, 0)
    return swap_count

def quick_sort_swaps(arr):
    def _quick_sort(arr):
        if len(arr) <= 1:
            return arr, 0 

        pivot = arr[len(arr) // 2]
        left = []
        middle = []
        right = []
        swap_count = 0  

        for x in arr:
            if x < pivot:
                left.append(x)
            elif x == pivot:
                middle.append(x)
            else:
                right.append(x)

        sorted_left, left_swaps = _quick_sort(left)
        sorted_right, right_swaps = _quick_sort(right)
        
        swap_count += left_swaps + right_swaps

        return sorted_left + middle + sorted_right, swap_count

    sorted_array, swap_count = _quick_sort(arr)
    return swap_count


def generate_random_data(min_value=0, max_value=100, size=1000):
    return [random.randint(min_value, max_value) for _ in range(size)]

ans = [[], [], [], [], [], [], [], [], [], []]
avg=[0,0,0,0,0]

for _ in range(10000):
    data = generate_random_data(0, 100, 100) 

    start = time.time()
    swap_count = selection_sort(data[:])  
    ans[0].append(swap_count)
    s=time.time() - start
    ans[1].append(s)
    avg[0]+=s

    start = time.time()
    swap_count = insertion_sort(data[:])  
    ans[2].append(swap_count)
    s=time.time() - start
    ans[3].append(s)
    avg[1]+=s

    start = time.time()
    _, merge_swaps = merge_sort(data[:])  
    ans[4].append(merge_swaps)
    s=time.time() - start
    ans[5].append(s)
    avg[2]+=s

    start = time.time()
    swap_count = quick_sort_swaps(data[:]) 
    ans[6].append(swap_count)
    s=time.time() - start
    ans[7].append(s)
    avg[3]+=s

    start = time.time()
    swap_count = quick_sort_fixed(data[:]) 
    ans[8].append(swap_count)
    s=time.time() - start
    ans[9].append(s)
    avg[4]+=s

fig, axs = plt.subplots(3, 2, figsize=(12, 12))  
axs = axs.flatten()  

axs[0].scatter(ans[0], ans[1], color='blue', label='selection_sort')
axs[0].scatter(ans[2], ans[3], color='green', label='insertion_sort')
axs[0].scatter(ans[4], ans[5], color='red', label='merge_sort')
axs[0].scatter(ans[6], ans[7], color='yellow', label='quick_sort_swaps')
axs[0].scatter(ans[8], ans[9], color='purple', label='quick_sort_fixed')
axs[0].set_title('Sort')
axs[0].set_xlabel('counts')
axs[0].set_ylabel('seconds')
axs[0].legend()

axs[1].scatter(ans[0], ans[1], color='blue', label='selection_sort')
axs[1].set_title('Selection Sort')
axs[1].set_xlabel('counts')
axs[1].set_ylabel('seconds')
axs[1].legend()

axs[2].scatter(ans[2], ans[3], color='green', label='insertion_sort')
axs[2].set_title('Insertion Sort')
axs[2].set_xlabel('counts')
axs[2].set_ylabel('seconds')
axs[2].legend()

axs[3].scatter(ans[4], ans[5], color='red', label='merge_sort')
axs[3].set_title('Merge Sort')
axs[3].set_xlabel('counts')
axs[3].set_ylabel('seconds')
axs[3].legend()

axs[4].scatter(ans[6], ans[7], color='yellow', label='quick_sort_swaps')
axs[4].set_title('Quick Sort (Swaps)')
axs[4].set_xlabel('counts')
axs[4].set_ylabel('seconds')
axs[4].legend()

axs[5].scatter(ans[8], ans[9], color='purple', label='quick_sort_fixed')
axs[5].set_title('Quick Sort (Fixed)')
axs[5].set_xlabel('counts')
axs[5].set_ylabel('seconds')
axs[5].legend()

plt.tight_layout() 
plt.show()

print('selection_sort:', float(avg[0]) / 100)
print('insertion_sort:', float(avg[1]) / 100)
print('merge_sort:', float(avg[2]) / 100)
print('quick_sort_swaps:', float(avg[3]) / 100)
print('quick_sort_fixed:', float(avg[4]) / 100)

