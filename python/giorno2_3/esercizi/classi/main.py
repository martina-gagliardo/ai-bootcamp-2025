class Country:
    def __init__(self, name):
        self.name = name
        self.regions = []

    def add(self, region):
        self.regions.append(region)

    @property
    def pop(self):
        """La popolazione totale del paese"""
        return sum(region.pop for region in self.regions)

    @property
    def most_populous_city(self):
        """La città con la popolazione maggiore nel paese"""
        all_cities = [city for region in self.regions for city in region.cities]
        return max(all_cities, key=lambda city: city.pop)


class Region:
    def __init__(self, name):
        self.name = name
        self.cities = []
    def add(self, city):
        self.cities.append(city)

    @property
    def pop(self):
        """La popolazione totale della regione"""
        return sum(city.pop for city in self.cities)


class City:
    """Una città"""

    def __init__(self, name, pop=None):
        self.name = name
        self.pop = pop if pop is not None else 0
