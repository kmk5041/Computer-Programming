#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

_CHO_ = 'ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ'
_JUNG_ = 'ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ'
_JONG_ = 'ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ' # index를 1부터 시작해야 함

# 겹자음 : 'ㄳ', 'ㄵ', 'ㄶ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅄ'
# 겹모음 : 'ㅘ', 'ㅙ', 'ㅚ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅢ'

_JAMO2ENGKEY_ = {
 'ㄱ': 'r',
 'ㄲ': 'R',
 'ㄴ': 's',
 'ㄷ': 'e',
 'ㄸ': 'E',
 'ㄹ': 'f',
 'ㅁ': 'a',
 'ㅂ': 'q',
 'ㅃ': 'Q',
 'ㅅ': 't',
 'ㅆ': 'T',
 'ㅇ': 'd',
 'ㅈ': 'w',
 'ㅉ': 'W',
 'ㅊ': 'c',
 'ㅋ': 'z',
 'ㅌ': 'x',
 'ㅍ': 'v',
 'ㅎ': 'g',
 'ㅏ': 'k',
 'ㅐ': 'o',
 'ㅑ': 'i',
 'ㅒ': 'O',
 'ㅓ': 'j',
 'ㅔ': 'p',
 'ㅕ': 'u',
 'ㅖ': 'P',
 'ㅗ': 'h',
 'ㅘ': 'hk',
 'ㅙ': 'ho',
 'ㅚ': 'hl',
 'ㅛ': 'y',
 'ㅜ': 'n',
 'ㅝ': 'nj',
 'ㅞ': 'np',
 'ㅟ': 'nl',
 'ㅠ': 'b',
 'ㅡ': 'm',
 'ㅢ': 'ml',
 'ㅣ': 'l',
 'ㄳ': 'rt',
 'ㄵ': 'sw',
 'ㄶ': 'sg',
 'ㄺ': 'fr',
 'ㄻ': 'fa',
 'ㄼ': 'fq',
 'ㄽ': 'ft',
 'ㄾ': 'fx',
 'ㄿ': 'fv',
 'ㅀ': 'fg',
 'ㅄ': 'qt'
}


###############################################################################
def is_hangeul_syllable(ch):
    '''한글 음절인지 검사
    '''
    if not isinstance(ch, str):
        return False
    elif len(ch) > 1:
        ch = ch[0]
    
    return 0xAC00 <= ord(ch) <= 0xD7A3

###############################################################################
def compose(cho, jung, jong):
    '''초성, 중성, 종성을 한글 음절로 조합
    cho : 초성
    jung : 중성
    jong : 종성
    return value: 음절
    '''
    if not (0 <= cho <= 18 and 0 <= jung <= 20 and 0 <= jong <= 27):
        return None
    code = (((cho * 21) + jung) * 28) + jong + 0xAC00

    return chr(code)

