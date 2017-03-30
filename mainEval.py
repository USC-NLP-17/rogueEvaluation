import fileinput
ref_folder_location = 'C:\\Users\\amitjha\\Desktop\\output\\human_output\\'
machine_folder_location = 'C:\\Users\\amitjha\\Desktop\\output\\machine_output\\'
scoreList = []
#create class to hold counters
class Score:
    def __init__(self,id):
        self.id = id
        self.pre = 0
        self.rec = 0
        self.f1 = 0
        self.match = 0

l = []

def buildList(fileN):
    filePointer = open(fileN, 'r', encoding='utf-8')
    s = '$'
    for refSumLine in filePointer:
        refSumLine = refSumLine.strip()
        s = s + refSumLine
    s = s.strip('$')
    listVal = s.split(u'\u0964')
    return listVal


inputCountS = input("Enter No. of Input files: ")
inputCount = int(inputCountS)
for i in range(1,inputCount+1,1):
    machinFile = 'machine' + str(i)+'.txt'
    refFile = 'output' + str(i) + '.txt'
    machinFile = machine_folder_location + machinFile
    refFile = ref_folder_location + refFile
    #open ref
    refList = buildList(refFile)
    machineList = buildList(machinFile)
    if len(machineList) <= 0 or len(refList) <= 0:
        continue
    matchSet = set(refList) & set(machineList)
    matchCount = len(matchSet)
    #create object
    o = Score(i)
    o.match = matchCount
    o.pre =  o.match / len(machineList)
    o.rec = o.match / len(refList)
    o.f1 = 2 * ((o.pre * o.rec) / (o.pre + o.rec))
    scoreList.append(o)
s = 0
print("ID  =>  F1 Score")
for i in scoreList:
    s += i.f1
    strO = str(i.id) +' =>  ' + str(i.f1)
    print(strO)
avgFScore = s/len(scoreList)
print("\n\nTotal Avg. F1 Score => " + str(avgFScore))
#print(avgFScore)

