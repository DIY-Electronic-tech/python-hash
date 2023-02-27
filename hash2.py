from datetime import datetime
import time

hash_len = 16

# chr() --> char
# ord() --> Num

def rtXtr(root, num):
    return num ** (1 / root)



def arr_mixing(inArr, type_mix):
    # transposition
    if type_mix % 2 == 0:
        inArr = arr_mixing_t0(inArr)
        inArr = arr_mixing_t1(inArr)
    else:
        inArr = arr_mixing_t1(inArr)
        inArr = arr_mixing_t0(inArr)
    
    return inArr


def arr_mixing_t0(inArr):
    for i in range(len(inArr)//2):
            inArr[i], inArr[len(inArr)-1-i] = inArr[len(inArr)-1-i], inArr[i]
    return inArr

def arr_mixing_t1(inArr):
    for i in range(len(inArr)//2):
        inArr[i], inArr[len(inArr)//2-1+i] = inArr[len(inArr)//2-1+i], inArr[i]
    return inArr


def string_multiplication_t0(inArr):
    oneVal = inArr[0]                   # inArr[len(inArr)-1] *= inArr[0]
    for i in range(len(inArr)-1):
        inArr[i] *= inArr[i+1]
    inArr[len(inArr)-1] *= oneVal
    return inArr


def convertArrToHash(inArr):
    str_hash = ''
    for i in range(len(inArr)):
        strHex = hex(inArr[i])[2:]
        while len(strHex) != 1:
            num = 0
            for j in range(len(strHex)):
                num += int(strHex[j], base=16)
            strHex = hex(num)[2:]
        
        str_hash += strHex

    return str_hash


def getHash(inStr):
    #inStr = list(inStr)
    """hash_len_dataIn = inStr[:hash_len]
    hash_len_dataIn = list(hash_len_dataIn)"""
    hash_len_dataIn = []

    if len(inStr) > hash_len:
        hash_len_dataIn = list(map(lambda x: ord(x), inStr[:hash_len]))
        for i in range(hash_len, len(inStr)):
            #print(i)
            for j in range(hash_len):
                #print(chr(int( rtXtr(2, ord(hash_len_dataIn[j]) * ord(inStr[i])) )))
                hash_len_dataIn[j] *= ord(inStr[i])

    elif len(inStr) < hash_len:
        hash_len_dataIn = list(map(lambda x: ord(x), inStr))
        hashVal = len(hash_len_dataIn) * (hash_len - len(hash_len_dataIn))

        for i in range(len(inStr), hash_len):
            hash_len_dataIn.append(hash_len_dataIn[i % len(inStr)] + abs(hashVal - (i+1)) * (hashVal + (i+1)) // (i-len(inStr)+1)) # (max(hashVal, (i+1)) // min(hashVal, (i+1)))    i-len(inStr)+1

    hash_len_dataIn = arr_mixing(hash_len_dataIn, len(inStr))
    hash_len_dataIn = string_multiplication_t0(hash_len_dataIn)
    return convertArrToHash(hash_len_dataIn)



"""print('Print "$" key to exit')
while True:
    strInput = input('Print any string: ')
    if strInput == '$':
        break
    else:
        print(getHash(strInput))"""

import random

allChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
            'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'а', 'б', 'в', 'г',
            'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
            'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю',
            'я', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л',
            'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ',
            'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', '@', '#', '%', '^', '&', '*', '/', '+',
            '-', ':', ';', ',', '.', '!', '?', '(', ')', '{', '}', '[', ']', '=',
            '<', '>', '_', '"', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']


def generateRandomString(leng):
    strOut = ''
    for i in range(leng):
        strOut += allChars[random.randint(0, len(allChars)-1)]
    return strOut

length_word = 10
counter = 100000
datalog = ''
arrAllGenHash = []
arrAllGenStr = []
coincidenceStr = 0
coincidenceHash = 0


datalog += 'tick: ' + str(counter) + '; ' + str(hash_len) + ' symbols hash length;' + ' length word: ' + str(length_word) + ';\n...'

start_time = datetime.now()

while counter > 0:
    counter -= 1
    arrAllGenStr.append(generateRandomString(length_word))
    arrAllGenHash.append(getHash(arrAllGenStr[len(arrAllGenStr)-1]))
    if arrAllGenHash[len(arrAllGenStr)-1] in arrAllGenHash[:len(arrAllGenHash)-1]:
        datalog += arrAllGenHash[len(arrAllGenStr)-1] + '\t' + arrAllGenStr[len(arrAllGenStr)-1] + '\n'
        coincidenceHash += 1

    if arrAllGenStr[len(arrAllGenStr)-1] in arrAllGenStr[:len(arrAllGenStr)-1]:
        coincidenceStr += 1
    
    
print(datalog)
print(coincidenceHash, coincidenceStr)
print('Time has passed:', datetime.now() - start_time)

#print(getHash('Hello'))