###############################################################################
# input: 음절
# return: 초, 중, 종성
def decompose(syll):
    '''한글 음절을 초성, 중성, 종성으로 분해
    syll : 한글 음절
    return value : tuple of integers (초성, 중성, 종성)
    '''
    if not is_hangeul_syllable(syll):
        return (None, None, None)
    
    uindex = ord(syll) - 0xAC00
    
    jong = uindex % 28
    jung = ((uindex - jong) // 28) % 21
    cho = ((uindex - jong) // 28) // 21

    return (cho, jung, jong)

###############################################################################
def str2jamo(str):
    '''문자열을 자모 문자열로 변환
    '''
    jamo = []
    for ch in str:
        if is_hangeul_syllable(ch):
            cho, jung, jong = decompose(ch)
            jamo.append( _CHO_[cho])
            jamo.append( _JUNG_[jung])
            if jong != 0:
                jamo.append( _JONG_[jong-1])
        else:
            jamo.append(ch)
    return ''.join(jamo)


###############################################################################
def jamo2engkey(jamo_str):

    eng=[]
    for ch in jamo_str:
        if ch in _JAMO2ENGKEY_:
            eng.append(_JAMO2ENGKEY_[ch])
        else:
            eng.append(ch)
    return ''.join(eng)
################################################################################

def engkey2jamo(eng):
    di={v:k for k,v in _JAMO2ENGKEY_.items()}
    jamo=[]
    for ch in eng:
        if ch in di:
            jamo.append(di[ch])
        else:
            jamo.append(ch)
    return ''.join(jamo)


#################################################################################
def jamo2syllable(jamo):
    chs=[]
    state=0
    for ch in jamo:
        if(False):
            a=1
        else:
            if(state==0):
                if(ch not in _JAMO2ENGKEY_.keys() or ch in _JUNG_):
                    t=[]
                    chs.append(ch)
                else:   
                    t=[]
                    t.append(ch)
                    state=1
            elif(state==1):
                if(len(t)>1):
                    if(ch in _JUNG_):
                        tt=jamo2engkey(t[-1]+ch)
                        di={v:k for k,v in _JAMO2ENGKEY_.items()}
                        t=t[:len(t)-1]
                        t.append(di[tt])
                        state=2
                    else:
                        state=2
                elif(len(t)==1):
                    if(ch in _CHO_ or ch in _JONG_):
                        chs.append(t[0])
                        t=[ch]
                    elif (ch not in _JAMO2ENGKEY_.keys()):
                        chs.append(ch)
                    else:
                        t.append(ch)

            if(state==2):
                if(len(t)>2):
                    if(len(t)>3):
                        if(ch in _JUNG_):
                            t.append(ch)
                            chs.append(compose(_CHO_.find(t[0]),_JUNG_.find(t[1]),_JONG_.find(t[2])+1))
                            t=t[3:]
                            state=1
                        elif(ch in _CHO_):
                            t.append(ch)
                            di={v:k for k,v in _JAMO2ENGKEY_.items()}
                            tt=t[2]+t[3]
                            k=jamo2engkey(tt)
                            if(k in di):
                                chs.append(compose(_CHO_.find(t[0]),_JUNG_.find(t[1]),_JONG_.find(di[k])+1))
                                t=t[4:]
                                state=1
                            else:
                                chs.append(compose(_CHO_.find(t[0]),_JUNG_.find(t[1]),_JONG_.find(t[2])+1))
                                t=[ch]
                                state=1
                    else:
                        if(ch in _JUNG_):
                            t.append(ch)
                            chs.append(compose(_CHO_.find(t[0]),_JUNG_.find(t[1]),0))
                            t=t[2:]
                            state=1
                        elif(ch in _JONG_ or ch in _CHO_):
                            t.append(ch)
                        elif ch not in _JAMO2ENGKEY_.keys():
                            chs.append(compose(_CHO_.find(t[0]),_JUNG_.find(t[1]),_JONG_.find(t[2])+1))
                            chs.append(ch)
                            t=[]
                            state=0

                else:
                    if(ch not in _JAMO2ENGKEY_.keys()):
                        chs.append(compose(_CHO_.find(t[0]),_JUNG_.find(t[1]),0))
                        chs.append(ch)
                        t=[]
                        state=0
                    elif(ch in _JUNG_):
                        pass
                    else:
                        t.append(ch)
    if(len(t)==2):
        chs.append(compose(_CHO_.find(t[0]),_JUNG_.find(t[1]),0))
    elif(len(t)==3):
        chs.append(compose(_CHO_.find(t[0]),_JUNG_.find(t[1]),_JONG_.find(t[2])+1))
    elif(len(t)==4):
        di={v:k for k,v in _JAMO2ENGKEY_.items()}
        tt=t[2]+t[3]
        k=jamo2engkey(tt)
        if(k in di):
            chs.append(compose(_CHO_.find(t[0]),_JUNG_.find(t[1]),_JONG_.find(di[k])+1))
        else:
            chs.append(compose(_CHO_.find(t[0]),_JUNG_.find(t[1]),_JONG_.find(t[2])))
            chs.append(t[3])

    elif(len(t)==1):
        chs.append(t[0])
    return ''.join(chs)
################################################################################
if __name__ == "__main__":
    
    i = 0
    line = sys.stdin.readline()

    while line:
        line = line.rstrip()
        i += 1
        print('[%06d:0]\t%s' %(i, line)) # 원문
    
        # 문자열을 자모 문자열로 변환 ('닭고기' -> 'ㄷㅏㄺㄱㅗㄱㅣ')
        jamo_str = str2jamo(line)
        print('[%06d:1]\t%s' %(i, jamo_str)) # 자모 문자열

        # 자모 문자열을 키입력 문자열로 변환 ('ㄷㅏㄺㄱㅗㄱㅣ' -> 'ekfrrhrl')
        key_str = jamo2engkey(jamo_str)
        print('[%06d:2]\t%s' %(i, key_str)) # 키입력 문자열
        
        # 키입력 문자열을 자모 문자열로 변환 ('ekfrrhrl' -> 'ㄷㅏㄹㄱㄱㅗㄱㅣ')
        jamo_str = engkey2jamo(key_str)
        print('[%06d:3]\t%s' %(i, jamo_str)) # 자모 문자열

        # 자모 문자열을 음절열로 변환 ('ㄷㅏㄹㄱㄱㅗㄱㅣ' -> '닭고기')
        syllables = jamo2syllable(jamo_str)
        print('[%06d:4]\t%s' %(i, syllables)) # 음절열

        line = sys.stdin.readline()
