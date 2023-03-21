if __name__ == "__main__":
    galeries = []
    with open('galerie.txt') as file:
        for line in file.read().rstrip().split('\n'):
            galeries.append({"code": (data := line.split(' '))[0], "city": data[1], "stores": [int(x) for x in data[2:] if int(x)]})


    # Zadanie 4.1
    # Dla każdego kraju wyznacz liczbę miast, w których powstaną galerię
    # Podaj kod kraju i liczbę miast
    
    countries = {}
    for galerie in galeries:
        if (code := galerie["code"]) not in countries:
            countries[code] = {galerie["city"]}
        else:
            countries[code].add(galerie["city"])

    print("##################################################")
    print("W następujących krajach znajduje się taka liczba miast z galeriami")
    for country, cities in countries.items():
        print(f"{country} {len(cities)}")
    print("##################################################\n\n")


    # Zadanie 4.2a
    # Oblicz całkowitą powierzchnię handlową każdej galerii ora liczbę lokali
    
    print("##################################################")
    print("W różnych miastach galerie mają następującą łączną powierchnię i liczbę lokali")
    
    areas = []
    for galerie in galeries:
        area = 0
        for index in range(0, len(galerie["stores"]), 2):
            area += galerie["stores"][index]*galerie["stores"][index+1]
        areas.append(area)
        print(f"{galerie['city']} {area} {len(galerie['stores'])//2}")

    print("##################################################\n\n")


    # Zadanie 4.2b
    # Podaj nazwę miasta z galerią o największej powierzchni całkowitej oraz 
    # nazwę miasta z galerią o najmniejszej powierzchni całkowitej.
    
    maximal_area, minimal_area = max(areas), min(areas)
    maximal_city, minimal_city = galeries[areas.index(maximal_area)]["city"], galeries[areas.index(minimal_area)]["city"]

    print("##################################################")
    print(f"Galeria o największej powierzchni znajduje się w {maximal_city} i ma powierzchnię {maximal_area}")
    print(f"Galeria o najmniejszej powierzchni znajduje się w {minimal_city} i ma powierzchnię {minimal_area}")
    print("##################################################\n\n")


    # Zadanie 4.3
    # Dwa lokale są tego samego rodzaju, jeżeli ich powierzchnia jest taka sama
    # Podaj miasta oraz liczbę lokali, w których jest najwięcej różnych rodzajów sklepów
    # oraz najmniej różnych rodzajów sklepów

    number_of_types = []
    for galerie in galeries:
        types = []
        for index in range(0, len(galerie["stores"]), 2):
            if (area := galerie["stores"][index]*galerie["stores"][index+1]) not in types:
                types.append(area)
        number_of_types.append(len(types))
    
    minimal_number, maximal_number = min(number_of_types), max(number_of_types)
    minimal_city, maximal_city = galeries[number_of_types.index(minimal_number)]["city"], galeries[number_of_types.index(maximal_number)]["city"]

    print("##################################################")
    print(f"Galeria o największej liczbie różnych rodzajów lokali znajduje się w {maximal_city} i ma {maximal_number} rodzajów lokali")
    print(f"Galeria o najniejszej liczbie różnych rodzajów lokali znajduje się w {minimal_city} i ma {minimal_number} rodzajów lokali")
    print("##################################################\n\n")