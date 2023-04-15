# class Heap():
#     def __init__(self) -> None:
#         self.heap_array = [None]
    
#     def move_up(self, idx):
#         if idx <= 1:
#             return False

#         parent_idx = idx // 2
#         if self.heap_array[idx] < self.heap_array[parent_idx]:
#             return True
#         return False

#     def insert(self, value):
#         length = len(self.heap_array)
        
#         idx = length - 1
#         self.heap_array.append(value)
        
#         if length <= 1:
#             return
        
#         while self.move_up(idx):
#             self.heap_array[idx], self.heap_array[idx // 2] = self.heap_array[idx // 2], self.heap_array[idx]
#             idx //= 2

heap = [144, 2, 3, 9, 10, 12]

def move_up(idx):
    pass

def make_heap(arr):
    tmp_arr = [None]
    for n in arr:
        pass