from collections import defaultdict

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# 1
updated_damages = []

def modify_damages():
    for d in damages:
        if "M" in d:
            updated_damages.append(float(d[:-1]) * conversion["M"])
        elif "B" in d:
            updated_damages.append(float(d[:-1]) * conversion["B"])
        else:
            updated_damages.append(d)
    return updated_damages

# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
modify_damages()
print("++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++")

# 2
# Create a Table
all_lists = zip(names, months, years, max_sustained_winds, areas_affected, deaths)
print(list(all_lists))
print("++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++")

hurricanes = {}


def construct_hurricanes():
    for index in range(len(names)):
        hurricanes[names[index]] = {"Name": names[index],
                                    "Month": months[index],
                                    "Year": years[index],
                                    "Max Sustained Wind": max_sustained_winds[index],
                                    "Areas Affected": areas_affected[index],
                                    "Damage": updated_damages[index],
                                    "Deaths": deaths[index]}

    print(hurricanes)


# Create and view the hurricanes dictionary
construct_hurricanes()
print("++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++")
# 3
# Organizing by Year
year_hurricane = {}
current_year = {}
current_cane = []


def create_hurc_by_year():
    for val in hurricanes:
        current_cane = hurricanes[val]
        current_year = hurricanes[val]["Year"]
        if current_year in year_hurricane.keys():
            year_hurricane[current_year].append(current_cane)
        else:
            year_hurricane[current_year] = [current_cane]

    print(year_hurricane[2005])


# create a new dictionary of hurricanes with year and key
create_hurc_by_year()
print("++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++")

# 4
# Counting Damaged Areas
impact_count = 0
area = []
impacted_areas = {}

# Below 'counter' used for create_hurc_by_year2
count = defaultdict(int)


# create dictionary of areas to store the number of hurricanes involved in
def create_hurc_by_year():
    for hurc in hurricanes:
        area = hurricanes[hurc]["Areas Affected"]
        for val in area:
            if val in impacted_areas.keys():
                impacted_areas[val] += 1
            else:
                impacted_areas[val] = 1

    print(impacted_areas)


# Utilizing defaultdict w/count variable
def create_hurc_by_year2():
    for hurc in hurricanes:
        area = hurricanes[hurc]["Areas Affected"]
        for val in area:
            count[val] += 1

    impacted_areas.update(count)
    print(impacted_areas)


create_hurc_by_year()
print("++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++")

# 5
# Calculating Maximum Hurricane Count
most_impacted = {}


def find_most_impacted_area():
    max_hurc_count = max(impacted_areas.values())
    max_hurc_key = max(impacted_areas, key=impacted_areas.get)
    max_area = {max_hurc_key: max_hurc_count}
    most_impacted.update(max_area)
    print(most_impacted)


# find most frequently affected area and the number of hurricanes involved in
find_most_impacted_area()
print("++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++")

# 6
# Calculating the Deadliest Hurricane
deadliest_hurc = {}


def the_deadliest():
    death_count = 0
    for val in hurricanes:
        if death_count < hurricanes[val]["Deaths"]:
            death_count = hurricanes[val]["Deaths"]
            death_hurc = hurricanes[val]["Name"]

    deadliest_hurc[death_hurc] = death_count
    for hurc, deaths in deadliest_hurc.items():
        print("The deadliest hurricane is " + hurc + " with a total of " + str(deaths) + " deaths.")


the_deadliest()
print("++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++")

# find highest mortality hurricane an
hurricanes_by_mortality = {}
for key in range(6):
    hurricanes_by_mortality[key] = []


def get_hurc_mortality():
    for hurc in hurricanes:
        if hurricanes[hurc]["Deaths"] > 0 and hurricanes[hurc]["Deaths"] <= 100:
            hurricanes_by_mortality[1].append(hurricanes[hurc])
        elif hurricanes[hurc]["Deaths"] > 100 and hurricanes[hurc]["Deaths"] <= 500:
            hurricanes_by_mortality[2].append(hurricanes[hurc])
        elif hurricanes[hurc]["Deaths"] > 500 and hurricanes[hurc]["Deaths"] <= 1000:
            hurricanes_by_mortality[3].append(hurricanes[hurc])
        elif hurricanes[hurc]["Deaths"] > 1000 and hurricanes[hurc]["Deaths"] <= 10000:
            hurricanes_by_mortality[4].append(hurricanes[hurc])
        elif hurricanes[hurc]["Deaths"] > 10000:
            hurricanes_by_mortality[5].append(hurricanes[hurc])
        else:
            hurricanes_by_mortality[0].append(hurricanes[hurc])

    print(hurricanes_by_mortality)


# categorize hurricanes in new dictionary with mortality severity as key
get_hurc_mortality()
print("++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++")


# 8 Calculating Hurricane Maximum Damage

def get_costliest_hurricane():
    max_damages_hurc = ''
    max_damages = 0
    for hurc in hurricanes:
        if hurricanes[hurc]["Damage"] == "Damages not recorded":
            continue
        elif hurricanes[hurc]["Damage"] > max_damages:
            max_damages = hurricanes[hurc]["Damage"]
            max_damages_hurc = hurricanes[hurc]

    print("Hurricane " + max_damages_hurc["Name"] + " caused the greatest damage at a cost of " + str(
        max_damages_hurc["Damage"]))


# find highest damage inducing hurricane and its total cost
get_costliest_hurricane()
print("++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++")

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

# categorize hurricanes in new dictionary with damage severity as key
hurricane_damage_ratings = {}

for key in range(6):
    hurricane_damage_ratings[key] = []


def hurc_damage_ratings():
    for hurc in hurricanes:
        if hurricanes[hurc]["Damage"] == "Damages not recorded":
            continue
        for key, value in damage_scale.items():
            if hurricanes[hurc]["Damage"] <= float(value):
                hurricane_damage_ratings[key].append(hurricanes[hurc])
                break
            elif hurricanes[hurc]["Damage"] > float(50000000000):
                hurricane_damage_ratings[5].append(hurricanes[hurc])
                break

    print(hurricane_damage_ratings)


# categorize hurricanes in new dictionary with damage severity as key
hurc_damage_ratings()


