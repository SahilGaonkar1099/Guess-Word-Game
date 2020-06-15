import random as r

def StringToList():#This function reads the file content and then converts its contents to list and returns the words list
    with open("Filename.txt",'r') as F:
        words=F.read()
        wordsList=words.split()#read contents gets converted to list of words
    return(wordsList)

print("WELCOME TO GUESS THE WORD GAME \n\n")

def LenOfWord():
    word = []
    W=input("Enter the Size[4-20] of the word U want to crack:\n")
    while len(word) != int(W):
        word = r.choice(StringToList())
    return word
def Game():
    i=0
    while True:
        print("GUESS GAME BEGINS\n")
        word=LenOfWord()
        word=word.lower();W=[]
        for i in range(0,len(word)):
            W.append('*')
        print(W)
        S=len(word)
        Help=[]
        s=len(word)
        Guessed=0
        for i in word:
            Help.append(i)
        Add=Help.copy()
        while len(Help)>0:
            In=input("Next latter:\n")
            if len(In)==1:
                if In in Add:
                    print("Good Keep Going:\n")
                    I=Add.index(In)
                    Add.remove(In)
                    Add.insert(I,'*')
                    W.__delitem__(I)
                    W.insert(I,In)
                    print(W)
                    Help.remove(In)
                    Guessed+=1
                else:
                    print("Word Does'nt has this letter:\n")
                    S-=1
                    print("Left chances",S)
                    if S>0:
                        continue
                    else:
                        break
            else:
                print("U tried to enter many latters at once\n")
                continue
        if s==Guessed:
            print("Congratulations You WoN\n")
            print("UR Guessed Word:",word)
            i=1
        else:
            print("U failed to Guess:",word)
            print("Better luck next time")
            i=1
        if DoYouWant2Continue(i):
            continue
        else:
            print("Thanks for Playing the Game\n\n")
            break

def DoYouWant2Continue(i):
    if i > 0:
        DoU = input("Do You want to continue?: Yes=>y : No=>n:\n")
        if DoU == 'y':
            return True
        else:
            return False


Game()
