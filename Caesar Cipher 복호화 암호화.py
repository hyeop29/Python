from string import ascii_lowercase, ascii_uppercase
import enchant

d = enchant.Dict("en_US")
lower_alphabet = list(ascii_lowercase)
upper_alphabet = list(ascii_uppercase)

# 암호화 함수
def encrypt(k,x) : 
    for i in range(len(x)):
        if x[i].isupper() :
            j = upper_alphabet.index(x[i])
            j = (j + k) % 26
            x[i] = upper_alphabet[j]
        elif x[i].islower() :
            j = lower_alphabet.index(x[i])
            j = (j + k) % 26
            x[i] = lower_alphabet[j]
        else :
            continue

    return ''.join(x)
# 복호화 함수
def decrypt(x) :
    for k in range(26) :
        new_x = list(x)
        for i in range(len(x)) :
            #print("i 값은 : {}" .format(i))
            if new_x[i].isupper() :
                j = upper_alphabet.index(new_x[i])
                #print("바뀌기 전 인덱스 위치 : {}" .format(j))
                j = (j - k) % 26
                #print("바뀐 후 인덱스 위치 : {}" .format(j))
                new_x[i] = upper_alphabet[j]
            elif new_x[i].islower() :
                j = lower_alphabet.index(new_x[i])
                j = (j - k) % 26
                new_x[i] = lower_alphabet[j]
            else :
                continue
        str_k = ''.join(new_x)
        # 해당 key 값으로 복호화한 문장이 말이 되는지 확인하는 부분
        answer = str_k.split()
        for j in range(len(answer)):
            if(d.check(answer[j])) :
                if j + 1 == len(answer) :
                    return str_k
            else :
                break
    return "Not a valid sentece!"

k = int(input("Enter k : "))
x = list(input("Sentenc to encrypt : "))
print("Encrypted sentence : {}".format((encrypt(k,x))))
print("-------------------------------------------")
x = list(input("Enter ciphertext to decrypt : "))
print("Decrypted sentence : {}". format(decrypt(x)))