from abc import ABC, abstractmethod

class MemberFactory(ABC):

    @abstractmethod
    def create_member(self, name: str, email: str, health_info: str):
        pass