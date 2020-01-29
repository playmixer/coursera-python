from bs4 import BeautifulSoup
import re
import os


# Вспомогательная функция, её наличие не обязательно и не будет проверяться
def build_tree(start, end, path):
    link_re = re.compile(r"/wiki/([\w()]+)")  # Искать ссылки можно как угодно, не обязательно через re
    files = dict.fromkeys(os.listdir(path))  # Словарь вида {"filename1": None, "filename2": None, ...}
    # TODO Проставить всем ключам в files правильного родителя в значение, начиная от start
    
    with open("{}{}".format(path, start), encoding='utf-8') as html:
        links = re.findall(link_re, html.read())                
        links = set(links)
        for link in links:
            if link in files:
                if files[link] is None:
                    files[link] = start
    page = start
    none_parent = True
    while none_parent:
        none_parent = False
        for file in files:
            if file != start:
                if files[file] is not None:
                    page = file
                    with open("{}{}".format(path, page), encoding='utf-8') as html:
                        links = re.findall(link_re, html.read())                
                        links = set(links)
                        for link in links:
                            if link in files:
                                if files[link] is None:
                                    files[link] = page
                                if link == end:
                                    return files
                else:
                    none_parent = True
            
    files = []
    return files


# Вспомогательная функция, её наличие не обязательно и не будет проверяться
def build_bridge(start, end, path):
    files = build_tree(start, end, path)    
    bridge = []
    # TODO Добавить нужные страницы в bridge
    bridge.append(end)
    while start not in bridge:
        bridge.append(files[end])
        end = files[end]
    return bridge


def parse(start, end, path):
    """
    Если не получается найти список страниц bridge, через ссылки на которых можно добраться от start до end, то,
    по крайней мере, известны сами start и end, и можно распарсить хотя бы их: bridge = [end, start]. Оценка за тест,
    в этом случае, будет сильно снижена, но на минимальный проходной балл наберется, и тест будет пройден.
    Чтобы получить максимальный балл, придется искать все страницы. Удачи!
    """

    bridge = build_bridge(start, end, path)  # Искать список страниц можно как угодно, даже так: bridge = [end, start]

    # Когда есть список страниц, из них нужно вытащить данные и вернуть их
    out = {}
    for file in bridge:
        with open("{}{}".format(path, file), encoding='utf-8') as data:
            soup = BeautifulSoup(data, "lxml")

        body = soup.find(id="bodyContent")

        # TODO посчитать реальные значения
        imgs = len([img for img in body.find_all('img', width=True) 
                        if int(img['width']) >= 200]) # Количество картинок (img) с шириной (width) не меньше 200
        
        count_header = 0
        heads = body.find_all(name=['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        for head in heads:
            for i in range(len(head.contents)):
                if not head.contents[i].string is None:
                    if head.contents[i].string[0] in ['E', 'T', 'C']:
                    # if not re.search(r"^[E,T,C]", head.contents[i].string) is None:
                        count_header += 1
                        break

        headers = count_header #10  # Количество заголовков, первая буква текста внутри которого: E, T или C
        
        tags_a = body.find_all('a')
        max_link_con = 0
        for i in range(len(tags_a)):
            t = tags_a[i].find_next_siblings()
            count = 1
            for tag in t:
                if tag.name == 'a':
                    count += 1
                    max_link_con = max(count,max_link_con)
                else:
                    count = 0
                
        linkslen = max_link_con  # Длина максимальной последовательности ссылок, между которыми нет других тегов
        
        lists = body.find_all(['ol','ul'])
        count_not_nested_list = 0
        for lst in lists:
            if lst.find_parent('li') is None:
                count_not_nested_list += 1
        
        lists = count_not_nested_list  # Количество списков, не вложенных в другие списки

        out[file] = [imgs, headers, linkslen, lists]
    return out


# if __name__ == "__main__":
#     start = 'Stone_Age'
#     end = 'Python_(programming_language)'
#     path = './wiki/'
#     res = parse(start, end, path)
#     print(res)