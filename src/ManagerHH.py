from src.hhabc import ManagerHHAbstract


class VacancyHH(ManagerHHAbstract):
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
        salary_from, salary_to = self.salary.split('-')
        if salary_to != 'None' and salary_from != 'None':
            return (int(salary_to) + int(salary_from) / 2) <= (int(other.salary_to) + int(other.salary_from) / 2)
        elif salary_to == 'None' and salary_from != 'None':
            return int(salary_from) <= int(other.salary_from)
        elif salary_to != 'None' and salary_from == 'None':
            return int(salary_to) <= int(other.salary_to)
        else:
            return int(salary_to) <= int(other.salary_to)


    def __lt__(self, other):
        """
        метод для операции сравнения «больше или равно»
        """
        salary_from, salary_to = self.salary.split('-')
        if salary_to != 'None' and salary_from != 'None':
            return (int(salary_to) + int(salary_from) / 2) < (int(other.salary_to) + int(other.salary_from) / 2)
        elif salary_to == 'None' and salary_from != 'None':
            return int(salary_from) <= int(other.salary_from)
        elif salary_to != 'None' and salary_from == 'None':
            return int(salary_to) <= int(other.salary_to)
        else:
            return int(salary_to) <= int(other.salary_to)

