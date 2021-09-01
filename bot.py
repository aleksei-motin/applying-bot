from webdriver import *
from search_PO import Search as S
import time
from urllib.parse import urlparse

def main():

    # Заходит на главную страницу
    driver.get("https://hh.ru")
    driver.implicitly_wait(10)

    # Сохраняет куки (запустить единожды, чтобы залогиниться и пройти капчу)
    # pickle.dump(driver.get_cookies(), open("cookies", 'wb'))

    # Загружает куки
    for cookie in pickle.load(open('cookies', 'rb')):
        driver.add_cookie(cookie)
    driver.refresh()

    # Вводит ключевые слова и начинает поиск
    driver.find_element(
        By.XPATH, '//input[@data-qa="search-input"]').\
        send_keys("Junior Python developer", Keys.ENTER)

    # Собирает данные о текущей странице
    current_url = driver.current_url
    current_url = urlparse(current_url).path

    # Проверяет, что он на странице поиска
    if current_url.startswith("search"):
        pass
    else:
        pass

    # .bloko-modal - класс iframe для сопроводительного
    if_iframe = driver.find_element(By.CLASS_NAME, '.bloko-modal')
    if if_iframe:
        pass
    else:
        pass

    # Проверяет на страницу тестового задания
    if current_url.startswith("applicant"):
        pass
    else:
        pass


    # Скроллит до видимости и нажимает на кнопку "Откликнуться"
    submit_apply_buttons = driver.find_element(
        By.XPATH, '//a[@data-qa="vacancy-serp__vacancy_response"]').\
        click()

    while submit_apply_buttons:
        for button in submit_apply_buttons:
            driver.execute_script("arguments[0].scrollIntoView();", submit_apply_buttons)
            driver.execute_script("(arguments[0]).click();", submit_apply_buttons)

    # Возвращается на предыдущую страницу
    driver.back()

    # Проверяет не добавлена ли уже вакансия в избранное и сохраняет, если false (юзать после driver.back())
    mark = driver.find_element(By.XPATH, '//span[@data-qa="vacancy-search-mark-favorite-false"]')
    if mark == "vacancy-search-mark-favorite_false":
        pass # .click() для добавление в избранное
    else:
        pass

    # Переходит на новую страницу
    # driver.find_element(By.XPATH, 'a[@data-qa="pager-page"]/span')

    # Ждёт минуту и закрывает браузер
    # time.sleep(60)
    # driver.quit()

if __name__ == "__main__":
    main()
