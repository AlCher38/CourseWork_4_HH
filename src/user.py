def interact_with_user():
    while True:
        print("1. Ввести поисковый запрос для запроса вакансий из hh.ru")
        print("2. Получить топ N вакансий по зарплате")
        print("3. Получить вакансии с ключевым словом в описании")
        print("4. Выход")

        choice = input("Выберите действие (1/2/3/4): ")

        if choice == "1":
            search_query = input("Введите поисковый запрос для запроса вакансий из hh.ru: ")
            # Implement logic to request vacancies from hh.ru based on search_query
            # Display the retrieved vacancies to the user
            print("Вакансии, найденные по запросу:", search_query)
        elif choice == "2":
            top_n = int(input("Введите количество вакансий для топ N по зарплате: "))
            # Implement logic to retrieve top N vacancies by salary
            # Display the top N vacancies to the user
            print(f"Топ {top_n} вакансий по зарплате:")
        elif choice == "3":
            keyword = input("Введите ключевое слово для поиска в описании вакансий: ")
            # Implement logic to retrieve vacancies with the specified keyword in the description
            # Display the retrieved vacancies to the user
            print("Вакансии с ключевым словом в описании:", keyword)
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие 1, 2, 3 или 4.")
