from typing import List

class DP:
    def fibonacci(self, n:int, dp:List[int])->int:
        if n<=1:
            return n
        elif dp[n] != -1:
            return dp[n]
        dp[n] = self.fibonacci(n-1, dp) + self.fibonacci(n-2, dp)
        return dp[n]
    def fib(self, n:int)->int:
        dp = [-1 for _ in range(n+1)]
        return self.fibonacci(n, dp)

def main():
    dp = DP()
    x = dp.fib(6)
    print(x)    # 8

if __name__ == '__main__':
    main()