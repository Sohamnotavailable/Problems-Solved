"""
Given a list of integer pairs and a parallel list of
student answers,
return the count of correct sums.
If the two lists differ in length, compare only up to the
shorter
length and ignore any extra items.
"""
from typing import List, Tuple

def additions_score(pairs: List[Tuple[int, int]], answers: List[int]) -> int:
    score = 0
    limit = min(len(pairs), len(answers))
    for i in range(limit):
        if pairs[i][0] + pairs[i][1] == answers[i]:
            score+=1
    return score
