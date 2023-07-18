# Entire Source Code of the Game

def chp_1():
    score_1=0
    print()
    print("CHAPTER I - PREMISE")
    print()
    print("The game is set in the fictional world of Azeroth.")
    print("You are a Hobbit, peacefully living in your village, The Meadows.")
    print("But one day you wake up to find that your best friend, James is missing.")
    print("James's home is empty and even the Meadow-Folk, i.e., the villagers, have no clue \
as to where he is.")
    a=input("Please press the enter key to continue.")
    print()
    print("As you approach his door, you find a note from the Royal guards with the Elvish \
King's seal on it.")
    print("It reads - James has been accused of stealing the Precious Gem that resided in \
the Queen's crown.")
    print("You come to know that the footsteps of the thief lead to James's house, \
hence the soldiers have arrested him and put him in prison by the King's orders.")
    print("Only you believe that James is innocent hence it's up to you to prove his innocence.")
    score_1+=100
    a=input("Please press the enter key to continue.")
    return score_1

def chp_2():
    score_2=0
    print()
    print("CHAPTER II - THE SEARCH BEGINS...")
    print()
    print("You decide to look inside his house to get some clues as to what actually happened.")
    print("You notice that there are some signs of struggle near the main door and the kitchen.")
    print("You also find some weird things that shouldn't belong in James's house, they are - ")
    print("A long wooden smoking pipe, a dark-blue conical hat and a few strands of white \
hair, possibly from a beard.")
    print("After see these objects, you start to wonder to whom such things belong to...")
    a=input("Please press the enter key to continue.")
    print()
    
    # Guess the Word game
    b=""
    score_2_1=0
    while b!="3" :
        print("Guess the person to whom a long wooden smoking pipe, a dark-blue \
conical hat and a few strands of white hair could belong to.")
        print("Your options are -")
        print("1. Royal guards     2. A Hobbit Villager     3. A Wizard    4. A Dragon")
        b=input()
        if b!="3" :
            print("Wrong answer, please try again")
            if score_2_1<3:
                score_2_1+=1
    print("Yes, you are right. These are the possessions of a Wizard!")
    score_2 += (4-score_2_1)*50
    a=input("Please press the enter key to continue.")
    print()
    print("You search the house for further clues.")
    print("Upon inspecting the fireplace, you find a secret note left by James, which \
enlightens you about what happened the previous night.")
    print("He writes that at late night, an unknown entity(whom you have successfully \
identified as the Wizard) broke into his home.")
    print("As James tried to grab the intruder, he was incapacitated by it(the Wizard), who  \
cast a spell of silence on him, so that James won't be able to tell the Guards what happened.")
    a=input("Please press the enter key to continue.")
    print()
    print("In his unexpected confrontation with the Wizard, James had managed to snatch \
the hat, pipe and some hair off before the Wizard turned invisible and escaped.")
    print("You understand that the Wizard's plan was to frame James in order to get \
the Royal Guards off his trail and run back to his lair.")
    print("Now you have to embark on a quest to help James get out of the prison and \
make sure that the evil Wizard is punished for his crimes.")
    score_2+=100
    a=input("Please press the enter key to continue.")
    return score_2
    
