import json
class Actor:
    def __init__(self, id, name, birthday, charName):
        self._id = id
        self.name = name
        self.birthday = birthday
        self.charName = charName
        self.shows = []
        self.relations = {}

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    def append(self, show):
        assert isinstance(show, dict)
        self.shows.append(show)

    def __iter__(self):
        for show in self.shows:
            yield show
    
    def __contains__(self, show):
        if show in self.shows:
            return True
        else:
            return False

    # This is to remove duplicates
    def __eq__(self, other):
        return self.id==other.id
        
    def __hash__(self):
        return hash(('id', self._id))

    def __str__(self):
        return f'The actor {self.name}({self._id}) is in shows: {json.dumps(self.shows)}'

    def addrelation(self, actorID):
        #show must not be empty, and must not be the show itself
        if actorID and actorID != self._id:
            #the show is already in our relations, strengthen the bond:
            if actorID in self.relations:
                self.relations[actorID] += 1
            #the show is not in our relations, create a new bond:
            else:
                self.relations[actorID] = 1


    def computerelations(self, graph):
        for actor in graph:
            for show in actor:
                if show in self.shows:
                    self.addrelation(actor._id)

    def printRelations(self):
        for actorId, weight in self.relations.items():
            print(f"with actor {actorId}: {weight}")

    def getStrength(self):
        return sum(self.relations.values())
    