import abc

class Base(metaclass=abc.ABCMeta):
    
    @abc.abstractclassmethod
    def fit(self):
        NotImplemented

    @abc.abstractclassmethod
    def transform(self):
        NotImplemented
    

class Search(Base):
    def __init__(self):
        print(self.__class__)
    
    @abc.abstractclassmethod
    def fit(self):
        NotImplemented

    @abc.abstractclassmethod
    def transform(self):
        NotImplemented
    

