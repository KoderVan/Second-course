import re
import requests


class LinkExtractor:  # создаём класс патернов для дальнейшего использования
    pattern_to_get_links = r"a.* href=[\"\'][\w\:\.]*\/{2}([\w\.\-]+)"  # первый патерн для нахождения ссылок в документе
    pattern_to_find_sites = r"a.* href=[\"\']([\w\.\-]+)[\"\']"  # второй паттерн для "отчищения" ссылок и получения чистых ссылок

    def extract_links(self, page: str):  # создаём функцию выделения нужных ссылок, переводим тескт из ссылки в строку
        all_links = re.findall(self.pattern_to_get_links, page)  # нахождение всех ссылок в документе
        cleared_links = re.findall(self.pattern_to_find_sites, page)  # отчищение этих ссылок от ненужных символов
        uniq_links = {link.strip() for link in
                      all_links + cleared_links}  # собираем все ссылки в сет чтобы они не повторялись
        return sorted(list(uniq_links))  # возвращаем отсортированный список ссылок


extractor = LinkExtractor()  # запускаем класс
page = requests.get(input().strip()).text  # переменная для ввода ссылки
print(*extractor.extract_links(page), sep='\n')
