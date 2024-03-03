import json

from src.vacancy import Vacancy


class VacancyFileStorage:
    def add_vacancy_to_file(self, vacancy):
        """
        Добавляет новую вакансию в файл.
        Args:
            self: экземпляр класса.
            vacancy: Объект вакансии.
        """
        with open('vacancies.json', 'w') as file:
            data = json.load(file)
            data['vacancies'].append({
                'title': vacancy.title,
                'link': vacancy.link,
                'salary': vacancy.salary,
                'currency': vacancy.currency,
                'text': vacancy.text,
                'requirements': vacancy.requirements
            })
            file.seek(0)
            json.dump(data, file, indent=4)

    def get_vacancies_from_file(self, criteria):
        """
        Извлекает и возвращает список вакансий из файла на основе заданных критериев.
        :param criteria: dict - словарь с критериями.
        :return: List - список вакансий.
        """
        pass

    def remove_vacancy_from_file(self, vacancy):
        """
        Удаляет вакансию из файла.
        :param vacancy: Вакансия для удаления
        :return: None
        """
        pass


class JSONFileStorage(VacancyFileStorage):
    def add_vacancy_to_file(self, vacancy: Vacancy) -> None:
        """
        добавляет новую вакансию в файл.
        Parameters:
            self (obj): экземпляр класса.
            vacancy (obj): объект вакансии.
        Returns:
            None
        """
        with open('vacancies.json', 'w', encoding='utf-8') as file:
            data = json.load(file)
            data['vacancies'].append()
            json.dump(data, file, indent=4)

    def get_vacancies_from_file(self, criteria):
        """
        извлекает и возвращает список вакансий из файла на основе заданных критериев.
        :param criteria: dict - словарь с критериями.
        :return: List - список вакансий.
        """
        with open('vacancies.json', 'r') as file:
            data = json.load(file)
            return data

    def remove_vacancy_from_file(self, vacancy):
        """
        Удаляет вакансию из файла.
        :param vacancy: Вакансия для удаления
        :return: None
        """
        with open('vacancies.json', 'r+') as file:
            data = json.load(file)
            data['vacancies'] = [v for v in data['vacancies'] if v['title'] != vacancy.title]
            file.seek(0)
            json.dump(data, file, indent=4)
