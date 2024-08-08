#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

###############################################################################
def word_count(filename):
    """ 단어 빈도 dictionary를 생성한다. (key: word, value: frequency)
    
    filename: input file
    return value: a sorted list of tuple (word, frequency) 
    """
    dic={}
    my_list=[]
    with open(filename) as fin:
        for word in fin.readlines():
            word=word.rstrip()
            if(word not in dic):
                dic[word]=1
            else:
                dic[word]=dic[word]+1

    for key, val in dic.items():
        t=(key,val)
        my_list.append(t)
    my_list.sort()
    return my_list








###############################################################################
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print( "[Usage]", sys.argv[0], "in-file", file=sys.stderr)
        sys.exit()

    result = word_count( sys.argv[1])

    # list of tuples
    for w, freq in result:
        print( "%s\t%d" %(w, freq))
