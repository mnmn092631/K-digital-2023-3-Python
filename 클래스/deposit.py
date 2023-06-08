class Deposit:
    def __init__(self, initial, interest, n):
        self.initial = initial
        self.interest = interest
        self.n = n
    
    def profit(self):
        return self.initial * (1 + self.interest) ** self.n

deposit1 = Deposit(1000000, 0.035, 7)
print(f"원리금은 {int(deposit1.profit())}원입니다.")
