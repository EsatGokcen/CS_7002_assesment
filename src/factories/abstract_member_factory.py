from abc import ABC, abstractmethod

class MemberFactory(ABC):

    @abstractmethod
    def create_member(self, *args):
        pass