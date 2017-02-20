import os
import time
import sys

class MalopolskieVoivodeship:

    all_counties = []
    all_staff = []


class County:

    def __init__(self, name, number):

        self.communities = []
        self.name = name
        self.number_of_communities = len(self.communities)
        self.number = number
        self.type = "powiat"

        MalopolskieVoivodeship.all_counties.append(self)
        MalopolskieVoivodeship.all_staff.append(self)

    def __str__(self):
        return("{}".format(self.name))

class Community:

    def __init__(self, name, number, type, county):
        self.name = name
        self.number = number
        self.type = type #  (e.g. "gmina miejska")
        self.county = county  # (e.g. 06)
        MalopolskieVoivodeship.all_staff.append(self)

    def __str__(self):
        return("{}".format(self.name))  # must be used in for loop and use 'county' variable


class CityCounty:

    def __init__(self, name, type="miasto na prawach powiatu"):
        self.name = name
        self.type = type
        MalopolskieVoivodeship.all_staff.append(self)

    def __str__(self):
        return "{} {}".format(self.name, self.type)


class Main:

    @staticmethod
    def loading_data():
        """
        Loading cities, communities and other from a file
        """
        with open ("malopolska.csv") as my_file:
            my_lines = my_file.readlines()

            for index, line in enumerate(my_lines):  # loading counties
                my_list = line.split("\t")

                if my_list[5][-1] == '\n':
                    my_list[5] = my_list[5][:-1]

                if index == 0 or index == 1:
                    pass
                else:
                    if int(my_list[1]) > 0 and not my_list[2]:
                        County(my_list[4], my_list[1])

            for index, line in enumerate(my_lines):
                my_list = line.split("\t")
                if my_list[5][-1] == '\n':
                    my_list[5] = my_list[5][:-1]
                if index == 0:
                    pass
                else:
                    if not my_list[2]: # checking if it is a county or "miasto na prawach powiatu"
                        if "miasto na prawach powiatu" in my_list[5]:
                            CityCounty(my_list[4])
                    else:
                        for county in MalopolskieVoivodeship.all_counties:
                            if county.number == my_list[1]:
                                county.communities.append(Community(my_list[4], my_list[2], my_list[5], my_list[1]))


    @staticmethod
    def list_statistics():
        """
        Show statistics of a voivodeship
        """

        os.system("clear")
        print("...::: Know Your Neighborhood :::...\n\n")

        communities_list = ["gmina miejska", "gmina wiejska", "gmina miejsko-wiejska", "obszar wiejski", "miasto",
                            "miasto na prawach powiatu", "delegatura"]
        lens_tuple = Main.count_communities(communities_list)
        len_powiaty = len(MalopolskieVoivodeship.all_counties)
        table = ""
        table += "/----------------------------------\ \n"
        table += "|        MAŁOPOLSKIE               |\n"
        table += "|------+---------------------------|\n"

        locations = ["województwo", 'powiaty', 'gmina miejska', 'gmina wiejska', 'gmina miejsko-wiejska',
                     'obszar wiejski', 'miasto', 'miasto na prawach powiatu', 'delegatura']

        for location in locations:
            if location == "województwo":
                table += "|" + "1".rjust(5) + " | " + location.ljust(25) + " |\n"
            if location == "powiaty":
                table += "|" + str(len_powiaty).rjust(5) + " | " + location.ljust(25) + " |\n"
            elif location == "gmina miejska":
                table += "|" + str(lens_tuple[0]).rjust(5) + " | " + location.ljust(25) + " |\n"
            elif location == "gmina wiejska":
                table += "|" + str(lens_tuple[1]).rjust(5) + " | " + location.ljust(25) + " |\n"
            elif location == "gmina miejsko-wiejska":
                table += "|" + str(lens_tuple[2]).rjust(5) + " | " + location.ljust(25) + " |\n"
            elif location == "obszar wiejski":
                table += "|" + str(lens_tuple[3]).rjust(5) + " | " + location.ljust(25) + " |\n"
            elif location == "miasto":
                table += "|" + str(lens_tuple[4]).rjust(5) + " | " + location.ljust(25) + " |\n"
            elif location == "miasto na prawach powiatu":
                table += "|" + str(lens_tuple[5]).rjust(5) + " | " + location.ljust(25) + " |\n"
            elif location == "delegatura":
                table += "|" + str(lens_tuple[6]).rjust(5) + " | " + location.ljust(25) + " |\n"

            if location == "delegatura":
                table += "\----------------------------------/"
            else:
                table += "|------+---------------------------|\n"

        print(table)
        print("")
        wait = input("Press enter to continue")


    @staticmethod
    def count_communities(names_list):
        """

        :param names_list: list of types of locations
        :return: tuple of lenghts: ("gmina miejska", "gmina wiejska", "gmina miejsko-wiejska", "obszar wiejski", "miasto",
                            "miasto na prawach powiatu", "delegatura")
        """

        lens_list = []
        for name in names_list:
            counter = 0
            for community in MalopolskieVoivodeship.all_staff:
                try:
                    if community.type == name:
                        counter += 1
                except:
                    pass
            lens_list.append(counter)
        return lens_list


    @staticmethod
    def len_powiaty():
        """
        Checks how many counties are in voivodeship
        :return: Number of counties
        """
        return len(MalopolskieVoivodeship.all_counties)

    @staticmethod
    def cities_longest_names():
        """
        Using Bubble Sort
        Prints names of 3 longest locations
        """

        os.system("clear")
        print("...::: Know Your Neighborhood :::...\n\n")

        cities = []
        for community in MalopolskieVoivodeship.all_staff:
            try:
                if community.type == "miasto" or community.type == "miasto na prawach powiatu":
                    cities.append(community)
            except:
                pass

        len_cities = len(cities)
        counter = 1
        while counter > 0:
            counter = 0
            for i in range(1, len_cities):
                if len(cities[i-1].name) > len(cities[i].name):
                    cities[i], cities[i - 1] = cities[i - 1], cities[i]
                    counter += 1

        longest_cities = [cities[-1], cities[-2], cities[-3]]
        print("Longest cities:\n")
        for index, city in enumerate(longest_cities):
            print(str(index+1) + ". " + str(city), "\n" + "Lenght: " + str(len(city.name)) + "\n")

        print("")
        wait = input("Press enter to continue")

    @staticmethod
    def largest_county():
        """
        Prints county with the largest number of communities and number of communities
        """

        os.system("clear")
        print("...::: Know Your Neighborhood :::...\n\n")

        if len(MalopolskieVoivodeship.all_counties) == 0:
            print("No counties.")
        else:
            largest_county = MalopolskieVoivodeship.all_counties[0]
            communities = 0
            for county in MalopolskieVoivodeship.all_counties:
                if len(county.communities) > len(largest_county.communities):
                    largest_county = county
                    communities = len(county.communities)

            print("County with the largest numbers of communities: {}".format(largest_county))
            print("Communities: {}".format(communities))

        print("")
        wait = input("Press enter to continue")


    @staticmethod
    def locations_many_types():
        """
        Prints names that are in different types of locations
        """

        os.system("clear")
        print("...::: Know Your Neighborhood :::...\n\n")

        locations = []
        locations_dict = {}
        for location in MalopolskieVoivodeship.all_staff:
            if location.name in locations_dict:
                locations_dict[location.name] += 1
            else:
                locations_dict[location.name] = 1

        for location_name, counter in locations_dict.items():
            if counter > 1:
                locations.append(location_name)

        print("Locations that belong to more than one category:\n")
        for index, location in enumerate(locations):
            print(str(index+1).rjust(3) +". {}".format(location))

        print("")
        wait = input("Press enter to continue")


    @staticmethod
    def advanced_search():
        """
        Search whatever you want from voivodeship!
        """

        os.system("clear")
        print("...::: Know Your Neighborhood :::...\n\n")

        locations = []
        user_input = input("Searching for: ")
        print("")
        counter = 0
        len_longest_city = 0
        for location in MalopolskieVoivodeship.all_staff:
            if user_input in location.name:
                if location.type == "powiat":
                    pass
                else:
                    locations.append(location)
                    counter += 1
                    if len(location.name) > len_longest_city:
                        len_longest_city = len(location.name)
        if counter > 0:
            print("Found {} location(s):\n".format(counter))

            table = ""
            table += str("/" + "-"*(len_longest_city + 38) +"\ " + "\n")
            table += "| LOCATION".ljust(len_longest_city + 6) +" | TYPE                      |\n".rjust(35)
            table += "|"
            table += "+".rjust(int(len_longest_city + 11), "-")
            table += "-".rjust(27, "-")
            table += "|\n"

            for location in sorted(locations, key = lambda location: (location.name, location.type)):
                table += "| " + location.name.ljust(len_longest_city + 9) + "| " + location.type.ljust(26) + "|" + "\n"

            table += "\-" + "-"*(len_longest_city + 37) +"/ " + "\n\n"
            print(table)

        if counter == 0:
            print("Found 0 locations\n")

        wait = input("Press enter to continue")


    @staticmethod
    def welcome_screen():
        """
        Welcome prints
        """
        os.system("clear")
        print("Welcome to ...::: Know Your Neighborhood :::...")
        time.sleep(2)


    @staticmethod
    def print_options():
        """
        Prints user options can do
        """
        os.system("clear")
        print("...::: Know Your Neighborhood :::...\n\n")
        options = ["List statistics", "Display 3 cities with longest names",
                   "Display county's name with the largest number of communities",
                   "Display locations, that belong to more than one category",
                   "Advanced search",
                   "Exit program"]

        print("What would you like to do?\n")
        for index, option in enumerate(options):
            if index == 5:
                print("   (0) " + option)
            else:
                print("   (" + str(index + 1) + ") " + option )
        print("\n")


    @staticmethod
    def error_integer_handling(chosen_option, value_of_possible_options):
        """
        :param chosen_option: user's input.
        :param value_of_possible_options: how many options users could take? Don't count 0 - exit
        :return: True or False. Will be useful to control while loop in other part of program. If True, continue program.
        """
        try:
            int(chosen_option)
            if int(chosen_option) < 0 or int(chosen_option) > value_of_possible_options:
                raise ValueError
        except TypeError:
            wait = input("Wrong input.")
            return False
        except ValueError:
            wait = input("It must be integer between 1 and " + str(value_of_possible_options) + " or 0. Press enter to try again.")
            return False
        return True


    @staticmethod
    def menu():
        """
        User main menu
        """
        Main.loading_data()
        Main.welcome_screen()
        while True:
            os.system("clear")
            Main.print_options()
            user_input = input()
            if Main.error_integer_handling(user_input, 5):
                user_input = int(user_input)

                if user_input == 1:
                    Main.list_statistics()
                elif user_input == 2:
                    Main.cities_longest_names()
                elif user_input == 3:
                    Main.largest_county()
                elif user_input == 4:
                    Main.locations_many_types()
                elif user_input == 5:
                    Main.advanced_search()
                elif user_input == 0:
                    sys.exit()


if __name__ == "__main__":
    Main.menu()