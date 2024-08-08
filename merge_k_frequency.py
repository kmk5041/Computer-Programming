#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 복수의 빈도 파일을 병합하는 프로그램

import sys
import heapq

###############################################################################
def merge_k_sorted_freq(input_files):
    '''
    input_files : list of input filenames (frequency files; 2 column format)
    '''

    fins = []
    number=0
    k= len(input_files)
    for i in range(k):
        fins.append(open(input_files[i]))
    heap = []
    finished = [False for _ in range(k)] # [False] * k
    for i in range(len(fins)):
        li=fins[i].readline().split()
        li.append(i)
        li[1]=int(li[1])
        li=tuple(li)
        heapq.heappush(heap,li)

    a=heapq.heappop(heap)
    b=a[2]
    number=a[1]
    li=fins[b].readline()
    if(li==''):
        finished[b]=True
    if(not finished[b]):
        li=li.split()
        li.append(b)
        li[1]=int(li[1])
        li=tuple(li)
        heapq.heappush(heap,li)

    while(len(heap)):
        n=heapq.heappop(heap)
        nn=n[2]
        li=fins[nn].readline()
        if(li==''):
            finished[nn]=True
        if(not finished[nn]):
            li=li.split()
            li.append(nn)
            li[1]=int(li[1])
            li=tuple(li)
            heapq.heappush(heap,li)
        if(n[0]==a[0]):
            number+=n[1]
        else:
            print(a[0],'\t',number)
            a=n
            number=n[1]

    for i in range(k):
        fins[i].close()

###############################################################################
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print( "[Usage]", sys.argv[0], "in-file(s)", file=sys.stderr)
        sys.exit()

    merge_k_sorted_freq( sys.argv[1:])
