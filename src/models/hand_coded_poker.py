from collections import Counter

def split_suites_ranks(inp_data):
    #Method that returns a list containing list of suites and ranks.

    suites = list()
    ranks = list()
    for i in range(0, 9, 2):
        suites.append(inp_data[i])
    for j in range(1, 10, 2):
        ranks.append(inp_data[j])
    return [suites, ranks]

def one_pair(inp_data):
    #Method that returns a boolean value if the input data has one pair poker hand.

    ranks = split_suites_ranks(inp_data)[1]
    counter = Counter(ranks)
    values = counter.values() #Getting the values of the dictionary so that we can check if there is any pair.
    if 2 in values:
        return True
    else:
        return False

def two_pairs(inp_data):
    # Method that returns a boolean value if the input data has two pairs poker hand.

    ranks = split_suites_ranks(inp_data)[1]
    counter = Counter(ranks)
    values = counter.values() #Getting the values of the dictionary so that we can check if there is any pair.
    
    if sorted(values) == [1,2,2]:
        return True
    else:
        return False

def three_of_a_kind(inp_data):
    # Method that returns a boolean value if the input data has three of a kind poker hand.

    ranks = split_suites_ranks(inp_data)[1]
    counter = Counter(ranks)
    values = counter.values() #Getting the values of the dictionary so that we can check if there is any pair.

    if set(values) == set([3,1]):
        return True
    else:
        return False
    
def straight(inp_data):
    # Method that returns a boolean value if the input data has a straight poker hand.

    ranks = split_suites_ranks(inp_data)[1]
    dummy_ranks = list() #Creating a sequentially dummy rank for comparing the actual card's rank.
    ranks = sorted(ranks)
    low = ranks[0]
    high = ranks[-1]
    for i in range(low, high+1):
        dummy_ranks.append(i)
    
    if ranks == sorted(dummy_ranks):
        return True
    else:
        return False

def flush(inp_data):
    # Method that returns a boolean value if the input data has a flush poker hand.

    suites = split_suites_ranks(inp_data)[0]
    if len(set(suites)) == 1:
        return True
    else:
        return False

def full_house(inp_data):
    # Method that returns a boolean value if the input data has a full house poker hand.

    if three_of_a_kind(inp_data) and two_pairs(inp_data):
        return True
    else:
        return False
    
def four_of_a_kind(inp_data):
    # Method that returns a boolean value if the input data has a four of a kind poker hand.
    ranks = split_suites_ranks(inp_data)[1]
    counter = Counter(ranks)
    values = counter.values() #Getting the values of the dictionary so that we can check if there is any pair.

    if sorted(values) == [1,4]:
        return True
    else:
        return False

def straight_flush(inp_data):
    # Method that returns a boolean value if the input data has a straight flush hand.

    if straight(inp_data) and flush(inp_data):
        return True
    else:
        return False

def royal_flush(inp_data):
    # Method that returns a boolean value if the input data has a royal flush poker hand.

    dummy_rank = [1,10,11,12,13]
    ranks = split_suites_ranks(inp_data)[1]
    ranks = sorted(ranks)
    if ranks == dummy_rank and flush(inp_data):
        return True
    else:
        return False

def get_poker_hand(inp_data):
    #Method to return the numerical category of a poker hand.

    if royal_flush(inp_data):
        return 9
    elif straight_flush(inp_data):
        return 8
    elif four_of_a_kind(inp_data):
        return 7
    elif full_house(inp_data):
        return 6
    elif flush(inp_data):
        return 5
    elif straight(inp_data):
        return 4
    elif three_of_a_kind(inp_data):
        return 3
    elif two_pairs(inp_data):
        return 2
    elif one_pair(inp_data):
        return 1
    else:
        return 0
