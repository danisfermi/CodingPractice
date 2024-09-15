from sortedcontainers import SortedList

def get_largest(input_list, N, K):
    smaller = SortedList()
    larger = SortedList()
    sum_smaller = 0
    window_size = float(N - K)
    result = []

    for i in range(len(input_list)):
        if i < K:
            larger.add(input_list[i])
            continue
        
        if i >= N:
            to_remove = input_list[i - N]
            if to_remove in larger:
                larger.remove(to_remove)
                to_add_back = smaller.pop(-1)
                larger.add(to_add_back)
                sum_smaller -= to_add_back
            else:
                smaller.remove(to_remove)
                sum_smaller -= to_remove
        
        # Add the new element to 'larger' and adjust
        larger.add(input_list[i])
        to_add = larger.pop(0)
        smaller.add(to_add)
        sum_smaller += to_add
        
        # Calculate the result
        result.append(float(sum_smaller) / min(float(i + 1 - K), window_size))

    return result

# Example usage
input_list = [20, 2, -2, 0, 10, 1, 5, -2, 0]
N = 5
K = 2
result = get_largest(input_list, N, K)
print(result)