def chp_3():
    score_3=0
    print()
    print("CHAPTER III - THE CULPRIT")
    print()
    print("Since the Wizard is a close friend and an advisor to the king, he will be \
at the king's palace at this time of the day.")
    print("You have to first find the Missing Gem and then present it to the king along \
with the true story of the robbery.")
    print("You begin your travel through the Mirkwood forest towards the Wizard's lair...")
    a=input("Please press the enter key to continue.")
    print()
    print("At the Wizard's lair, you encounter a guard patrolling the gate. The guard wouldn't \
let anyone pass through without solving a puzzle.")
    print("Since the Wizard prefers only speaking to intelligent people, you have to outsmart \
the guard in a puzzle set by the Wizard himself, to prove your intelligence.")
    print("The rules of this puzzle are simple -")
    print()
    
    # 21 Matchsticks Game
    
    print("1. The guard will place 21 matchsticks on a table.")
    print("2. You and the Guard will take alternate turns to pick up the matchsticks, with you \
going first.")
    print("3. You can pick 1, 2, 3 or 4 matchsticks depending on your choice during a turn.")
    print("4. The person who picks the last matchstick loses the game.")
    a=input("Please press the enter key to start the game.")
    f="Yes"
    while f=="Yes" :
        d=21
        while d!=1 :
            c=int(input("Enter the number of matchsticks you want to pick. - "))
            d-=c
            e=5-c
            d-=e
            print("The Guard picks up", e, "matchsticks.")
        print("And since you picked up the last matchstick, you lose the game.")
        f=input("Do you want to try again? - ")
    print()
    print("Wait a minute...")
    print("You realise that this game is impossible to win if you are the first one \
to pick the matchstick first.")
    print("This time you agree play the puzzle but ask the Guard to go first.")
    print("The Guard replies with a smile that you have figured out the catch in the puzzle, and \
have hence proved your intelligence.")
    print("The Guard opens the gate and you go in...")
    score_3+=100
    a=input("Please press the enter key to continue.")
    return score_3
    
def chp_4():
    score_4=0
    print()
    print("CHAPTER IV - AN UNEXPECTED ALLY")
    print()
    print("The Wizard is currently at the palace, hence you can look for clues regarding the \
Stolen Gem")
    print("As you go further indoors you meet a Centaur, the Wizard's assistant.")
    print("The Wizard of often mistreats his assistant, Centaur, and makes him do \
unnecessarily difficult chores.")
    print("On the other hand the Centaur is honest and wise, and knows about the Wizard's crime.")
    a=input("Please press the enter key to continue.")
    print()
    print("He agrees to help you, but can answer only 3 questions, or else the Wizard will be \
alerted due to a special spell that was cast on the Centaur, when he became his assistant.")
    print("Choose your questions wisely.")
    print()
    
    # Choose your Question game
    
    score_4_1=0
    j=""
    while j!="Continue" :
        print("What will be your first question - ")
        print("1. Where was the Wizard on the night of the robbery?")
        print("2. What did the Wizard have for Breakfast?")
        g=int(input())
        if g==1 :
            print("The Centaur replies that he had seen the Wizard slip through the gates and \
venture out during that night.")
        else :
            print("The Centaur replies that the Wizard had a sandwich, disappointed in such \
a useless question.")
        print()
        print("What will be your second question - ")
        print("1. Did he meet with anybody later that night?")
        print("2. What type of sandwich did he eat?")
        h=int(input())
        if h==1 :
            print("The Centaur replies that he did meet a viking and exchanged some items ")
        else :
            print("The Centaur replies that it was a PB and J sandwich, even more disappointed.")
        print()
        print("What will be your third question - ")
        print("1. Where can I find this Viking?")
        print("2. Who made the sandwiches?")
        i=int(input())
        if i==1 :
            print("The Centaur replies that the Viking usually drinks at the local Tavern.")
        else :
            print("The Centaur replies that he made them and storms off, muttering that he \
wasted his time with you.")
            print("Try again")
        print()
        if g+h+i==3:
            j="Continue"
        else :
            if score_4_1<3:
                score_4_1+=1
            j="Try Again"
    score_4 += (4-score_4_1)*50
    print("Congrats! You have acquired all the information you need and you now take your leave \
from the lair.")
    print("Before leaving the lair, the Centaur also hands you a special anti-magic potion \
which can be used to remove any magical properties or spells on an object.")
    print("You may use that in case you ever have to defend yourself or solve a puzzle.")
    print("You thank the Centaur and leave.")
    score_4+=100
    a=input("Please press the enter key to continue.")
    return score_4

