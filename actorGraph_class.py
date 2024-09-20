from actor_class import Actor

class ActorGraph:
    def __init__(self, corpus):
        #initialisation of dictionary that will store all shows. They keys are the IDs, the values are Show objects.
        self.actors = {}
        #Load the actor corpus
        for data_actor in corpus:
            self.actors[data_actor.id]=data_actor

    def __iter__(self):
        for actor in self.actors.values():
            yield actor

    def buildRelations(self):
        for actor in self:
            actor.computerelations(self)