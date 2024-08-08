#!/usr/bin/env python3
# coding: utf-8

import sys

def get_morphs_tags(tagged):
    first=tagged.split('+')
    final=[]
    for i in range(0,len(first)):
        s=first[i]
        if(len(s)!=0):
            if(s[0]=='/'):
                if(s[1]=='/'):
                    ss=s.split('/')
                    t=('/',ss[2])
                    final.append(t)
                else:
                    ss=s.split('/')
                    t=('+',ss[1])
                    final.append(t)
            else:
                ss=s.split('/')
                t=(ss[0],ss[1])
                final.append(t)
    return final
###############################################################################
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print( "[Usage]", sys.argv[0], "in-file", file=sys.stderr)
        sys.exit()

    with open(sys.argv[1]) as fin:

        for line in fin.readlines():

             #2 column format
            segments = line.split('\t')

            if len(segments) < 2: 
                continue

            #  result : list of tuples
            result = get_morphs_tags(segments[1].rstrip())
        
            for morph, tag in result:
                print(morph, tag, sep='\t')
