from webdriver import *
from search_PO import Search as S
import time

def main():

    # Заходит на главную страницу
    driver.get("https://hh.ru")
    driver.implicitly_wait(10)

    # Загружает куки
    for cookie in pickle.load(open('session', 'rb')):
        driver.add_cookie(cookie)
    driver.refresh()

    # Вводит ключевые слова и начинает поиск
    driver.find_element(
        By.XPATH, '//input[@data-qa="search-input"]').\
        send_keys("Junior Python developer", Keys.ENTER)

    # Проверяет что находится на странице поиска



    # Скроллит до видимости и нажимает на кнопку "Откликнуться"

    submit_apply_buttons = driver.find_element(
        By.XPATH, '//a[@data-qa="vacancy-serp__vacancy_response"]').\
        click()

    while True:
        for button in submit_apply_buttons:
            driver.execute_script("arguments[0].scrollIntoView();", submit_apply_buttons)
            driver.execute_script("(arguments[0]).click();", submit_apply_buttons)

    # Возвращается на предыдущую страницу

    # Сохраняет вакансию в избранное

    # Переходит на новую страницу

    # Ждёт минуту и закрывает браузер
    # time.sleep(60)
    # driver.quit()

if __name__ == "__main__":
    main()
