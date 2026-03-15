"""
Simulate scissor-rock-paper.
Given two parallel lists of moves (’rock’, ’paper’, ’
scissor’),
count wins for user and computer. Compare moves only up
to the
length of the shorter list.
Return:
’user’ if user wins more rounds,
’computer’ if computer wins more rounds,
’tie’ otherwise.
"""
from typing import List

def scissor_rock_paper_winner(user_moves: List[str], comp_moves: List[str]) -> str:
    user_wins = 0
    comp_wins = 0
    limit = min(len(user_moves), len(comp_moves))
    
    wins = {
        ('rock', 'scissor'),
        ('scissor', 'paper'),
        ('paper', 'rock')
    }
    
    for i in range(limit):
        u = user_moves[i]
        c = comp_moves[i]
        if u==c:
            continue
        if (u, c) in wins:
            user_wins+=1
        else:
            comp_wins+=1
            
    if user_wins > comp_wins:
        return 'user'
    elif comp_wins > user_wins:
        return 'computer'
    else:
        return 'tie'
