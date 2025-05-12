#Made by Mashal159 in august 2022


def inputcheck(x):          #check if the user enters the input or not
    while x == "":
        x = input("please enter the required opject: ")
    return x

def intcheck(x):            #check if the input is numeric or not

    while not x.isnumeric():
        x = input("please enter number: ")
    return int(x)
    
# making class for candidates to store their name and number of votes and their elimination state
class candidate():                    
    def __init__(self,name,VoteNum=0,eliminated=False):
        self.name = name
        self.VoteNum = int(VoteNum)
        self.eliminated = eliminated
    def __str__(self):
        return self.name
    def get_name(self):
        return self.name
    def set_VoteNum(self):
        self.VoteNum = self.VoteNum+1
    def get_votes(self):
        return self.VoteNum
    def elimination(self):
        return self.eliminated
    def eliminat(self):           #to eliminate candidate
        self.eliminated = True
    def zeroing000(self):         #to make number of votes of the candidate 0
        self.VoteNum = 0 
   

def getCandidates():
            #take the number of candidates from the user
    cand_num = inputcheck(intcheck(input("enter number of candidates: ")))
    
    cand_list=[]     #empty list to store the candidates
    
    candNames=[]     #empty list to store names of candidates
    
    #loop to make candidates from from user as class candidate in list of candidates
    for i in range(cand_num):
        while True:
            x=inputcheck(input(f"enter candidate No. {i+1}: ")).lower()
            cand = candidate(x)
            if x in candNames:    #chek if the choosen candidate is choosen before or not
                print("enter another candidate")
            else:
                candNames.append(x)         #store name of candidates
                cand_list.append(cand)      #store candidate class opjects
                break
    return cand_list
#function to get preferences from each voter
def votingProsses(cand_list,votersNum):
    votinglist=[]         # empty list to store the preferences
    #loop to store list of prefrances of each voter in a biger list
    for i in range(votersNum):
        print("")
        print(f"voter number {i+1}: ")
        list2=[]      #empty list to store preferences of each voter
        #loop of storing preferences in ballot
        for j in range(len(cand_list)):
            x = inputcheck(input(str(j+1) + ". ").lower())  #get each preference
            for i in cand_list:
                check = False
                if x == i.get_name() and x not in list2:   #check if the input is one of the candidates 
                    check = True
                    break
            if check:       #check if the vote is valid or not to store it 
                list2.append(x)
            else:
                print("invalid vote ")
                break
        if check:           #check if the ballot is valid or not to store it
            votinglist.append(list2)
    return votinglist
    
    
def removeFromBallots(cand_list,votinglist):    
    for i in range(len(votinglist)):   
        for j in cand_list:  #loob in candidates list 
            for k in votinglist[i]:      #loob in each ballot
                if j.get_name() == k:     #check the name of candidate
                    if j.elimination():
                        votinglist[i].remove(k)    #remove eleminated candidates votes from ballot
                else: break   
    return votinglist
    
def countvots(cand_list,votinglist):
    for i in votinglist:   
        for j in cand_list:  #loob in candidates list to increase number of votes of the voted candidate 
                if j.get_name() == i[0]:     #check the name of candidate
                    j.set_VoteNum()
                    break    #remove eleminated candidates votes from ballot        
            


#function to check if there is a winner
def winner(list,votinglist): 
    check = False
    for i in list:
        if (i.get_votes()/len(votinglist)) > 1/2 or i.get_votes()==len(votinglist):
            print(" ")
            print(i," is winnerrrrrrrrrr")
            print(" ")
            print(" ")
            print(" ")
            check = True
        
    return check


#function to check if their is tie and if not return minimum votes 
def find_max_min(cand_list):
    max = 0
    min =  1000000000
    #loob to max and min number of votes
    for i in cand_list:
        if i.get_votes() > max:
            max=i.get_votes()
    for i in cand_list:        
        if i.get_votes()<min and i.get_votes()!=0 :
            min = i.get_votes()
    return [max,min]
#make list to max and min candidates
def max_min_lists(max,min):
    maxList = []
    minList = []
    for i in cand_list:
        if i.get_votes() == max:
            maxList.append(i)  
        if i.get_votes() == min :
            minList.append(i)
    return [maxList,minList]

#check if their is tie
def is_tie(maxList,minList,cand_list,max,min,votersnum):
    list  =removeEliminated(cand_list)
    for i in cand_list:
        if i.get_votes()==min:
            x = True
        else:
            x = False
    nonzeroCand_list = removeZeros(cand_list)
    if (x) or maxList == nonzeroCand_list or (max==votersnum and len(maxList)!=0):
        return [True,list]
    else:
        return [False]

#eliminat the minimum candidates
def eliminationProsses(cand_list,max,min):
    if min!=max:
        for i in cand_list:
            if i.get_votes()==min:
                i.eliminat()

#remove eliminated from list of candodates    
def removeEliminated(cand_list):       
    newlist = []
    for i in cand_list:
        newlist.append(i)
        if i.elimination():
            newlist.remove(i)
    return newlist
    
#turn candidates into 0 votes
def turn_into_zeros(list):
    for i in list:
        i.zeroing000()

#remove candidates whith 0 votes
def removeZeros(cand_list):
    newlist = []
    for i in cand_list:
        if i.get_votes()!=0: newlist.append(i)
    return newlist


print("read requirments carfully")
#loob of the whole program
while True:
    cand_list = getCandidates()
    print("  ")
    #get number of voters from user    
    votersNum= inputcheck(intcheck(input("enter voters number: ")))  
    #loob of voting and counting
    while True :
        cand_list = removeEliminated(cand_list)
        votinglist  =  votingProsses(cand_list,votersNum)
        if len(votinglist) == 0:
            print(" ")
            print("no winners")
            for i in renge(3):print("  ")
            break
        check = False     #follow up winner case
        #loob of counting and geting feedbacks
        while True:
            turn_into_zeros(cand_list)    #turn candidates into 0 votes
            votinglist  = removeFromBallots(cand_list,votinglist)    
            countvots(cand_list,votinglist)  #counting votes
            if check:      #check=true if their is winner in the loob
                break #their is winner
            else:
                #check tie
                maxminlist = find_max_min(cand_list)   
                listmaxmin = max_min_lists(maxminlist[0],maxminlist[1])
                checklist = is_tie(listmaxmin[0],listmaxmin[1],cand_list,maxminlist[0],maxminlist[1],len(votinglist))
                
                if not checklist[0]: #checklist[o] follw up tie case
                    check = winner(cand_list,votinglist)    
                    if check:
                        break #ther is winner
                    eliminationProsses(cand_list,maxminlist[0],maxminlist[1])
                else:
                    eliminationProsses(cand_list,maxminlist[0],maxminlist[1])
                    removeFromBallots(cand_list,votinglist)
                    nozero = removeEliminated(cand_list)
                    turn_into_zeros(cand_list)
                    votinglist  = removeFromBallots(cand_list,votinglist)
                    countvots(cand_list,votinglist)  #counting votes
                    nozero = removeZeros(nozero)
                    check = winner(cand_list,votinglist)
                    if check :break  #teir is winner
                    #a loob will print tied candidates if their is ni winner 
                    for i in nozero:
                        print(i,end = "    ")     #printing tied candidates
                    print("tie")
                    eliminationProsses(cand_list,maxminlist[0],maxminlist[1])
                    cand_list = nozero
                    break   
        if check:
            break
    
    new = input("if you want to make another election write Yes if not اكتب اي حاجه و خلصني:   ").lower()
    if new != "yes":
        break
    
