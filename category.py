from requests_html import HTMLSession

category_basic = [
    'https://www5.pornhd.to/category/blowjob',
    'https://www5.pornhd.to/pornstar',
    'https://www5.pornhd.to/studio/mofos',
    'https://www5.pornhd.to/studio/brazzers',
]


def javforme_studio_category():
    home_url = 'https://www5.pornhd.to'
    session = HTMLSession()
    r = session.get(home_url)
    menu = r.html.find('#menu', first=True)
    all_categ_links = menu.absolute_links
    studio_links = list(filter(lambda x: 'studio' in x, all_categ_links))
    return studio_links


def pornhd_category():
    home_url = 'https://www5.pornhd.to/'
    session = HTMLSession()
    r = session.get(home_url)
    menu = r.html.find('#menu', first=True)
    all_categ_links = menu.absolute_links
    return all_categ_links


def index_category(to_file='output/category_javforme.txt'):
    category_studio = javforme_studio_category()
    category_all = category_basic + category_studio
    with open(to_file, 'w') as f:
        f.write('\n'.join(category_all))


if __name__ == '__main__':
    index_category()
