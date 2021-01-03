class Solution():
    def transcoin(self,coins:list(int),counts:int):
        coins=coins.sort()
        colenth=len(coins)
        if counts < coins[0]:
            print('0')
        else:
            for i in range(colenth):
               while i>0:
                    if coins[i-1]<=counts<=coins[i]:
                        a = counts //coins[i-1]
                        b = counts%coins[i-1]
                        i-=1









