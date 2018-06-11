#################################################################
### ASSIGNMENT 1: Solutions to given problems of PYTHON 1     ###
###                                                           ###
### AUTHOR: Kwadwo Amoako Jr.                                 ###
###                                                           ###
### DESCRIPTION: Function.1 solves the problem of numbers     ###
###              divisible by 7, not 5 divisible; and between ###
###              2000 & 3200.                                 ###
###                                                           ###
###              Funtcion.2 solves the problem of returning a ###
###              given first and surname in reverse order     ###
###                                                           ###
###              Function.3 solves the volume of a sphere     ###
###              when given the diameter- in 'cm' - of sphere ###
###                                                           ###
### PURPOSE: execute the defined functions below and the      ###
###          returned results should be as in the             ###
###          'DESCRIPTION'.                                   ###
#################################################################

def seven_div(arr):
    """ print out all elements, 7 divisible not 5 divisible,
    in given list. elements must be between 2000 and 3200.
    parameter: arr = list """

    _data = arr
    _target_data = []   # target data storage

    ##___loop through given list___##
    for number in _data:
        if number >= 2000 and number <= 3200:  # first filter stage
            div_five = number % 5
            div_seven = number % 7

            if div_five != 0 and div_seven == 0:   # second filter stage
                _target_data.append(number)  # add qualifying numbers to new list

    limit = len(_target_data)  # get number of elements in new list
    for i in _target_data:     # loop through new list

        ##___print elements, comma seperated___##
        if limit > 1:
            print(i, end=',')
            limit -= 1
        else:
            print(i)
            
            
def fullname(first=None, last=None):
    """ print first and last name is reverse order
    parameter: first= first name
               last= last name   """

    first = first   # first name
    last = last     # last name

    ##___check for first name___##
    if first == None:
        first = input('First Name: ')  # ask for first name

    ##___check for last name___##
    if last == None:
        last = input('Last Name: ')  # ask for last name

    print(last + ' ' + first)



def sph_volume(diameter):
    """ find the volume of a sphere in centimeters
    parameter: diameter = diameter """

    _ratio = 4/3
    _PI_ = 3.14
    radius = diameter/2

    ##__find volume __##
    volume = _ratio * _PI_ * (radius**3)

    return volume

    
                      

    
    


    

    
                
    
