class EventManager(object):
    def __init__(self):
        self.events = []

    def add(self, event):
        self.events.append(event)

    def showEvents(self) -> str:
        print(self.events, "\n")
        return "\n".join([str(event) for event in self.events])

    def addEvent(self, titre, date, heure, description=""):
        self.events.append([titre, date, heure, description])

    def editEvent(self, titreOriginal, titreTarget):
        self.events[self.events.index(titreOriginal)] = titreTarget

    def deleteEvent(self, titre):
        self.events.remove(titre)

    def menu(self):
        print("Menu :")
