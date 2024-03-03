from abc import ABC

from src.hhabc import ManagerHHAbstract


class Vacancy(ManagerHHAbstract, ABC):
    def __init__(self, name_vacancy, link_vacancy, salary, curency, text, requirement):
        self.name_vacancy = name_vacancy
        self.link_vacancy = link_vacancy
        self.salary = salary
        self.curency = curency
        self.text = text
        self.requirement = requirement

    def __le__(self, other):
        """
        метод для операции сравнения «меньше или равно»
        """
        try:
            salary_from, salary_to = self.salary.split('-')
            salary_from_other, salary_to_other = other.salary.split('-')
            if salary_to != 'None' and salary_from != 'None':
                return (int(salary_to) + int(salary_from) / 2) <= (int(salary_to_other) + int(salary_from_other) / 2)
            elif salary_to == 'None' and salary_from != 'None':
                return int(salary_from) <= int(salary_from_other)
            elif salary_to != 'None' and salary_from == 'None':
                return int(salary_to) <= int(salary_to_other)
            else:
                return int(salary_to) <= int(salary_to_other)
        except:
            return

    def __lt__(self, other):
        """
        метод для операции сравнения «больше или равно»
        """
        try:
            salary_from, salary_to = self.salary.split('-')
            salary_from_other, salary_to_other = other.salary.split('-')
            if salary_to != 'None' and salary_from != 'None':
                return (int(salary_to) + int(salary_from) / 2) < (int(salary_to_other) + int(salary_from_other) / 2)
            elif salary_to == 'None' and salary_from != 'None':
                return int(salary_from) < int(salary_from_other)
            elif salary_to != 'None' and salary_from == 'None':
                return int(salary_to) < int(salary_to_other)
            else:
                return int(salary_to) < int(salary_to_other)
        except:
            return
