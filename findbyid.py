import random

class FindByIDFactory:
    def __init__(self, *args, **kwargs):
        cls = type(self)
        if not hasattr(cls, "has_instantiated"):
            cls.instances = []
            cls.has_instantiated = True

        self.ID = cls.getFreeID()
        cls.instances.append(self)

    @classmethod
    def getFreeID(cls):
        # biggest = 0
        #
        # for i in cls.instances:
        #     if i.ID > biggest:
        #         biggest = i.ID
        #
        # return biggest + 1
        return random.randint(10000, 100000)

    @classmethod
    def findByID(cls, ID):

        for i in cls.instances:
            if i.ID == ID:
                return i
        else:
            raise Exception("Invalid ID!")

    @classmethod
    def getInstances(cls):
        return cls.instances
    
