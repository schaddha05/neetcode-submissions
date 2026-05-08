class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        count = {}
        for num in hand:
            count[num] = count.get(num, 0) + 1 
        
        for num in hand:
            if count[num]:
                for n in range(num, num + groupSize):
                    if n not in count or count[n] == 0:
                        return False 
                    count[n] -= 1

        return True 
