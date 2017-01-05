from client import Parser

urls = [
        "http://stackoverflow.com/",
        "https://www.jeffknupp.com/",
        "https://khashtamov.com/",
        "https://students.superjob.ru/",
        "http://lol.fdsfsf/"
        ]

parser = Parser(5)
lst = parser.get_pages(urls)
for item in lst:
	print item
