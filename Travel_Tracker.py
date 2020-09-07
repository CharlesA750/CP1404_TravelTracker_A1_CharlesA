"""
Name: Charles Anderson
Date started: 29/08/2020
GitHub URL:
"""
MENU = "Menu: \nL - List places \nA - Add new place \nM - Mark a place as visited \nQ - Quit \n>>> "
FILENAME = "places.csv"
VISITEDMARK = " "
NOTVISITEDMARK = "*"


def main():
    print("Travel Tracker 1.0 - by Charles Anderson")
    places_list = open(FILENAME, 'r')
    print("{} places loaded from {}".format(len(places_list), FILENAME))
    menu_choice = input(MENU).upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            list_places(places_list)
        elif menu_choice == "A":
            places_list = add_places(places_list)
        elif menu_choice == "M":
            places_list = mark_visited(places_list)
        else:
            print("Invalid menu choice")
        menu_choice = input(MENU).upper()
    else:
        save_file(places_list)


def list_places(places_list):
    """Display the list of places to the console"""
    cities = [i[0] for i in places_list]
    countries = [i[1] for i in places_list]
    priorities = [i[2] for i in places_list]
    visited = [i[3] for i in places_list]
    format_length = max(len(words) for words in places_list)
    num_visited = sum(x.count("n") for x in places_list)
    list_len = -1
    for place in range(len(places_list)):
        list_len += 1
        if visited[list_len] == "v":
            print(VISITEDMARK + str(list_len + 1) + ". {} in {:{}} with priority {}".format(cities[list_len], countries[list_len],
                                                                              format_length, priorities[list_len]))

        else:
            print(NOTVISITEDMARK + str(list_len + 1) + ". {} in {:{}} with priority {}".format(cities[list_len], countries[list_len],
                                                                                    format_length, priorities[list_len]))
    print("{} places. You still want to visit {} places.".format(len(places_list), num_visited))
    return places_list


def add_places(places_list):
    """Add places to the list"""
    new_place = []
    city = input("Name: ").title()
    while city == "":
        print("Input can not be blank")
        city = input("Name: ").title()
    new_place.append(city)
    country = input("Country: ").title()
    while country == "":
        print("Input can not be blank")
        country = input("Country: ").title()
    new_place.append(country)
    finished = False
    while not finished:
        try:
            priority = int(input("Priority: "))
            if priority < 0:
                print("Number must be > 0")
            else:
                print("{} in {} (priority {}) added to Travel Tracker".format(city,country, priority), file=places_list)
                finished = True
        except ValueError:
            print("Invalid input; enter a valid number")
    new_place.append(priority)
    new_place.append("n")
    places_list = places_list.append(new_place)
    return places_list


def mark_visited(places_list):
    """Mark a place as visited"""
    change_visited = int(input("Enter the number of the place you want to mark as visited: "))
    while change_visited < 0:
        print("Number must be > 0")
        change_visited = int(input("Enter the number of the place you want to mark as visited: "))
    if change_visited > int(len(places_list)):
        print("Invalid place number")
    else:
        places_list[change_visited - 1][2].replace("n", "v")
        print("{} in {} visited".format(places_list[change_visited - 1][0], places_list[change_visited - 1][1]), file= places_list)
        return places_list


def save_file(places_list):
    places_list.close()
    print("{} places saves to {}".format(len(places_list), FILENAME))


main()

