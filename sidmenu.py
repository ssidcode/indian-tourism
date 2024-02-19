import menu as mn
import pandas as pd

while True:
    print('-------------------------------------------------------------------------------------------------------------')
    print('Press 1 for displaying information about inbound tourism')
    print('Press 2 for displaying SEASONALITY IN FOREIGN TOURIST ARRIVALS IN India ')
    print('Press 3 for displaying mode of travel  ')
    print('Press 4 for displaying  PORTS OF ENTRY')
    print('Press 5 for displaying gender-wise analysis')
    print('Press 6 for displaying age group-wise analysis')
    print('Press 7 for displaying purpose of visit for tourism')
    print('Press 8 for displaying  Indian monuments visited by domestic vs foreign tourists')
    print('Press 9 to return to main menu')
    print('-------------------------------------------------------------------------------------------------------------')

    n=eval(input('Enter  number of your choice: '))
    if n==1:
        mn.inbound()
    elif n==2:   
        print('Press 1 to show month-wise analysis')
        print('Press 2 to show quarter-wise analysis')
        a=eval(input('Enter the number of your choice: '))
        if a==1:
           mn.seasonality()
        elif a==2:
            mn.fta()
    elif n==3:
        print('Press 1 to display pie chart for mode of travel')
        print('Press 2 to display mode of transport world and nationality wise distribution')
        a=eval(input('Enter the number of your choice: '))
        if a==1:      
            mn.mode()
        elif a==2:
            mn.wndist()

    elif n==4:
        mn.ports()
    elif n==5:
        print('Press 1 to show bar chart for the gender-wise analysis')
        print('Press 2 to show pie chart for the gender-wise analysis')
        w=eval(input('Enter the number of your choice: '))
        if w==1:
            mn.gender()
        elif w==2:
            mn.gendist()
    elif n==6:
        print('Press 1 to show bar chart for the age-wise analysis')
        print('Press 2 to show pie chart for the age-wise analysis')
        w=eval(input('Enter the number of your choice: '))
        if w==1:
            mn.agegrp()
        elif w==2:
            mn.agepie()
    elif n==7:
        mn.prps()
    elif n==8:
        mn.monuments()
    else:
        break
