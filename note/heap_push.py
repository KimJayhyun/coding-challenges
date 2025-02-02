import unittest


def push_heap(arr, target, call_back):
    arr.append(target)

    idx = len(arr) - 1
    while idx > 0:
        parent_idx = (idx - 1) >> 1

        if not call_back(arr[idx], arr[parent_idx]):
            break

        arr[idx], arr[parent_idx] = arr[parent_idx], arr[idx]
        idx = parent_idx

    return arr[0]


import unittest


class TestPushHeap(unittest.TestCase):
    def test_min_heap_basic(self):
        """최소 힙의 기본 기능과 반환값 테스트"""
        arr = []
        # 순서대로 5, 3, 7, 1을 삽입하고 각각의 root 값 확인
        root = push_heap(arr, 5, lambda x, y: x < y)
        self.assertEqual(arr, [5])
        self.assertEqual(root, 5)

        root = push_heap(arr, 3, lambda x, y: x < y)
        self.assertEqual(arr, [3, 5])
        self.assertEqual(root, 3)

        root = push_heap(arr, 7, lambda x, y: x < y)
        self.assertEqual(arr, [3, 5, 7])
        self.assertEqual(root, 3)

        root = push_heap(arr, 1, lambda x, y: x < y)
        self.assertEqual(arr, [1, 3, 7, 5])
        self.assertEqual(root, 1)

    def test_max_heap_basic(self):
        """최대 힙의 기본 기능과 반환값 테스트"""
        arr = []
        # 순서대로 5, 8, 3, 9를 삽입하고 각각의 root 값 확인
        root = push_heap(arr, 5, lambda x, y: x > y)
        self.assertEqual(arr, [5])
        self.assertEqual(root, 5)

        root = push_heap(arr, 8, lambda x, y: x > y)
        self.assertEqual(arr, [8, 5])
        self.assertEqual(root, 8)

        root = push_heap(arr, 3, lambda x, y: x > y)
        self.assertEqual(arr, [8, 5, 3])
        self.assertEqual(root, 8)

        root = push_heap(arr, 9, lambda x, y: x > y)
        self.assertEqual(arr, [9, 8, 3, 5])
        self.assertEqual(root, 9)

    def test_duplicate_values(self):
        """중복 값 삽입과 반환값 테스트"""
        arr = []
        roots = []
        for value in [4, 4, 4, 4]:
            root = push_heap(arr, value, lambda x, y: x < y)
            roots.append(root)
        self.assertEqual(arr, [4, 4, 4, 4])
        self.assertEqual(roots, [4, 4, 4, 4])

    def test_descending_input(self):
        """내림차순 입력에 대한 최소 힙 테스트"""
        arr = []
        last_root = None
        for value in [5, 4, 3, 2, 1]:
            last_root = push_heap(arr, value, lambda x, y: x < y)
        self.assertEqual(arr[0], 1)  # 최종 root는 1
        self.assertEqual(last_root, 1)  # 반환된 root도 1
        # 힙 속성 검증
        for i in range(len(arr) // 2):
            if 2 * i + 1 < len(arr):
                self.assertLessEqual(arr[i], arr[2 * i + 1])
            if 2 * i + 2 < len(arr):
                self.assertLessEqual(arr[i], arr[2 * i + 2])

    def test_ascending_input(self):
        """오름차순 입력에 대한 최대 힙 테스트"""
        arr = []
        last_root = None
        for value in [1, 2, 3, 4, 5]:
            last_root = push_heap(arr, value, lambda x, y: x > y)
        self.assertEqual(arr[0], 5)  # 최종 root는 5
        self.assertEqual(last_root, 5)  # 반환된 root도 5
        # 힙 속성 검증
        for i in range(len(arr) // 2):
            if 2 * i + 1 < len(arr):
                self.assertGreaterEqual(arr[i], arr[2 * i + 1])
            if 2 * i + 2 < len(arr):
                self.assertGreaterEqual(arr[i], arr[2 * i + 2])

    def test_custom_comparison(self):
        """커스텀 비교 함수와 반환값 테스트"""
        arr = []
        roots = []
        values = [-5, 3, -2, 4]
        for value in values:
            root = push_heap(arr, value, lambda x, y: abs(x) < abs(y))
            roots.append(root)
        # 마지막으로 반환된 root는 절대값이 가장 작은 값이어야 함
        self.assertEqual(abs(roots[-1]), 2)
        # 힙 속성 검증
        for i in range(len(arr) // 2):
            if 2 * i + 1 < len(arr):
                self.assertLessEqual(abs(arr[i]), abs(arr[2 * i + 1]))
            if 2 * i + 2 < len(arr):
                self.assertLessEqual(abs(arr[i]), abs(arr[2 * i + 2]))

    def test_single_element(self):
        """단일 원소 삽입과 반환값 테스트"""
        arr = []
        root = push_heap(arr, 1, lambda x, y: x < y)
        self.assertEqual(arr, [1])
        self.assertEqual(root, 1)


if __name__ == "__main__":
    unittest.main()
