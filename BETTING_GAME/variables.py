GAMES = (" Cashpot "," Hot Pick "," Pick Three "," One Drop "," Four play ","Lucky Day Lotto")

# (game_num, min_wager, nums, max_num, fixed_wager = False)
GAME_CONFIGS = [(0,10,1,36),(1,20,1,16,True),
(2,40,3,35),(3,10,1,36),(4,20,4,15),(5,20,5,20,True)]

RULES = [
    """Pick a number between 1 and 36.
    You win if your selected number is
    randomly generated.
    The minimum wager is $10.00.
    Pay-out is 26 times the wager.""",
    """Pick a number between 1 and 16.
    You win if your selected number is
    randomly generated.
    The only wager applicable is $20.00.
    Pay-out is fixed at $1,000.00.""",
    """Pick 3 numbers between 1 and 35.
    You win if your selected numbers are randomly generated.
    The minimum wager is $40.00.
    If your wager is $40.00, pay-out $1,000.00.
    If your wager is greater than $40.00 but less than $60.00,
    pay-out is $4,000.00.
    If your wager is $60.00 or greater, pay-out is 10 times your wager.""",
    """Pick a number between 1 and 36.
    You win if your selected number is
    randomly generated.
    The minimum wager is $10.00.
    Pay-out is 27 times the wager.""",
    """Pick 4 numbers between 1 and 15.
    You win if your selected numbers are
    randomly generated.
    The minimum wager is $10.00.
    Pay-out is 60 times the wager.""",
    """Pick 5 numbers between 1 and 20.
    You win if your selected numbers
    are randomly generated.
    The only wager applicable $20.00.
    The pay-out is $100,000.00."""]