class BoardingQueue:
    def __init__(self):
        self.queue = []

    def add_passenger(self, name, priority):
        self.queue.append((priority, name))
        self._bubble_sort()
        
    def _bubble_sort(self):
        n = len(self.queue)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.queue[j][0] < self.queue[j + 1][0]:
                    self.queue[j], self.queue[j + 1] = self.queue[j + 1], self.queue[j]    

    def board_passenger(self):
        if not self.queue:
            print("Черга порожня.")
            return
        priority, name = self.queue.pop()
        print(f"Посаджений пасажир: {name} з пріоритетом {priority}")


boarding = BoardingQueue()
boarding.add_passenger("Іван", 1)
boarding.add_passenger("Анна", 3) 
boarding.add_passenger("Олег", 2)  

boarding.board_passenger()
boarding.board_passenger()
boarding.board_passenger()