def chp_10():
    score_10=0
    print()
    print("CHAPTER X - THE BEGINNING OF THE END")
    print()
    
    # The Hangman Game
    
    print("As you finally approach the chest, you have to open it before the Wizard himself \
arrives.")
    print("This chest can only be unlocked by a certain keyword.")
    print("You have been provided with 2 hints to assist you.")
    a=input("Please press the enter key to continue.")
    print()
    print("Your 2 hints are -")
    print("1. The maker of this Copper Chest was a fan of the Wizarding World by J.K Rowling.")
    print("2. The password is the name of a particular spell used by Witches or Wizards.")
    a=input("Please press the enter key to continue.")
    print()
    print("You can guess the letters present in the word and if your guess is right \
the empty position will be filled by a letter.")
    print("You have 15 such guesses to fill the entire word, before the Wizard arrives and \
finds you.")
    
    score_10_1=0
    ae=0
    while ae<15 :
        import random as r
        ai={1:["a", "l", "o", "h", "o", "m", "o", "r", "a"],
            2:["e", "x", "p", "e", "c", "t", "o", "p", "a", "t", "r", "o", "n", "u", "m"],
            3:["a", "c", "c", "i", "o"],
            4:["e", "x", "p", "e", "l", "l", "i", "a", "r", "m", "u", "s"],
            5:["a", "v", "a", "d", "a", "k", "e", "d", "a", "v", "r", "a"]}
        aj=r.randint(1,5)
        ah=ai[aj]
        ak=[]
        ao="_"
        for aq in range(0,len(ah)):
            ak.append(ao)
        al=0
        while al==0 :
            am=str(input("Guess a letter for the word - "))
            ap=0
            for an in ah:
                if am==an:
                    ak[ap]=am
                ap=ap+1
            ae+=1
            if ae==15:
                break
            for ai in ak:
                print(" ".join(str(ai)), end=" ")
            if ah==ak:
                break
        if ae<15 :
            print()
            print("GREAT JOB! You figured out the code word you needed to open the Copper chest.")
            break
        else:
            if score_10_1<10:
                score_10_1+=1
            print("Oops, you didn't get it right.")
            print("The Wizard has now arrived and all hope is lost.")
            a=input("Please press the enter key to retry the puzzle.")
            print()
            ae=0
    score_10 += (11-score_10_1)*50
    print("Alas! You have successfully retrieved the Queen's Gem.")
    print("You to take the gem back to the Elf King and tell the truth about the Gem’s robbery.")
    print("The Viking and Centaur also support you and confirm your story.")
    a=input("Please press the enter key to continue.")
    print()
    print("The Elf King then agrees to release your friend, James from prison and \
orders the Evil Wizard to be exiled from the kingdom.")
    print("You and James peacefully return to your village.")
    score_10+=100
    a=input("Please press the enter key to continue.")
    return score_10

def chp_6():
    score_6=0
    print()
    print("CHAPTER VI - THE MIDNIGHT CRISIS")
    print()
    print("Now, the sun is starting to set and you need to find a place to spend the night.")
    print("Since, you are too far to go back home, go to a local Inn, where \
travellers often to seek shelter at night.")
    print("You pay for your room and decide to resume on your quest tomorrow dawn.")
    a=input("Please press the enter key to continue.")
    print()
    print("It is midnight, when you suddenly wake up from your sleep due to \
loud arguments at the Inn's door.")
    print("You go to the door and see the Inn's owner arguing with someone.")
    print("This someone is yet another traveller who has forgotten to bring \
money with himself for the Inn.")
    print("He is trying convince to owner to let him stay for the night, but \
the owner won't let him stay for free.")
    a=input("Please press the enter key to continue.")
    print()
    print("You are overcome by pity at the Traveller's plight and intervene \
to offer the last of your money to the owner to pay for his room.")
    print("The Traveller thanks you for your generosity and offers you five \
magic beans, which you accept.")
    print("He says that these beans are a highly valuable form of currency, \
exclusively used by the Viking kind.")
    print("At the next morning's dawn, you continue with your quest.")
    score_6+=100
    a=input("Please press the enter key to continue.")
    return score_6

