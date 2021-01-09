def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):

    def createZeroArray(timeunit):
        a=[0]
        return a*timeunit

    def returnTimeIndices(array):
        starthrs, startmin=array[0].split(":")
        endhrs,endminutes=array[1].split(":")

        Intstarth=int(starthrs)
        Intstartm=int(startmin)
        Intendh=int(endhrs)
        Intendm=int(endminutes)

        IndexStart=Intstarth*60+Intstartm
        IndexEnd=Intendh*60+Intendm

        return IndexStart, IndexEnd

    def createBinaryTimeSLots(array, IndexStart, IndextEnd):

        for idx, i in enumerate(array):
            if idx>=IndexStart and idx <=IndextEnd:#idx needs to be between Start and End
                array[idx]=1
        return array

    def BlockArrayForDailyBound(array, dailyBounds1):
        BeforeisBlockedhrs, BeforeisBlockedhrsmin=dailyBounds1[0].split(":")
        AfterisBlockedhrs,AfterisBlockedhrsmin=dailyBounds1[1].split(":")

        Intstarth=int(BeforeisBlockedhrs)
        Intstartm=int(BeforeisBlockedhrsmin)
        Intendh=int(AfterisBlockedhrs)
        Intendm=int(AfterisBlockedhrsmin)

        IndexStart=Intstarth*60+Intstartm
        IndexEnd=Intendh*60+Intendm

        for idx, i in enumerate(array):
            if idx<=IndexStart or idx>=IndexEnd:
                array[idx]=1
        return array


    Person1TT=createZeroArray(1441)#Minutes per Day
    Person2TT=createZeroArray(1441)

    #Person1

    for TP1 in calendar1:
        idxS, idxE=returnTimeIndices(TP1)
        createBinaryTimeSLots(Person1TT, idxS, idxE)
    BlockArrayForDailyBound(Person1TT,dailyBounds1)
    print(Person1TT)

    for TP2 in calendar2:
        idxS, idxE=returnTimeIndices(TP2)
        createBinaryTimeSLots(Person2TT, idxS, idxE)
    BlockArrayForDailyBound(Person2TT,dailyBounds2)
    print(Person2TT)

    def createCadidatesTimeSLots(array1, array2):
        availableTimeSlots=[0]*1441
        for idx, i in enumerate(availableTimeSlots):
            if array1[idx] ==1 or array2[idx]==1:
                availableTimeSlots[idx]=1
        return availableTimeSlots

    AvailTT=createCadidatesTimeSLots(Person1TT, Person2TT)
    print(AvailTT)
    def createMeetingMask(meetingDuration):
        #meetingDuration is integer
        return [0]*(meetingDuration-1)



    MeetingMask=createMeetingMask(meetingDuration)
    limit=len(MeetingMask)
    res=[]
    super=0
    for idx, i in enumerate(AvailTT[:-limit]):
        cnt=0
        for jdx, j in enumerate(MeetingMask):
            if MeetingMask[jdx]==AvailTT[idx+jdx]:
                cnt+=1
                if cnt>=limit:
                    super+=1

            else:
                if super>0:
                    res.append([idx+jdx-limit-super,idx+jdx])
                    super=0
                break

    #print(res)

    timeslots=[]
    for i in res:
        begin=i[0]
        timeslots.append([begin, i[1]])
    #print("timeslots ", timeslots)

    def makeTimeSLotsToString(timeSlotsvar):
        def makeMilitaryTime(idx):
            hrs,min=divmod(idx,60)
            return hrs,min
        sol=[]
        for i in timeSlotsvar:
            print("i ", i)
            starth,startm=makeMilitaryTime(i[0])
            endh, endm=makeMilitaryTime(i[1])
            if startm<10:
                startm="0"+str(startm)
            if endm<10:
                endm="0"+str(endm)
            IStartsol=str(starth)+":"+str(startm)
            IEndsol=str(endh)+":"+str(endm)
            sol.append([IStartsol, IEndsol])
        return sol

    res=makeTimeSLotsToString(timeslots)

    return res
