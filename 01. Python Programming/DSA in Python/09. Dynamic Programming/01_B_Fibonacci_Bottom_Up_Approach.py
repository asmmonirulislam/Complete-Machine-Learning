from typing import List

class DP:
    def fib(self, n:int)->int:
        if n<=1:
            return n
        dp = [-1 for _ in range(n+1)]
        dp[0]=0
        dp[1]=1
        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]

def main():
    dp = DP()
    x = dp.fib(6)
    print(x)    # 8

if __name__ == '__main__':
    main()