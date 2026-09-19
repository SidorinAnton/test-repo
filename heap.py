from typing import List, Optional, TypeVar

T = TypeVar("T")


class MinHeap:
    def __init__(self, args: Optional[List[T]] = None):
        self.heap: List[T] = []

        if args is None:
            return

        for val in args:
            self.add(val)

    def add(self, value: T):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def pop(self) -> T:
        self._swap(0, len(self.heap) - 1)
        val = self.heap.pop()
        self._sift_down(0)
        return val

    def _swap(self, idx1: int, idx2: int):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def _sift_up(self, idx: int):
        while idx > 0 and self.heap[(idx - 1) // 2] > self.heap[idx]:
            self._swap(idx, (idx - 1) // 2)
            idx = (idx - 1) // 2

    def _sift_down(self, idx: int):
        while True:
            left_idx = idx * 2 + 1
            right_idx = idx * 2 + 2
            min_idx = idx

            if left_idx < len(self.heap) and self.heap[left_idx] < self.heap[min_idx]:
                min_idx = left_idx

            if right_idx < len(self.heap) and self.heap[right_idx] < self.heap[min_idx]:
                min_idx = right_idx

            if min_idx == idx:
                break

            self._swap(idx, min_idx)
            idx = min_idx


def main():
    heap = MinHeap()
    heap.add(10)
    heap.add(1)
    heap.add(30)
    heap.add(30)
    heap.add(200)
    heap.add(5)

    assert heap.pop() == 1
    assert heap.pop() == 5
    assert heap.pop() == 10
    assert heap.pop() == 30
    assert heap.pop() == 30
    assert heap.pop() == 200


if __name__ == "__main__":
    main()
