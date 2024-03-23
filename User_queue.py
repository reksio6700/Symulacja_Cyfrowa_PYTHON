import queue
import constants
from user import User


class Queue:
    def __init__(self):
        self.usersList = []
        self.waitQueue = queue.Queue()

    # dodawanie użytkownika
    def createUser(self, speed, clock, generator1, generator2):
        user = User(speed, clock, generator1, generator2)
        if len(self.usersList) < constants.maxUsers:  # dodanie do odpowiedniej struktury danych
            self.usersList.append(user)
            return user
        else:
            self.waitQueue.put(user)
            return user

    # usuwanie użytkownika oraz jeśli to możliwe dodanie użytkownika do aktywnych
    def deleteUser(self, User, clock):
        self.usersList.remove(User)
        if (self.waitQueue.qsize() > 0 and len(
                self.usersList) < constants.maxUsers):  # sprawdzenie czy nie ma użytkownika w drugiej kolejce
            self.usersList.append(self.waitQueue.get())
            self.usersList[-1].timeReport = clock
