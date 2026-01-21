import random

class Player:
    def __init__(self, name, health=3, proAI=False):
        self.name = name
        self.health = health
        self.proAI = proAI
        self.items = []
    
    def take_damage(self):
        self.health -= 1
        print(f"{self.name} takes damage. Resulting Player Health: {self.health}")
    
    def living(self):
        return self.health > 0
def shotgun():
    chance = random.choice([i/10 for i in range (11)])
    if chance <= 0.5:
        print("blank")
        return "blank"
    else:
        print("live")
        return "live"
def load_shotgun():
    num_of_shells = random.randint(4, 9)
    shells = []
    for i in range(num_of_shells):
        shell_type = random.choice(['blank', 'blank', 'live', 'live', 'live'])
        shells.append(shell_type)
    live_count = shells.count('live')
    blank_count = shells.count('blank')
    print(f"\n[* Shotgun loaded: {num_of_shells} shells - {live_count} live, {blank_count} blank *]")
    return shells
def calculate_shoot_self_value(shells, known_info):
    # the ai probability checker based of the amount of blank shells vs live shells left in the shotgun
    if not shells:
        return 0.0
    live_count = shells.count('live')
    blank_count = shells.count('blank')
    total = len(shells)
    if total == 0:
        return 0.0
    # Probability that a randomly chosen next shell is blank
    return blank_count / total 
def greedy_ai_decision(shells, player, opponent):
    if not shells:
        return "opponent"
    
    blank_prob = calculate_shoot_self_value(shells, {})
    live_prob = 1 - blank_prob
    
    print(f"\n[AI Analysis] \n *calculating* \n [{len(shells)} shells left]")
    print(f"[Blank round chances: {blank_prob:.2%}, Live round chances: {live_prob:.2%}]")
    
    # Greedy-algorithmic stuffs:
    # If blank probability is less than 60% then ai will shoot itself (meaning you the player are safe but the ai gets another turn)
    # If opponent health is rlly low and live round odds are greater than 50% the ai will then shoot opponent
    # BASICALLY the AI will shoot the opponent (you) if the live round odds are greater than a blank bullet/shell
    
    if blank_prob > 0.6:
        print(f"[AI Strat: High blank probability - shooting self for extra turn]")
        return "self"
    elif opponent.health <= 1 and live_prob > 0.5:
        print(f"[AI Strat: Opponent low health - The Ai will now slime you out twin!]")
        return "opponent"
    elif live_prob > blank_prob:
        print(f"[AI Strat: More lives than blanks - attempting shooting the opponent]")
        return "opponent"
    else:
        print(f"[AI Strat: Playing it very safe - shooting opponent]")
        return "opponent"
def shoot(target, shells, shooter, opponent):
    if not shells:
        print("Shotgun empty!")
        return False
    #shotgun stuff
    
    shell = shells.pop(0)
    print(f"\n{shooter.name} shoots {target}...")
    print(f"*BOOM* - {shell.upper()}!")
    
    if shell == 'live':
        if target == 'self':
            shooter.take_damage()
        else:
            opponent.take_damage()
        return False  
    else:
        print(f"{shooter.name} survives and gets another turn!")
        # Blank shell guarantees the shoota always get the other turn frfr
        return True
def player_turn(player, opponent, shells): #players turn stuffs
    while True:
        if not shells:
            print("\nShotgun empty! Reloading...")
            return True
        
        if player.proAI:
            target = greedy_ai_decision(shells, player, opponent)
        else:
            print(f"\n{player.name}'s turn - Shells remaining: {len(shells)}")
            target = input("Shoot (s)elf or (o)pponent? ").lower()
            while target not in ['s', 'o', 'self', 'opponent', 'opp', 'me', 'SELF', 'OPPONENT', 'Self', 'Opponent']:
                target = input("Invalid choice. Shoot (s)elf or (o)pponent? ").lower()
            target = 'self' if target == 's' else 'opponent'
        
        gets_extra_turn = shoot(target, shells, player, opponent)
        
        if not opponent.living():
            return False
        
        if not gets_extra_turn:
            return True
def game_round(player1, player2):
    """Play one round"""
    shells = load_shotgun()
    current_player = player1 if random.choice([True, False]) else player2
    
    print(f"\n{current_player.name} goes first!")
    
    while shells and player1.living() and player2.living():
        opponent = player2 if current_player == player1 else player1
        
        continue_round = player_turn(current_player, opponent, shells)
        
        if not continue_round:
            break
        

        current_player = player2 if current_player == player1 else player1
def main():
    print("=*=* BUCKSHOT ROULETTE *=*=\n")
    
    player1 = Player("Player 1", health=3, proAI=False)
    player2 = Player("AI Opponent", health=3, proAI=True)
    
    round_num = 1
    
    while player1.living() and player2.living():
        print(f"\n{'='*40}")
        print(f"ROUND {round_num}")
        print(f"{player1.name}: {player1.health} HP | {player2.name}: {player2.health} HP")
        print(f"{'*'*40}")
        
        game_round(player1, player2)
        round_num += 1
    
    print("\n" + "="*40)
    if player1.living():
        print(f" {player1.name} WINS! \n YEAH TWINNNN")
    else:
        print(f" {player2.name} WINS! \n YOU ACTUALLY LOST TO A COMPUTER LOSER")
    print("="*40)

if __name__ == "__main__":
    main()
    
" Brian Duru "