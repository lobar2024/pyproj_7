from collections import deque

class Queue:
    def __init__(self, max_size=None):
        self._data = deque()
        self._max_size = max_size

    def enqueue(self, item):
        if self._max_size and len(self._data) >= self._max_size:
            raise OverflowError("Navbat to'ldi!")
        self._data.append(item)

    def dequeue(self):
        if not self._data:
            raise IndexError("Navbat bo'sh!")
        return self._data.popleft()

    def peek(self):
        return self._data[0] if self._data else None

    def __len__(self):   return len(self._data)
    def __str__(self):   return f"Queue{list(self._data)}"
    def is_empty(self):  return len(self._data) == 0


if __name__ == "__main__":
    q = Queue(max_size=4)
    q.enqueue("Ali")
    q.enqueue("Vali")
    q.enqueue("Soli")
    print(q)                  # Queue['Ali', 'Vali', 'Soli']
    print(q.dequeue())        # Ali
    print(q.peek())           # Vali
    print("Uzunlik:", len(q)) # 2
