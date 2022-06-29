#Lince Rumainum
#ISE5123
#HW2 Problem 1
#stats.py

#FUNCTIONS:
# calculate median
def median (inputList):
    # calculate median
    if (len(inputList) > 0):
        #length of list
        listLen = len(inputList)
        #sort the list
        inputList.sort()

        if listLen % 2 != 0:# list with odd length
            medNum = inputList[int(listLen/2)]
        else: # list with even length
            #get the two middle numbers            
            leftNum = inputList[ int(listLen/2) - 1]            
            rightNum = inputList[int(listLen/2)]
            #calculate the median
            medNum = (leftNum + rightNum) / 2
        return medNum #return median
    # no input
    else:
        return 0

def mode (inputList):
    # calculate mode
    if (len(inputList) > 0):
        # length of list
        listLen = len(inputList)
        # create dictionary for each unique number and its count
        countNumDict = {num:inputList.count(num) for num in inputList}
    
        #initialize list of modes indices
        modeList = []
        
        countList = list(countNumDict.values())
        #initialize the current mode to the first item on the list
        currMode = countList[0]
        
        #find mode through the list in dict
        for i in range(1,len(countList)):
            currNum = countList[i]
            #update mode
            # new mode found
            if currNum > currMode:
                # update to empty list again just in case it was filled
                modeList = []
                # append the new index
                modeList.append(i)
                currMode = currNum
            # same count of the current index and mode's index
            elif  currNum == currMode:
                if len(modeList) == 0:
                    # add the first mode
                    modeList.append(0)
                    # add the next mode
                    modeList.append(i)
                else:
                    #update mode
                    modeList.append(i)
                currMode = currNum
                
        # update if first number on dict is the mode            
        if len(modeList) == 0:
            modeList.append(0)
        
        # get actual modes from the key on dict
        modes = []
        keysList = list(countNumDict.keys())
        for j in range(len(modeList)):
            modes.append(keysList[modeList[j]])

        return modes
    # no input
    else:
        return 0

def mean (inputList):
    # calculate mean
    if (len(inputList) > 0):
        #length of list
        listLen = len(inputList)
        #initialize sum
        sum = 0

        # calculate sum of the list
        for i in range(0,listLen):            
            sum += inputList[i]        
        return round(sum/listLen, 2)
    # no input
    else:
        return 0

def standardDeviation (inputList):
    # calculate standardDeviation
    if (len(inputList) > 0):
        # length of list
        listLen = len(inputList)
        
        #get the mean
        aveList = mean(inputList)
        #initialize summation
        sum = 0
        #calculate summation part of standard deviation
        for i in range(listLen):
            sum += (inputList[i] - aveList) ** 2
        #calculate the standard deviation    
        stdDev = round((sum / listLen) ** 0.5, 3)
        
        return stdDev

        
    # no input
    else:
        return 0