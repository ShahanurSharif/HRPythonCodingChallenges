#!/bin/python3

import math
import os
import random
import re
import sys


def acmTeam(topic):
    topics = [int(t, 2) for t in topic]
    max_topics = 0
    team_count = 0
    for i in range(len(topics)):
        for j in range(i+1, len(topics)):
            combined = int(topics[i])|int(topics[j])
            known_topics = bin(combined).count('1')
            print(known_topics)
            if known_topics>max_topics:
                max_topics = known_topics
                team_count = 1
            elif known_topics == max_topics:
                team_count += 1

    return [max_topics, team_count]

if __name__ == '__main__':
    n = 4

    m = 5

    topic =['10101', '11100', '11010', '00101']

    result = acmTeam(topic)

    print(result)