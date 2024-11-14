################################################
# Programmeerimine I
# 2024/2025 sügissemester
#
# Projekt OnlyWin Casino
# Teema: Hasartmängude simulaator
#
#
# Autorid: Tim Ingo, Roman Kurm
#
# mõningane eeskuju: erinevad hasartmängud internetist
#
# Lisakommentaar: Käivitamiseks läheb vaja PySimpleGUI teeki.
#
##################################################


import random
import PySimpleGUI as sg
from datetime import date

def odds():
    roulette_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ,14 ,15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    win_number = (random.choice(roulette_numbers))
    return win_number

#funktsioon odds tagastab suvalise numbri 1-30.

under = 1
over = 2
middle = 3
win = 0

roulette_win = odds()

def win_control():
    global under, over, middle, win
    if roulette_win <= 13:
        win = under
    elif roulette_win >= 15:
        win = over
    elif roulette_win == 14:
        win = middle
    return win

win_number = win_control()
#funktsioon win_control kontrollib kas võidunumber jäi punaste(1-13) või mustade(15-30) vahele või hoopis roheliseks(14)
def calculations(number):
    if win_number == 1 and number <= 13:
        win = under
    elif win_number == 2 and number >= 15:
        win = over
    elif win_number == 3 and number == 14:
        win = middle
    else:
        win = 0
    return win

#funktsioon calculations kontrollib üle, kuhu võidunumber osutus ning mis oli panustatud number

sg.theme('GreenMono')
layout = [[sg.Text('WinOnly CASINO', text_color='red', font=("Helvetica", 18))],
          [sg.Text('Sisestage nimi: ')],
          [sg.InputText(key="eesnimi")],
          [sg.Text('Sisestage pangakonto nr: ')],
          [sg.InputText(key="pank")],
          [sg.Text('_' * 80)],
          [sg.Submit('Roulette'), sg.Submit('Slots')]]
window = sg.Window('1. window: andmed', layout, size=(1024,800))

#"ehitame" esimese akna layoute.

event, values = window.read()

if event == sg.WIN_CLOSED:
    window.close()
#akna sulgemisel lõpetab programm töö

elif event == 'Roulette':
    window.close() #Põhiwindow suletakse kui vajutatakse Roulette nupule
    
    #loome uue layoute uue akna jaoks
    layout2 = [[sg.Text('BigBassBonex', text_color='black', font=("Helvetica", 12))],
                [sg.Text('Numbrid 1-13; 15-31 tagastavad kahekordse summa, 14 tagastab 7X')],
                [sg.Text('Millisele numbrile panustate? ', size=(15,2)), sg.Slider(range=(0,31), orientation='h', size=(50,25), key='L')],
                [sg.Text('Mitme euroga panustate? ')],
                [sg.InputText(key="panus")],
                [sg.Submit('Sisesta'), sg.Cancel('Välju')]]

    window = sg.Window('2. window: Roulette', layout2, size=(1024,800))
    event2, values2 = window.read()
    #salvestame mis valikud kasutaja tegi

    if event2 == 'Sisesta':

        bet_number = values2['L']
        bet_amount = int(values2['panus'])
        result = calculations(bet_number)

#salvestame andmed muutujatele

        if win == 1:
            color = "Red"
        elif win == 2:
            color = "Black"
        elif win == 3:
            color = "Green"

#kontrollime mis värv võiduks osutunud on

        if bet_number <= 13:
            color_chosen = "Red"
        elif bet_number >= 15:
            color_chosen = "Black"
        elif bet_number == 14:
            color_chosen = "Green"

#salvestame kasutaja valitud värvi

        if result == 1:
            cashback = 2 * bet_amount
        elif result == 2:
            cashback = 2 * bet_amount
        elif result == 3:
            cashback = 7 * bet_amount
        else:
            cashback = 0

#arvutame panuse tagasimakse


        window.close()  # Sulgeme praeguse akna
        
        
        # paigutus viimase akna jaoks
        layout3 = [
            [sg.Text(f'Roulette võiduvõimalus: {color}, {roulette_win   }')],
            [sg.Text('Teie panus oli: ' + str(bet_amount))],
            [sg.Text('Teie panustatud number oli: ' + str(bet_number) + (color_chosen))],
            [sg.Text('Teie voidetud summa on: ' + str(cashback))],
            [sg.Submit('Välju')]
        ]
        
        
        window = sg.Window('3. window: Tulemus', layout3, size=(1024,800))
        while True:
            event3, values3 = window.read()

            if event3 == sg.WIN_CLOSED or event3 == 'Välju':
                window.close()
                break
        
    
    
    #kui vajutatakse nuppu 'Slots', pannakse põhiwindow kinni ja avaneb uus window
elif event == 'Slots':
    
    window.close()

    #loome jällegi uue akna

    layout4 = [[sg.Text('BigRassBonex', text_color='black', font=("Helvetica", 12))],
            [sg.Text('Hetkel saab proovida vaid Roulette masinat.')]]


    window = sg.Window('4. window: Slots', layout4, size=(1024,800))

    values4, values4 = window.read()
    
    
    window.close()