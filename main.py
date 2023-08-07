import requests


class SwapiIter:

    def __init__(self):
        pass

    def __iter__(self):
        self.next_page = 'https://swapi.py4e.com/api/people/'
        self.results = []
        self.i = -1
        return self

    def __next__(self):
        self.i += 1
        if len(self.results) >= self.i:
            if not self.next_page:
                raise StopIteration
            data = requests.get(self.next_page).json()
            self.next_page = data['next']
            self.results = data['results']
            self.i = 0

        return self.results[self.i]


swapi = SwapiIter()
for item in swapi:
    print(item)
