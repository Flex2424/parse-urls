from client import Parser
from client2 import Parser2, Profiler

urls = [
        "http://stackoverflow.com/",
        "https://www.jeffknupp.com/",
        "https://khashtamov.com/",
        "https://students.superjob.ru/",
        "http://lol.zz",
        "https://www.python.org/",
        "https://pythonworld.ru/",
        "https://habrahabr.ru/",
        "https://python.ru/",
        "https://tproger.ru/",
        "https://en.wikipedia.org/",
        "https://cybersecurity.ru/",
        "https://www.coursera.org/",
        "https://www.nist.gov/",
        "https://www.owasp.org/",
        "https://sqlmap.org/",
        "https://github.com/",
        "https://www.sublimetext.com/",
        "https://pypi.python.org/",
        "https://www.yandex.ru/",
        "https://twitter.com/",
        "https://vk.com/",
        "https://www.facebook.com/"
        ]

with Profiler() as p:
    print "Total url: ", len(urls)
    parser = Parser2(7)
    lst = parser.get_pages(urls)
    print "len(lst): ", len(urls)
    for item in lst:
        print item
