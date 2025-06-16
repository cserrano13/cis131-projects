# Module3 Assignment4
# author - cesar
# date - 2025-06-15
"""
Dice Game Simulation: Craps * 1_000_000
Simulates games of craps and tabulates the results
"""
import random

def main():
    """
    Main function will first initialize one dict to track the results,
    results will be recorded as:
        int(roll_count): list[win_count, loss_count]
    Then enter a loop to iterate 1_000_000 times,
    at the end of each loop the results will be recorded into the craps_results dict,
    results to be recorded include: 
        - roll_01: num_of_wins/num_of_losses
        - roll_02: num_of_wins/num_of_losses
        - roll_03: num_of_wins/num_of_losses
        - etc...
    """

    # initialize variables to track results, iteration count, and number of rolls/game
    games = 0
    results = {}
    roll_count = 0
    
    # begin looping through simulations
    while (games < 1_000_000):
        print(f"\nGame #{games+1}")
        def roll_dice(roll_count):
            """Roll two dice and return their face values as a tuple."""
            die1 = random.randrange(1, 7)
            die2 = random.randrange(1, 7)
            return (die1, die2)  # pack die face values into a tuple

        def display_dice(dice):
            """Display one roll of the two dice."""
            die1, die2 = dice  # unpack the tuple into variables die1 and die2
            print(f'Player rolled {die1} + {die2} = {sum(dice)}')

        die_values = roll_dice(roll_count)  # first roll
        roll_count += 1 # increment every time dice are rolled
        print(f"Roll #{roll_count}") # display roll counter
        display_dice(die_values)

        # determine game status and point, based on first roll
        sum_of_dice = sum(die_values)

        if sum_of_dice in (7, 11):  # win
            game_status = 'WON'
            if (roll_count not in results):
                results[roll_count] = [1, 0] # create record if nonexistent
            else:
                results[roll_count][0] += 1 # increments the wins value in results dict
        elif sum_of_dice in (2, 3, 12):  # lose
            game_status = 'LOST'
            if (roll_count not in results):
                results[roll_count] = [0, 1] # create record if nonexistent
            else:
                results[roll_count][1] += 1 # increments the losses value in results dict
        else:  # remember point
            game_status = 'CONTINUE'
            my_point = sum_of_dice
            print('Point is', my_point)

        # continue rolling until player wins or loses
        while game_status == 'CONTINUE':
            die_values = roll_dice(roll_count)
            roll_count += 1 # increment every time dice are rolled
            print(f"Roll #{roll_count}") # display roll counter
            display_dice(die_values)
            sum_of_dice = sum(die_values)

            if sum_of_dice == my_point:  # win by making point
                game_status = 'WON'
                if (roll_count not in results):
                    results[roll_count] = [1, 0] # create record if nonexistent
                else:
                    results[roll_count][0] += 1 # increments the wins value in results dict
            elif sum_of_dice == 7:  # lose by rolling 7
                game_status = 'LOST'
                if (roll_count not in results):
                    results[roll_count] = [0, 1] # create record if nonexistent
                else:
                    results[roll_count][1] += 1 # increments the losses value in results dict

        # display "wins" or "loses" message
        if game_status == 'WON':
            print('Player wins')
            games += 1 # increment game iteration counter
            roll_count = 0 # reset roll counter at end of game
        else:
            print('Player loses')
            games += 1 # increment game iteration counter
            roll_count = 0 # reset roll counter at end of game
    
    # end of game iterations, display total results
    total_wins = 0
    total_losses = 0
    print("|Roll\t|Wins\t|Losses\t|%Resolved\t|Cumulative %Resolved")
    for i in range(len(results)):
        if ((i+1) in results):
            v1, v2 = results[i+1]
            total_wins += v1
            total_losses += v2
            print(f"|{i+1}\t|{v1}\t|{v2}\t|{(v1 + v2) / games * 100:.2f}\t\t|{(total_wins + total_losses) / games * 100:.2f}")
        if ((i+1) == len(results)):
            win_rate = (total_wins / games * 100)
            loss_rate = (total_losses / games * 100)
            print(f"Win rate: {win_rate:.2f}%")
            print(f"Loss rate: {loss_rate:.2f}%")
main()
