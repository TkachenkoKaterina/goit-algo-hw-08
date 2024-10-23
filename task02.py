import heapq


def merge_k_lists(lists):
    heap = []

    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i][0], i, 0))

    result = []

    while heap:
        value, list_idx, element_idx = heapq.heappop(heap)
        result.append(value)

        if element_idx + 1 < len(lists[list_idx]):
            next_tuple = (
                lists[list_idx][element_idx + 1], list_idx, element_idx + 1
                )
            heapq.heappush(heap, next_tuple)

    return result


if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)
