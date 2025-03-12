'''
/**

 * Process a list of ballots,
 and return all candidates sorted in descending
 order by their total number of points.

 ['shan', 'jason']
a ballet can contain up to 3 votes
and order of the vote is important

each voter can vote for upto 3 candidates
each voter can vote in order
Ballot:{
    shan: 3
    jason: 2
    adam: 1
    martin: 0
}

 */

voter, candidates, ballots contains candidate votes
List<String> getResults(List<Ballot> ballots)
    return "list of names of candidates in order"
'''
from collections import defaultdict
from typing import List, Dict


def getResults(Ballots: List[Dict[str, int]])->str:
    candidate_points = defaultdict(int)

    # for ballot in Ballots:


if __name__ == '__main__':
    ballots = [
        {'shan': 3, 'jason': 2, 'adam': 1, 'martin': 0},
        {'shan': 3, 'jason': 2, 'adam': 1, 'martin': 0},
        {'shan': 3, 'jason': 2, 'adam': 1, 'martin': 0},
        {'shan': 3, 'jason': 2, 'adam': 1, 'martin': 0},
    ]
    results = getResults(ballots)
    print(results)

# '''
# /**
#
#  * Process a list of ballots,
#  and return all candidates sorted in descending
#  order by their total number of points.
#
#  ['shan', 'jason']
# a ballet can contain up to 3 votes
# and order of the vote is important
#
# each voter can vote for upto 3 candidates
# each voter can vote in order
# Ballot:{
#     shan: 3
#     jason: 2
#     adam: 1
#     martin: 0
# }
#
#  */
#
# voter, candidates, ballots contains candidate votes
# List<String> getResults(List<Ballot> ballots)
#     return "list of names of candidates in order"
# '''

