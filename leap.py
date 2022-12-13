# define a function with argument as year1, year2
def leapyear(n1,n2):

    leap_year = []       # initializing an empty list for leap year
    non_leap_year = []   # initializing an empty list for non leap year

    # iterating through for loop from year1 to year2
    for i in range(n1, n2+1):

        # condition for being a leap year
        if(i % 4 == 0 and i % 100 != 0 or i % 400 == 0):
            leap_year.append(i)      # appending in leap_year list

        else:
            non_leap_year.append(i)  # appending in non_leap_year list
    
    print('leap years are: ')
    # iterating through leap_year_list to print leap years
    for i in leap_year:    # iterating through list directly
        print(i, end = ' ')

    print()   # to print a new line between leap years and non leap years

    print("non leap years are: ")
    # iterating through leap_year_list to print non leap years
    for j in range(len(non_leap_year)):     # iterating through list using range
        print(non_leap_year[j], end = ' ')

d1 = [int(x) for x in input("Enter date1 as dd/mm/yyyy: ").split('/')]
n1 = d1[2]    # taking year for argument1 in function
d2 = [int(x) for x in input("Enter date2 as dd/mm/yyyy: ").split('/')]
n2 = d2[2]    # taking year for argument2 in function


# if year of date 1 greater than date 2 then swap the year
if n1 > n2:   
    n1, n2 = n2, n1
leapyear(n1, n2)   # calling function


# Thank you Sir for this project
