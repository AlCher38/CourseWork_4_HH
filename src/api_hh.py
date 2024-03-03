import requests


class JobAPI:
    def __init__(self):
        """
        Инициализирует объект с заданным значением base_url.
        :param base_url: str - Базовый URL-адрес объекта.
        :return: None
        """
        self.url = 'https://api.hh.ru/vacancies'
        self.params = {
            'text': 'python',
            'page': 0
        }

    def get_vacancies(self):
        """
        Отправляет запрос GET в API и возвращает список вакансий.
        :return: Список вакансий.
        """
        response = requests.get(self.url, params=self.params)
        return response


class HhJobAPI(JobAPI):
    """
    Инициализирует новый экземпляр класса с указанным базовым URL-адресом.
    Parameters:
    base_url (str): Базовый URL-адрес для API.
    Returns:
        None
    """

    def __init__(self, base_url="https://api.hh.ru"):
        super().__init__()
        self.base_url = base_url
