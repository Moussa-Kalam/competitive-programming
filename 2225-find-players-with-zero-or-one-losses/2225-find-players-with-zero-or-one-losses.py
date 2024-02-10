class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        # count wins and losses
        wins = dict()
        losses = dict()
        
        for winner, loser in matches:
            wins[winner] = wins.get(winner, 0) + 1
            
            losses[loser] = losses.get(loser, 0) + 1
            
            if loser not in wins :
                wins[loser] = 0
        
        players_no_losses = [player for player in wins if player not in losses]
        players_one_loss = [player for player, loss_count in losses.items() if loss_count == 1]
        
        return [sorted(players_no_losses), sorted(players_one_loss)]
        
       