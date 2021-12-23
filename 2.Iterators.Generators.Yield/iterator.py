import json


class Country:

    def __init__(self, file_default, file_end):
        self.number = -1
        self.file_end = file_end

        with open(file_default) as f:
            data = json.load(f)
            self.data = data
            self.data_end = data[-1]

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        line = self.data[self.number]
        if line == self.data_end:
            raise StopIteration
        return line['name']['common']

    def writing_to_file(self):
        country_dict = dict()
        with open(self.file_end, 'w') as f:
            for country in self:
                if ' ' in country:
                    country_dict[country] = 'https://en.wikipedia.org/wiki/' + str(country.replace(" ", "_"))
                else:
                    country_dict[country] = 'https://en.wikipedia.org/wiki/' + str(country)
            json.dump(country_dict, f, indent=2)


mycountry = Country('countries.json', 'country.json')
mycountry.writing_to_file()
