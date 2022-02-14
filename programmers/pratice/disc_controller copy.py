
import heapq
from operator import length_hint
from os import sep
from turtle import st

def solution(jobs):
    jobs.sort()
    count, last = 0, -1
    wait = []
    time = jobs[0][0]
    length = len(jobs)
    answer = 0
    
    while count < length:
        for s, t in jobs:
            if last < s <= time:
                heapq.heappush(wait, (t, s))
                print(heapq)
        if len(wait) > 0:
            last = time
            term, start = heapq.heappop(wait)
            count += 1
            time += term
            answer += (time - start)
            print(heapq)
        else:
            time += 1
    print(answer // length)
    return answer // length


solution([[0, 3], [1, 9], [2, 6]])