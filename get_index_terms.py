#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import get_morphs_tags as mf

###############################################################################
# 색인어 추출
def get_index_terms( mt_list):
    """ 형태소 분석 결과(형태소-품사 쌍)로부터 색인어를 추출
    색인어는 품사가 일반명사(NNG), 고유명사(NNP), 영어(SL), 숫자(SN), 한자(SH)이어야 함
    동일 어절 내에서 인접하여 결합된 경우도 색인어로 추출해야 함 (복합어)

    mt_list: a list of tuples (morpheme, tag)
    return value: a list of string (색인어 리스트)
    """
    nouns=[]
    my_list=[]
    for i in mt_list:
        a,b=i
        if(b=="NNG" or b=="NNP" or b=="SL" or b=="SN" or b=="SH"):
            my_list.append(a)
            nouns.append(a)
        else:

            if(len(my_list)>1):
                bb=''.join(my_list)
                nouns.append(bb)
                my_list.clear()
            elif(len(my_list)==1):
                my_list.clear()
            else:
                continue
    if(len(my_list)>1):
        bb=''.join(my_list)
        nouns.append(bb)
        my_list.clear()
        
    
    return nouns

###############################################################################
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print( "[Usage]", sys.argv[0], "in-file", file=sys.stderr)
        sys.exit()

    with open( sys.argv[1]) as fin:

        mt_freq = {}
    
        # 2 column format
        for line in fin.readlines():

            segments = line.split('\t')

            if len(segments) < 2:
                continue

            # 형태소, 품사 추출
            # result : list of tuples
            result = mf.get_morphs_tags(segments[1].rstrip())
    
            # 색인어 추출 (명사 및 복합명사 등)
            terms = get_index_terms(result)
        
            # 색인어 출력
            for term in terms:
                print(term)
