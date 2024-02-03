#!/usr/bin/env python3
from collections import deque

class Solution:
    radiant = "R"
    dire = "D"
    def predictPartyVictory(self, senate: str) -> str:
        if len(senate) <= 0:
            return ""
        party_match = {self.radiant: "Radiant", self.dire: "Dire"}
        action_round = deque(senate)
        radiant_stack = []
        dire_stack = []
        while action_round:
            # print(action_round)
            # print("radiant", radiant_stack)
            # print("dire", dire_stack)
            next_senator = action_round.popleft()
            if next_senator == self.radiant:
                if dire_stack:
                    action_round.append(dire_stack.pop())
                else:
                    radiant_stack.append(next_senator)
            elif radiant_stack:
                action_round.append(radiant_stack.pop())
            else:
                dire_stack.append(next_senator)
                
        if radiant_stack:
            return party_match[self.radiant]
        if dire_stack:
            return party_match[self.dire]
        return party_match[senate[0]]


if __name__ == "__main__":
    s = Solution()
    print(s.predictPartyVictory("DDRRR"))
