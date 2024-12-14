#!/bin/python3

import math
import os
import random
import re
import sys


def acmTeam(topic):
    none_topic = []
    for i in range(len(topic)):
        none_topic.append(topic[i].count('1'))

    print(none_topic)
    return topic

if __name__ == '__main__':
    n = 4

    m = 5

    topic =['10101', '11100', '11010', '00101']

    result = acmTeam(topic)

    print(result)