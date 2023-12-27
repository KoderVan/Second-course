import re
import requests


def get_links(first_link):
    request_link = requests.get(first_link).text
    pattern = r"href=\"([\w\:\/\.]+)"
    search = re.findall(pattern, request_link)
    inner_links = []
    for link in search:
        get_link = requests.get(link).text.strip()
        inner_links += re.findall(pattern, get_link.replace('stepic.org', 'stepik.org'))
    return inner_links


def result_of_search(list_of_links, second_link):
    if second_link in list_of_links:
        return 'Yes'
    else:
        return 'No'


def main():
    list_of_links = get_links(input())
    final_result = result_of_search(list_of_links, input())
    print(final_result)


if __name__ == "__main__":
    main()
