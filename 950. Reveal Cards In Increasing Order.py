from collections import deque
from typing import Deque


def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
    """
    Solves the problem by using "Reverse Simulation". 
    Time Complexity - O(n)
    """
    deq: Deque[int] = deque()
    deck.sort()

    #Reverse Simulation. 
    deq.append(deck.pop())
    for i in range(len(deck)) :
        num = deq.popleft()
        deq.append(num)
        deq.append(deck.pop())

    ans = list(deq)
    ans.reverse()
    return ans
    
    