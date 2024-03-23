from constants import X, L, ALPHA, DELTA
import math


class User:
    _counter = 0

    def __init__(self, speed, clock, generator1, generator2):
        User._counter += 1
        self.id = User._counter
        self.speed = 80
        self.station = 1
        self.distance = X
        self.powerBS1 = generator1
        self.powerBS2 = generator2
        self.handoverTime = 0
        self.timeReport = clock
        self.CounterSwitches = 0
        self.DistanceSwitches = 0.0

    def updatePower(self, generator1, generator2):
        self.powerBS1 = 4.56 - 22 * math.log10(self.distance) + generator1
        self.powerBS2 = 4.56 - 22 * math.log10(L - self.distance) + generator2

    def updatePosition(self):
        self.distance += self.speed / 50

    def updateReportTime(self):
        self.timeReport = self.timeReport + 20

    def checkSwitchStation(self):
        if self.station == 1:
            if self.powerBS1 - self.powerBS2 <= -ALPHA: return True
        elif self.station == 2:
            if self.powerBS2 - self.powerBS1 <= -ALPHA: return True
        return False

    def checkDeleteUser(self):
        return self.distance > L - X

    def checkDisconnectUser(self):
        if self.station == 1:
            if self.powerBS1 - self.powerBS2 <= -DELTA: return True
        elif self.station == 2:
            if self.powerBS2 - self.powerBS1 <= -DELTA: return True
        return False