def chp_7():
    score_7=0
    print()
    print("CHAPTER VII - HOW GOOD IS YOUR MATH?")
    print()
    print("Now, you come across a floating bridge which keeps appearing and disappearing \
and only gives passage to someone who can solve the ancient stone tablet's mystery.")
    print("It has an inscription that reads - ")
    print()
    print("To cross the bridge, you must be heard")
    print("Romans may help, to complete the words")
    print()
    print("Under this you find a short sentence with some missing letters - ")
    print("The har_est th_ng _n l_fe _s to learn wh__h br__ge to _ross an_ wh__h to burn.")
    a=input("Please press the enter key to continue.")
    print()
    
    # The Roman Numeral game
    
    score_7_1=0
    o=0
    while o!=2 :
        print("How will you try to solve this problem - ")
        print("Your options are -")
        print("1. Try to look for some other bridge")
        print("2. Try to fill Roman Numeral characters in the spaces")
        o=int(input())
        if o!=2 :
            if score_7_1<2:
                score_7_1+=1
            print("Wrong answer, please try again")
    score_7 += (3-score_7_1)*50
    print()
    print("You figured it out!")
    print("The inscription is a hint that instructs us how to cross the bridge.")
    print("You have to fill the spaces with Roman Numerals and read the sentence out aloud.")
    score_7_2=0
    x=0
    while x!=1 :
        def roman(num):
            val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
            sym = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
            r = ""
            p = 0
            while num > 0 :
                for q in range(num//val[p]):
                    r += sym[p]
                    num -= val[p]
                p += 1
            return r
        s=[]
        for t in range(1, 14):
            print("Enter the integer respective to the Roman numeral character \
for blank space no. ", t)
            u=int(input())
            v=roman(u)
            s.append(v)
        w=["D", "I", "I", "I", "I","I", "C", "I", "D", "C", "D", "I", "C"]
        if w==s :
            print("Amazing! You have solved yet another problem.")
            print()
            print("You read the sentence out aloud - The hardest thing in life is to learn \
which bridge to cross and which to burn - and the bridge appears for you to cross.")
            x=1
        else :
            if score_7_2<10:
                score_7_2+=1
            print("Incorrect answer please try again.")
    score_7 += (11-score_7_2)*50
    score_7+=100
    a=input("Please press the enter key to continue.")
    return score_7
    
def chp_8():
    score_8=0
    print()
    print("CHAPTER VIII - THE VIKING")
    print("Finally after crossing the bridge you reach a Tavern, where the Viking hangs out.")
    print("But now you have come across yet another obstacle.")
    a=input("Please press the enter key to continue.")
    print()
    print("You cannot enter the Tavern without the numerical password at the door.")
    print("The password is some number varying from 1 to 255.")
    print("After a while, you meet with an old man who knows the password.")
    a=input("Please press the enter key to continue.")
    print()
    print("But he can only answer in the specific words - HOT or COLD.")
    print("He will reply with - HOT, if your guess is closer to the password \
than your previous guess, else he will reply with - COLD.")
    print("You can guess the number 15 times before the password changes and \
you start over again.")
    a=input("Please press the enter key to start the game.")
    print()
    
    # HOT or COLD game
    
    score_8_1=0
    import random as ac
    z=0
    while z!=1 :
        y=ac.randint(1,255)
        ab=0
        aa=666
        ad=aa
        while aa!=y and ab<15:
            aa=int(input("Guess the password - "))
            ab+=1
            if aa==y :
                print("Good Job!!")
                z=1
            elif ab==15 :
                if score_8_1<3:
                    score_8_1+=1
                print("This is was your last guess, now the password will change and you will \
have to start over.")
            elif ab>1 and aa!=y :
                if abs(y-ad)>abs(y-aa) :
                    print("The old man replies - HOT")
                else :
                    print("The old man replies - COLD")
            else :
                print("You have made your first guess, now onwards the old man \
will reply with - HOT and COLD.")
            ad=aa
    score_8 += (4-score_8_1)*1000
    print("Your guess is right! The old man nods and walks away...")
    a=input("Please press the enter key to continue.")
    print()
    print("You can now go inside and talk to the Viking to know the whereabouts \
of the Missing Gem.")
    print("As you go inside the Tavern, you spot him sitting on a table.")
    print("You ask him about the whereabouts of the Missing Gem, which the \
Viking refuses to disclose.")
    a=input("Please press the enter key to continue.")
    print()
    print("You then remember about magic beans being a highly valuable currency \
to Vikings, and offer all 5 of those to him in exchange for the location.")
    print("Satisfied with the offer, he tells you to Lost Gem's location, where \
the Wizard had told him to hide for a couple of days.")
    print("He has hidden it inside a chest, at the very centre of the deadly Fanghorn forest.")
    print("Determined to save your friend, you head for the Fanghorn forest.")
    score_8+=100
    a=input("Please press the enter key to continue.")
    return score_8
    
def chp_9_A():
    score_9=0
    print()
    print("CHAPTER IX - WHAT GOES AROUND, COMES AROUND...")
    print()
    print("While travelling in the forest you encounter many strange looking creatures, \
but the Talisman you received from the retired Royal Guard keeps you safe.")
    
    # The Battle of the Beasts
    
    print("Suddenly, out of nowhere, a magical golem and a Basilisk, a beast \
that's half bird and half snake, jump in front of you.")
    print("You conclude them to have been sent by the Wizard, in order to stop you.")
    a=input("Please press the enter key to continue.")
    print()
    print("Fortunately, your Talisman again comes handy and protects you from the Basilisk.")
    print("But it does not protect you from the Golem, which is a supernatural creature.")
    score_9_1=0
    score_9_2=0
    ag=0
    while ag!=1 :
        print("You have to think fast and make a move before the Golem does...What do you do?")
        print("1. Try to outrun him and hide")
        print("2. Look for any useful items in your bag.")
        ae=int(input())
        if ae==1 :
            print("Smart thinking, what do you do next?")
            print("1. Wait until it goes away")
            print("2. Look for any useful items in your bag.")
            af=int(input())
            if af==2 :
                ag=1
            else :
                score_9_1+=1
                print("Trying to wait him out was a bad idea as the Golem never tires.")
                print("Eventually, you are spotted by him and caught.")
                print("Maybe try something else next time.")
                a=input("Please press the enter key to restart the fight.")
                print()
        else :
            score_9_2+=1
            print("You are grabbed by the Golem, before you could even open your bag.")
            print("Try hiding first next time.")
            a=input("Please press the enter key to restart the fight.")
    print("You find the anti-magic potion given to you by the Centaur.")
    print("You throw it at the Golem, who suddenly stops moving and becomes a regular stone \
statue, as the potion removes all its magical properties.")
    print("Finally you are safe now and head towards the Copper Chest sitting on an \
elevated platform.")
    score_9 += (4 - (score_9_2 + score_9_1))*50
    a=input("Please press the enter key to continue.")
    return score_9
                        
def chp_9_B():
    print()
    print("CHAPTER IX - WHAT GOES AROUND, COMES AROUND...")
    print()
    print("While travelling in the forest you encounter many strange looking creatures")
    print("This is a very dangerous forest filled with wild & savage beasts. Unfortunately, \
one way or the another, you fall prey to a deadly pack of wolves .")
    a=input("Please press the enter key to continue.")
    print()
    print("You regret not doing the side missions, for you may have found some help.")
    print("Now there's nothing you can do to avoid certain death, as you \
are slowly dragged into the dark abyss of the Fanghorn forest by a pack of Wolves.")
    print("KARMA got to you...")
    a=input("Please press the enter key to start at CHAPTER - V again.")

def chp_5():
    score_5=0
    k="No"
    while k=="No" :
        print()
        print("CHAPTER V - THE SIDE MISSION")
        print()
        print("As you are on your way to the Inn, you spot a small kid crying.")
        print("You approach her and come to know that she has lost her way back home.")
        print("As there is no one around, she turns to you for help. But strangely, you notice \
her wearing a rare locket, which is only given to the Royal Guards along with their uniform and \
their gear. You start having your doubts.....")
        print()
        print("It may be a trap or may not be a trap...")
        k=input("How do you respond to the kid's call ? Yes (to help) or No (to not help) ? - ")
        if k=="Yes" :
            score_5+=500
        
            # Find the Direction game
    
            print("You ask her which turns she took and after how much distance.")
            print("She replies - ")
            print()
            print("First she went straight for 100 m, after which she took three clockwise \
90⁰ turns and went straight for another 100 m.")
            print("Then she took another clockwise 90⁰ turn and went 100 m forward, \
lastly she took three anti-clockwise 90⁰ turns and went straight for 100 m.")
            print("Assuming her house to be North, in which direction and how much \
distance should she travel to reach home?")
            score_5_1=0
            n=0
            while n!=1 :
                l=input("Direction - ")
                m=input("Distance in m - ")
                if l=="South" and m=="200" :
                    n=1
                else :
                    if score_5_1<5:
                        score_5_1+=1
                    print("Wrong answer, try again.")
            score_5 += (6-score_5_1)*50
            print()
            print("Congratulations, after having correctly figured out the right path \
, you offer to walk her back home.")
            print("You finally reach her home and meet her worried father, an old retired \
Royal Guard who used to work at the King's palace. He had given the locket to her when he had \
retired.")
            print("He is very grateful to you for helping his child and gives you a Golden \
Talisman, as a token of appreciation.")
            print("This magical Talisman, will grant you a safe passage in any forest you \
travel, as no animal will be able to harm this Talisman's wearer.")
            print("You thank him and return back to your main quest.")
            a=input("Please press the enter key to continue.")
            score_5+=100
            
            chp5=score_5
            chp6=chp_6()
            chp7=chp_7()
            chp8=chp_8()
            chp9=chp_9_A()
            
            return (chp5 + chp6 + chp7 + chp8 + chp9)
            
        else :
            print("You leave the kid to itself, believing it to be a trap as a mere child could \
never have access to the locket")
            a=input("Please press the enter key to continue.")
            
            chp_6()
            chp_7()
            chp_8()
            chp_9_B()

# Game Begins

def Game():
    print()
    print("This is an epic Fantasy-Adventure game developed by Jai Singh")
    name=input("Please enter your unique Gamer ID - ")
    print()
    print("Now the game begins...")
    a=input("Please press the enter key to begin.")

    chp1=chp_1()
    chp2=chp_2()
    chp3=chp_3()
    chp4=chp_4()
    chp56789=chp_5()
    chp10=chp_10()        
    tscore = chp1 + chp2 + chp3 + chp4 + chp56789 + chp10
    
    print()
    print("Sadly, the game ends here...")
    print("Thank you for playing.")
    
    return name, tscore
    
def save():
    import csv as ar
    with open("scores.txt", mode="a") as av:
        bc = ar.writer(av)
        bc.writerow(bb)
    av.close()

def search():
    import csv as au
    with open("scores.txt", mode="r") as aw:
        ax=au.reader(aw)
        ay=input('Enter player name to search - ')
        az=0
        for ba in ax:
            if len(ba)==0:
                pass
            else:
                if ba[0]==ay:
                    print(ba[0], 'has scored', ba[1])
                    az+=1
        if az==0:
            print('No record found')
    aw.close()

def highscore():
    import csv as bd
    with open("scores.txt", mode="r") as be:
        bf=bd.reader(be)
        bh=0
        bi=''
        for bg in bf:
            if len(bg)==0:
                pass
            else:
                if int(bg[1])>int(bh):
                    bh=bg[1]
                    bi=bg[0]
        print(bi, "has the highest score as", bh)
    be.close()

while True:
    print()
    print("Welcome! PLease select any one of the following options - ")
    print("\n 1. Play game \n 2. View highest score \n 3. View score of a particular player \
\n 4. Exit")
    print()
    bd=int(input())
    if bd==1:
        bb = list(Game())
        save()
    elif bd==2:
        highscore()
    elif bd==3:
        search()
    else:
        break






