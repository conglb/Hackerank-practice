from collections import Counter

class Solution:

    def __init__(self):
        self.x = 0
        self.n = 0
        self.shoes = []
        self.customers = []
        self.ans = 0

    def input(self):
        self.x = int(input())

        shoes = input()
        self.shoes = map(int, shoes.split())

        self.n = int(input())
        for _ in range(self.n):
            t = tuple(map(int, input().split()))
            self.customers.append(t)


    def process(self):
        counter = Counter(self.shoes)
        for customer in self.customers:
            shoeType = customer[0]
            cost = customer[1]
            if counter[shoeType]:
                if counter[shoeType] > 0:
                    self.ans += cost
                    counter[shoeType] -= 1

    def output(self):
        print(self.ans)

if __name__ == "__main__":
    sol = Solution()
    sol.input()
    sol.process()
    sol.output()
