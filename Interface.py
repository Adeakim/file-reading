from abc import ABC,abstractmethod


class Interface(ABC):
    @abstractmethod
    def open_file(self):
        pass
    
    @abstractmethod
    def iterate_file(self):
        pass
    
    @abstractmethod
    def read_whole_content(self):
        pass
    
    @abstractmethod
    def read_first_two_lines(self):
        pass
    
    @abstractmethod
    def read_last_two_lines(self):
        pass
    
    