import json
from pprint import pprint

class Iterator:

    def __init__(self,FileJson):
        self.Filejson = FileJson
        self.current_list_index = 0

    def __iter__(self):
        return self

    def read(self):
        with open(self.Filejson, encoding = 'utf-8') as f:
            json_data = json.load(f)
        return json_data
#[self.current_list_index]['name']['common']

    def __next__(self):
        current_list = self.read()
        if self.current_list_index == len(current_list):
            raise StopIteration
        item = current_list[self.current_list_index]['name']['common']
        self.current_list_index += 1
        return "https://en.wikipedia.org/wiki/" + item

for item in Iterator('json.json'):
    print(item)