# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




def censored(cipher, key):
    censore = [" the ", " i ", " a ", " at ", " me " " that ", " why ", " when ", " where ", " how ", " be ", " and ",
               " of ", " in ", " off ",
               " to ", " too ", " have ", " it ", " you ", " for ", " he ", " with ", " she ", " they ", " them ",
               " we ", " on ", " do ",
               " does ", " say ", " this ", " but ", " his ", " not ", " no ", " yes ", " by ", " or ", " as ", " is ",
               " what ", " go ",
               " can ", " get ", " their ", " there ", " if ", " all ", " make ", " up "]
    ans = vigenere_decrypt(cipher, key)
    for g in range(len(censore)):
        if censore[g] in ans:
            print("-key", key, "-answer: ", ans)
            break  # if u find it, stop looking for it - in order to not print the same thing more than once

def vigerene_breakANY_sencored(cipher, len_key, key):
    if len_key <= 0:
        pass
    censore = [" the ", " i ", " a ", " at ", " me " " that ", " why ", " when ", " where ", " how ", " be ", " and ",
               " of ", " in ", " off ",
               " to ", " too ", " have ", " it ", " you ", " for ", " he ", " with ", " she ", " they ", " them ",
               " we ", " on ", " do ",
               " does ", " say ", " this ", " but ", " his ", " not ", " no ", " yes ", " by ", " or ", " as ", " is ",
               " what ", " go ",
               " can ", " get ", " their ", " there ", " if ", " all ", " make ", " up "]
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(alphabet)):
        new_key = key + alphabet[i]
        if len_key == 1:
            ans = vigenere_decrypt(new_key, cipher)
            for g in range(len(censore)):
                if censore[g] in ans:
                    print("-key: ", new_key, "-answer: ", ans)
                    break
        else:
            vigerene_breakANY_sencored(cipher, len_key - 1, new_key)
        new_key = key
        #reset key

def vigerene_breakANY(cipher, len_key, key):
    if len_key <= 0:
        pass
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(alphabet)):
        new_key = key + alphabet[i]
        if len_key == 1:
            print("-key: ", new_key, "-answer: ", vigenere_decrypt(new_key, cipher))
        else:
            vigerene_breakANY(cipher, len_key - 1, new_key)
        new_key = key
        #reset key^


def vigerene_break_2(msg):
    key = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            key = alphabet[i] + alphabet[j]
            print("-key", key, "-answer: ", vigenere_decrypt(key, msg))

def sencore_vigerene_break_2(msg):
    key = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sencore = [" the ", " i ", " a ", " at ", " me " " that ", " why ", " when ", " where ", " how ", " be ", " and ", " of ", " in ", " off ",
               " to ", " too ", " have ", " it ", " you ", " for ", " he ", " with ", " she ", " they ", " them ", " we ", " on ", " do ",
               " does ", " say ", " this ", " but ", " his ", " not ", " no ", " yes ", " by ", " or ", " as ", " is ", " what ", " go ",
               " can ", " get ", " their ", " there ", " if ", " all ", " make ", " up "]

    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            key = alphabet[i] + alphabet[j]
            ans = vigenere_decrypt(key, msg)
            for g in range(len(sencore)):
                if sencore[g] in ans:
                    print("-key", key, "-answer: ",ans)
                    break #if u find it, stop looking for it - in order to not print the same thing more than once




def vigenere_encrypt(key, msg):
    if len(key) <= 0:
        return msg

    new_msg = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for i in range(len(msg)):
        if msg[i] in alphabet:
            k = alphabet.find((key[i % len(key)]))
            offset = (alphabet.find(msg[i]) + k + len(alphabet)) % len(alphabet)
            new_msg = new_msg + alphabet[offset]
        else:
            new_msg = new_msg + msg[i]
    return new_msg


def vigenere_decrypt(key, msg):
    if len(key) <= 0:
        return msg

    new_msg = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for i in range(len(msg)):
        if msg[i] in alphabet:
            k = alphabet.find((key[i % len(key)]))
            offset = (alphabet.find(msg[i]) - k + len(alphabet)) % len(alphabet)
            new_msg = new_msg + alphabet[offset]
        else:
            new_msg = new_msg + msg[i]
    return new_msg


if __name__ == '__main__':
    key = "cherry"
    cipher = "vv sv, vv emv xf zg, kyyv mj rjl hlcuamfe: dlvkfgy kzq usscct me rjl dzlf xf qwmjvi voi jjkukj ypk ripqdw fd vykiyilslj hvvkllg," \
             " fi vv krig eidq hkrzlua r qgh fw vyslsjgz, rlf fp mrwsjzli ieu void: vv uzc, xf qnlig."
    print(cipher)
    msg = vigenere_decrypt(key, cipher)
    print(msg)
#start here
    print(" ")
    cipher2 = "istct xd ewpdcn lsxnw hepetd ewli xq pkpg pynzcp oxdrzkpgd pmlreaj hwli ist jyxgtchp th uzg pys isn xe th wpgp," \
              " xe hxwa xyhepyiwn sthleatlg pys qp ctaalrps qj ddxtewtcr pkpc bzgp mxkpcgp lco tcpmaatrlqwt. ewpgp th pydewpg istzgj" \
              " hwtrs diliph ispe ewth wlh pwgppon wleatyto."
    #sencore_vigerene_break_2(cipher2)
    vigerene_breakANY_sencored(cipher2, 2, "")
    print("result: key = pl")

    print("starting project")
    flag = ""

    while flag != "*":
        print("-chose: if you want to ENCRYPT enter 1, if you want to DECRYPT enter '2', if you want us to BREAK or CRACK the code enter '3',"
              " if you want to stop enter '*'")
        flag = input()
        if flag == "1":
            print("-please enter your massage and then the key")
            project_msg = input()
            project_key = input()
            print("encrypting...")
            print("-key: ", project_key, "-encryption: ", vigenere_encrypt(project_key, project_msg), "-original message: ", project_msg)
        elif flag == "2":
            print("-please enter your ENCRYPTED PROMPT that you want to DECRYPT, and then enter the key")
            project_cipher = input()
            project_key = input()
            print("decrypting...")
            print("-key: ", project_key, "-decryption: ", vigenere_decrypt(project_key, project_cipher), "-cipher: ", project_cipher)
        elif flag == "3":
            print("-i see you want us to BREAK THE CODE please enter the cipher you want us to break, and then the length of the key,"
                  " keep in mind, it only works when the wanted key has the length of 10 to 1, enter the length minus 1")
            project_cipher = input()
            len_key = input()
            numbers = "0123456789"
            len_key = numbers.find(len_key) + 1
            if len(project_cipher) >= 20:
                vigerene_breakANY_sencored(project_cipher, len_key, "")
            else:
                vigerene_breakANY(project_cipher, len_key, "")
        else:
            print("-i see u chose none of the above...")

