from abc import ABC, abstractmethod


class ManagerHHAbstract(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class ManagerFile(ABC):
    @abstractmethod
    def safe_vacancies(self, file_path):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass
