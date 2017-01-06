import threading
try:
    import Queue
except ImportError:
    import queue as Queue

import requests


class Parser:
    def __init__(self, thread_count=4):
        self.thread_count = thread_count
        print "Threads count: ", self.thread_count
        self.results = []

    def parsing(self, queue):
        while True:
            url = queue.get()
            print "current: [{0}]".format(url)
            try:
                resp = requests.get(url)
                dict_url = {}
                dict_url["status code"] = resp.status_code
                dict_url["url"] = resp.url
                # dict_url["content"] = resp.content
                self.results.append(dict_url)
            except requests.RequestException as e:
                print "exception with {0}".format(url)
                dict_url = {}
                dict_url["status code"] = -1
                dict_url["url"] = url
                dict_url["err"] = e
                self.results.append(dict_url)

            queue.task_done()
            if queue.empty():
                break

    def get_pages(self, urls):
        q = Queue.Queue()
        for url in urls:
            q.put(url)

        wait_for_threads = []

        for i in range(self.thread_count):
            t = threading.Thread(target=self.parsing, args=(q,))
            t.start()
            wait_for_threads.append(t)

        for thread in wait_for_threads:
            thread.join()

        return self.results
