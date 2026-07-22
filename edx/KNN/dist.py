import numpy as np
import random
import scipy.stats as ss

def distance(p1, p2):
    """
    Compute the Euclidean distance between two points p1 and p2.
    """
    return np.sqrt(np.sum((p1 - p2) ** 2))


p1 = np.array([1, 1])
p2 = np.array([4, 4])

dist = distance(p1,p2)


def majority_vote(votes):

    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1

    winners=[]
    max_counts = max(vote_counts.values())
    for vote, count in vote_counts.items():
        if count == max_counts:
            winner.append(vote)

    return random.choice(winners)


votes = [1,2,3,1,2,3,3,3,3]

vote_counts = majority_vote(votes)


def majority_vote_short(votes):
    
    mode, count = ss.mstats.mode(votes)
    return random.choice(mode)