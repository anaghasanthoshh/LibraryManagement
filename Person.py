from abc import ABC,abstractmethod
class Person(ABC):
    def __init__(self,first_name,last_name,address,phone,memberId):
            self.first_name = first_name
            self.last_name = last_name
            self.address = address
            self.phone = phone
            self.memberId=memberId


    @abstractmethod
    def get_info(self):
        pass

