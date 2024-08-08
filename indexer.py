#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import get_morphs_tags as mf
import get_index_terms as term
import pickle

###############################################################################
def indexing_tagged(indexing, sentences, filename):
    """ 형태소 분석 파일로부터 색인 정보를 생성 (역색인, 문장)
    indexing : 역색인 dictionary (key : index term, value : set of sentences)
    sentences : 색인된 문장 리스트
    filename : 형태소 분석 파일
    """
    sentence=''
    with open(filename)as fin:
        for line in fin.readlines():
            segments=line.split('\t')
            if(len(segments)<2):
                sentences.append(sentence.strip())
                sentence=''
            else:
                sentence=sentence+' '
                sentence=sentence+segments[0]
                result=mf.get_morphs_tags(segments[1].rstrip())
                terms=term.get_index_terms(result)
                for t in result:
                    if(t[0] in terms):
                        if(t[0] in indexing):
                            indexing[t[0]].add(len(sentences))
                        else:
                            indexing[t[0]]={len(sentences)}



#############################################################################
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print( "[Usage]", sys.argv[0], "in-file(s)", file=sys.stderr)
        sys.exit()

    inverted_indexing = {}
    sentences = []
    
    for filename in sys.argv[1:]:
        indexing_tagged( inverted_indexing, sentences, filename)

    with open("index.pickle","wb") as fout:
        pickle.dump((inverted_indexing, sentences), fout)

