import requests
import Queue
import threading

def parsing(queue):
    while True:
        url = queue.get()
        response = requests.get(url)
        print response.status_code
        print response.url
        #print response.content
        queue.task_done()


urls = [
        "http://stackoverflow.com/",
        "https://www.jeffknupp.com/",
        "https://khashtamov.com/",
        "https://students.superjob.ru/"
        ]

q = Queue.Queue()
for url in urls:
    q.put(url)

thread_count = 5
for i in range(thread_count):
    pill2kill = threading.Event()
    t = threading.Thread(target=parsing, args=(q,))
    t.daemon = True
    t.start()

q.join()
