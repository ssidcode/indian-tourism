import pandas as pd,numpy as np
import graphs as gp,functions as fn, menu as mn
import tabulate as tab

def clear():
    for x in range(20):
        print()


def data():
    while True: 
        print('--------------------------------------------------------------------------------------------')
        print('Press 1 to display the dataframe for top 10 foreign countries visited India during 2014-2020')
        print('Press 2 to display the dataframe for top 10 most visited Indian states during 2014-2020')
        print('Press 3 to display geneal information about Foreign and Domestic tourism in India')
        print('Press 4 to return to main menu')
        print('---------------------------------------------------------------------------------------------')
        n=eval(input('Enter the number of your choice'))

        if n==1:
            print(tab.tabulate(df1,tablefmt='pretty',headers='keys',showindex='never'))
        elif n==2:
            print(tab.tabulate(df2,tablefmt='pretty',headers='keys',showindex='never'))
        elif n==3:
            print(tab.tabulate(df3,tablefmt='pretty',headers='keys',showindex='never'))
        else:
            break
            print('---------------------------------------------------------')
            input('Enter any key to continue: ')
            print('---------------------------------------------------------')
            clear()   
    
def textual():
    while True:
        print('------------------------------------------------------------------------------')
        print('Press 1 for displaying top Foreign countries visited India')
        print('Press 2 for dispalying Foreign countrywise comparison')
        print('Press 3 for displaying maximum and minimum tourist visits according to Foreign countries each year')
        print('Press 4 for dispalying analysis on state visitors of year of your choice')
        print('Press 5 for displaying max and min visitors visited state wise')
        print('Press 6 to return to main ')
        print('------------------------------------------------------------------------------')
        n=eval(input('Enter the number of your choice'))
         
        if n==1:
            fn.top()
        elif n==2:
            fn.countrywise()
        elif n==3:
            fn.comparison()
        elif n==4:
            fn.yearwise()
        elif n==5:
            fn.compare()
        else:
            break
            print('---------------------------------------------------------')
            input('Enter any key to continue: ')
            print('---------------------------------------------------------')
            clear()


def graphical():
    while True:
        print('---------------------------------------------------------------------------------------')
        print('Press 1 for dispalying maximum visitors each year statewise')
        print('Press 2 for displaying average visits each yaear')
        print('Press 3 for comparing top 10 countries of year of your choice')
        print('Press 4 for dispalying total number of visitors each year')
        print('Press 5 for displaying average visitors visiting India States each year')
        print('Press 6 for dispalying number of foreign tourists Visiting India in million')
        print('Press 7 for displaying comaprison of tourist arrivals vs departure growth over the years')
        print('Press 8 to return to main menu')
        print('------------------------------------------------------------------------------------------')
        n=eval(input('Enter the number of your choice: '))

        if n==1:
            gp.state()
        elif n==2:
            gp.avg()
        elif n==3:
            gp.yearsgf()
        elif n==4:
            gp.total()
        elif n==5:
            gp.state()
        elif n==6:
            gp.general()
        elif n==7:
            gp.local()
        else:
            break
            print('---------------------------------------------------------')
            input('Enter any key to continue: ')
            print('---------------------------------------------------------')
            clear()

def stats():
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
            print('Press 2 to show leak and peak moths of the season')
            a=eval(input('Enter the number of your choice: '))
            if a==1:
               mn.seasonality()
            elif a==2:
                mn.lkpk
        elif n==3:
            print('Press 1 to display bar and pie chart for mode of travel')
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
            print('---------------------------------------------------------')
            input('Enter any key to continue: ')
            print('---------------------------------------------------------')
            clear()

        
while True:
    print('Enter 1 for displaying the dataframe')
    print('ENter 2 for textual analysis on tourists arrivals')
    print('Enter 3 for graphical analysis on Visiting patterns')
    print('Enter 4 for diiferent staticts about Indian Tourism')
    print('Enter any key other key to exist')

    n=eval(input('Enter the number of your choice: '))
    clear()

    if n==1:
        data()
    elif n==2:
        textual()
    elif n==3:
        graphical()
    elif n==4:
        stats()
    else:
        print('Thank you');break

    
