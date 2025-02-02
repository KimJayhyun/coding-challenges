import unittest


def get_max_from_heap(arr):
    if not arr:
        return "error"
    # 마지막 부모 노드의 idx : `len(arr) // 2 - 1`
    for idx in range(len(arr) // 2 - 1, -1, -1):
        # heapify
        while True:
            largest_of_three_idx = idx  # parent_node
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2

            if (
                left_child_idx < len(arr)
                and arr[largest_of_three_idx] < arr[left_child_idx]
            ):
                largest_of_three_idx = left_child_idx

            if (
                right_child_idx < len(arr)
                and arr[largest_of_three_idx] < arr[right_child_idx]
            ):
                largest_of_three_idx = right_child_idx

            if largest_of_three_idx == idx:
                break

            arr[largest_of_three_idx], arr[idx] = arr[idx], arr[largest_of_three_idx]

            # 아래로 내려감
            idx = largest_of_three_idx

    return arr[0]


import unittest


class TestMaxHeap(unittest.TestCase):
    def test_get_max(self):
        """최대 힙에서 최대값을 정확히 반환하는지 테스트"""
        # 기본적인 케이스
        self.assertEqual(get_max_from_heap([4, 10, 3, 5, 1]), 10)

        # 이미 최대 힙 상태인 경우
        self.assertEqual(get_max_from_heap([100, 50, 30, 20, 10]), 100)

        # 정렬되지 않은 경우
        self.assertEqual(get_max_from_heap([3, 1, 15, 10, 20, 30]), 30)

        # 중복된 값이 있는 경우
        self.assertEqual(get_max_from_heap([7, 7, 7, 7, 7]), 7)

        # 한 개의 원소만 있는 경우
        self.assertEqual(get_max_from_heap([42]), 42)

        # 두 개의 원소만 있는 경우 (큰 값이 먼저)
        self.assertEqual(get_max_from_heap([99, 10]), 99)

        # 두 개의 원소만 있는 경우 (작은 값이 먼저)
        self.assertEqual(get_max_from_heap([10, 99]), 99)

    def test_get_max_empty_heap(self):
        """빈 배열이 들어오면 예외 발생해야 함"""
        self.assertEqual(get_max_from_heap([]), "error")

    def test_get_max_negative_numbers(self):
        """음수가 포함된 경우 테스트"""
        self.assertEqual(get_max_from_heap([-1, -10, -5, -3, -20]), -1)

        # 양수와 음수가 섞인 경우
        self.assertEqual(get_max_from_heap([-10, 20, -30, 40, 0]), 40)


if __name__ == "__main__":
    unittest.main()
