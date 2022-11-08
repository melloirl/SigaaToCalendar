from bs4 import BeautifulSoup


def getCourses(document):
    courses = {}
    page = BeautifulSoup(document.text, 'html.parser')
    t_start = page.find('tr', {'class': 'odd'})
    while (t_start.nextSibling):
        if (hasattr(t_start, 'children')):
            desc = t_start.find('td', {'class': 'descricao'})
            if (desc):
                name = desc.find('a').text
            info = t_start.find('td', {'class': 'info'})
            if (info):
                local = info.text
                times = info.find_next_sibling()
                if (times):
                    time = times.text.split()
        courses[name] = (local, time[0])
        t_start = t_start.nextSibling
    return courses
