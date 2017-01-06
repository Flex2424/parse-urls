from concurrent.futures import ThreadPoolExecutor
import requests
import time


class Parser2:
    def __init__(self, thread_count=4):
        self.thread_count = thread_count
        print "Threads count: ", self.thread_count
        self.results = []

    def parsing(self, url):
        resp = requests.get(url)
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

    def get_pages(self, urls):
        with ThreadPoolExecutor(self.thread_count) as executor:
            executor.map(self.parsing, urls)
        return self.results


class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print "Elapsed time: {:.3f} sec".format(time.time() - self._startTime)
