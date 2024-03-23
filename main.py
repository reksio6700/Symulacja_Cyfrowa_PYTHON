from User_queue import Queue
import generators

seeds = None
with open("seeds.txt", 'r') as Seed:
    seeds = [int(line.strip()) for line in Seed]


def main(TTT, LAMBD, maxDeletedUser, DataStart, seedSetNumber):
    GaussGen1 = generators.GaussianGenerator(seed=seeds[seedSetNumber])
    GaussGen2 = generators.GaussianGenerator(seed=seeds[seedSetNumber + 10])
    ExpGen = generators.ExponentialGenerator(seed=seeds[seedSetNumber + 20], lambd=LAMBD)
    UniGen = generators.UniformGenerator(seed=seeds[seedSetNumber + 30])



    CounterOfDisconneced = 0
    CounterOfSwitches = 0
    CounterDistance = 0.0
    ServedUsers = 0

    ActiveReport = False  # flaga
    CurrentReport = None
    UserQueue = Queue()
    UserQueue.createUser(UniGen.uniformGenerator(), 0.0, GaussGen1.gaussianGenerator(),
    GaussGen2.gaussianGenerator())  # tworzenie pierwszego użytkownika
    timeCreateNextUser = ExpGen.exponentialGenerator()  # czas tworzenia nowego użytkownika
    timeRaportUser = min(UserQueue.usersList, key=lambda user: user.timeReport).timeReport
    while ServedUsers < maxDeletedUser + DataStart:
        # ustawienie czasu systemu
        if timeCreateNextUser <= timeRaportUser:
            CLOCK = timeCreateNextUser
        else:
            CLOCK = timeRaportUser

        # Zdarzenie czasowe - tworzenie nowego użytkownika
        if CLOCK == timeCreateNextUser:
            UserQueue.createUser(UniGen.uniformGenerator(), CLOCK, GaussGen1.gaussianGenerator(),
                                 GaussGen2.gaussianGenerator())
            timeCreateNextUser = CLOCK + ExpGen.exponentialGenerator()

        # Zdarzenie czasowe - raport użytkownika
        if CLOCK == timeRaportUser:
            CurrentReport = min(UserQueue.usersList, key=lambda user: user.timeReport)
            CurrentReport.updatePower(GaussGen1.gaussianGenerator(), GaussGen2.gaussianGenerator())
            ActiveReport = True

        # Zdarzenie warunkowe - usunięcie użytkownika przez dystans
        if ActiveReport and CurrentReport.checkDeleteUser():
            if ServedUsers >= DataStart:
                CounterOfSwitches += CurrentReport.CounterSwitches
                CounterDistance += CurrentReport.DistanceSwitches
                #with open("results2.txt", 'a') as file:
                    #file.write(str(len(UserQueue.usersList )+UserQueue.waitQueue.qsize()) +"\n")

            UserQueue.deleteUser(CurrentReport, CLOCK)
            ServedUsers += 1
            ActiveReport = False

        # Zdarzenie warunkowe - rozłączenie użytkownika
        if ActiveReport and CurrentReport.checkDisconnectUser():
            if ServedUsers >= DataStart:
                CounterOfSwitches += CurrentReport.CounterSwitches
                CounterDistance += CurrentReport.DistanceSwitches
                CounterOfDisconneced += 1
                #with open("results2.txt", 'a') as file:
                    #file.write(str(len(UserQueue.usersList)+ UserQueue.waitQueue.qsize())  + "\n")

            UserQueue.deleteUser(CurrentReport, CLOCK)
            ServedUsers += 1
            ActiveReport = False

        # Zdarzenie warunkowe - przełączenie stacji
        if ActiveReport and CurrentReport.checkSwitchStation():
            CurrentReport.handoverTime += 20
            if CurrentReport.handoverTime == TTT + 20:
                if CurrentReport.station == 1:
                    CurrentReport.station = 2
                elif CurrentReport.station == 2:
                    CurrentReport.station = 1
                CurrentReport.handoverTime = 0
                if ServedUsers >= DataStart:
                    CurrentReport.CounterSwitches += 1
                    CurrentReport.DistanceSwitches += CurrentReport.distance

        elif ActiveReport and not CurrentReport.checkSwitchStation() and CurrentReport.handoverTime != 0:
            CurrentReport.handoverTime = 0

        if ActiveReport:
            CurrentReport.updateReportTime()
            CurrentReport.updatePosition()
            timeRaportUser = min(UserQueue.usersList, key=lambda user: user.timeReport).timeReport
            ActiveReport = False

    with open("results.txt", 'a') as file:
        file.write("Wartość TTT = " + str(TTT) + " zestaw seed: " + str(seedSetNumber) + "\n")
        file.write("Rozłączenia = " + str(CounterOfDisconneced) + "\n")
        file.write("Przełączenia = " + str(CounterOfSwitches) + "\n")
        file.write("Dystans przełączeń = " + str(CounterDistance) + "\n")


#for i in range(120, 180, 20):
for j in range(0, 10):
    main(TTT=60, LAMBD=0.0011, maxDeletedUser=500, DataStart=66, seedSetNumber=j)
