from collections import deque


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        
        # Deque will store (start_day, num_people)
        dq = deque()
        
        # Day 1: One person knows the secret
        dq.append((1, 1))
        
        # Total number of people who know the secret
        total = 1
        
        for day in range(2, n + 1):
            # Remove people who forget the secret today
            while dq and dq[0][0] + forget == day:
                total -= dq.popleft()[1]
                total %= MOD
            
            # New people who learn the secret today
            new_people = 0
            for start_day, num_people in dq:
                if start_day + delay <= day:
                    new_people += num_people
            
            # Add new people to deque who will start sharing tomorrow
            if new_people > 0:
                # Check if there's already someone who starts sharing from this day
                if dq and dq[-1][0] == day:
                    dq[-1] = (dq[-1][0], dq[-1][1] + new_people)  # Add to the last element if same start day
                else:
                    dq.append((day, new_people))  # Otherwise, append new entry for this day
        
            
            # Add to the total count of people who know the secret
            total += new_people
            total %= MOD
        
        return total

sol = Solution()
print(sol.peopleAwareOfSecret(6, 2, 4))