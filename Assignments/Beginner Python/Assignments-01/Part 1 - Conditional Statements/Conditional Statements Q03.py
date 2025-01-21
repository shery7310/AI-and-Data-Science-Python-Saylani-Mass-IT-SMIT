# Write a program that checks if a given year is a leap year.

# https://airandspace.si.edu/stories/editorial/science-leap-year
# https://www.quora.com/Why-does-a-leap-year-have-to-be-divisible-by-100

"""
We could do this in any pattern we wanted… but it’s best if we make the pattern as easy
to remember as possible. So we add a leap day to every calendar year that
is evenly divisible by 4… except for century years.
A century year is only a leap year if it is divisible by 400.
"""

year = input("Enter any Year:\n")
if len(year) > 3: # If user enters something like 200 we will ask him to enter a valid year
    year = int(year)
    if year % 100 == 0:    # this is to filter out century year
        if year % 400 == 0: # for a century year to be a leap year it has to be
            print(f"{year} is a leap year") # divisible by both 400 and 100
        else:
            print(f"{year} is not a leap year")
    else:
        if year % 4 == 0: # a leap year is always divible by 4
            print(f"{year} is a leap year")
        elif year % 4!= 0 :
            print(f"{year} is not a leap year")
else:
    print(f"Enter a Valid Year")                


'''
These are some leap years we can check the program against:
    1804, 1808, 1812, 1816, 1820, 1824, 1824, 1832, 1836, 1840,
    1844, 1848, 1852, 1856, 1860, 1864, 1868, 1872, 1876, 1880,
    1884, 1888, 1892, 1896, 1904, 1908, 1912, 1916, 1920, 1924,
    1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964,
    1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004,
    2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044,
    2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084,
    2088, 2092, 2096
'''    

# We could improve this code:

if len(year) > 3: 
    year = int(year)
    if year % 100 == 0 and year % 400 == 0: 
        print(f"{year} is a leap year") 
    else:
        if year % 4 == 0:
            print(f"{year} is a leap year")
        elif year % 4!= 0 :
            print(f"{year} is not a leap year")
else:
    print(f"Enter a Valid Year")      