class Matura2021Marzec:
    def __init__(self):
        self.galeries = []
        with open('galerie.txt') as file:
            for line in file.read().rstrip().split('\n'):
                self.galeries.append({"code": (data := line.split(' '))[0], 
                                      "city": data[1], "stores": [int(x) for x in data[2:] if int(x)]})


    def zadanie_4_1(self) -> list:
        country_and_number = []
        countries = {}

        for galerie in self.galeries:
            if (code := galerie["code"]) not in countries:
                countries[code] = {galerie["city"]}
            else:
                countries[code].add(galerie["city"])

        for country, cities in countries.items():
            country_and_number.append((country, len(cities)))

        return country_and_number


    def zadanie_4_2(self):
        areas_and_locals = []
        areas = []

        for galerie in self.galeries:
            area = 0
            for index in range(0, len(galerie["stores"]), 2):
                area += galerie["stores"][index]*galerie["stores"][index+1]
            areas.append(area)
            areas_and_locals.append((galerie['city'], area, len(galerie['stores'])//2))

        maximal_area, minimal_area = max(areas), min(areas)
        maximal_city, minimal_city = self.galeries[areas.index(maximal_area)]["city"], self.galeries[areas.index(minimal_area)]["city"]

        return areas_and_locals, minimal_city, minimal_area, maximal_city, maximal_area


    def zadanie_4_3(self):
        number_of_types = []
        minimal_number, maximal_number = 0, 0
        minimal_city, maximal_city = '', ''

        for galerie in self.galeries:
            types = []
            for index in range(0, len(galerie["stores"]), 2):
                if (area := galerie["stores"][index]*galerie["stores"][index+1]) not in types:
                    types.append(area)
            number_of_types.append(len(types))
        
        minimal_number, maximal_number = min(number_of_types), max(number_of_types)
        minimal_city, maximal_city = self.galeries[number_of_types.index(minimal_number)]["city"], self.galeries[number_of_types.index(maximal_number)]["city"]

        return minimal_city, minimal_number, maximal_city, maximal_number
