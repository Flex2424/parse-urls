import requests
import Queue
import threading

class Parser:
    def __init__(self, thread_count=4):
        self.thread_count = thread_count
        self.results = []


    def parsing(self, queue):
        while True:
            url = queue.get()
            try:
                resp = requests.get(url)
                dict_url = {}
                dict_url["status code"] = resp.status_code
                dict_url["url"] = resp.url
                #dict_url["content"] = resp.content
                self.results.append(dict_url)
            except requests.RequestException as e:
                dict_url = {}
                dict_url["status code"] = -1
                dict_url["url"] = url
                dict_url["err"] = e
                self.results.append(dict_url)

            queue.task_done()
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
