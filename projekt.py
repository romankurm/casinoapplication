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
    roulettenumbrid = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ,14 ,15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    winnumber = (random.choice(roulettenumbrid))
    return winnumber

#funktsioon odds tagastab suvalise numbri 1-30.

under = 1
over = 2
middle = 3
win = 0

roulettewin = odds()

def wincontrol():
    global under, over, middle, win
    if roulettewin <= 13:
        win = under
    elif roulettewin >= 15:
        win = over
    elif roulettewin == 14:
        win = middle
    return win

#funktsioon wincontrol kontrollib kas võidunumber jäi punaste(1-13) või mustade(15-30) vahele või hoopis roheliseks(14)

sg.theme('GreenMono')
paigutus = [[sg.Text('WinOnly CASINO', text_color='red', font=("Helvetica", 18))],
          [sg.Text('Sisestage nimi: ')],
          [sg.InputText(key="eesnimi")],
          [sg.Text('Sisestage pangakonto nr: ')],
          [sg.InputText(key="pank")],
          [sg.Text('_' * 80)],
          [sg.Submit('Roulette'), sg.Submit('Slots')]]
aken = sg.Window('1. aken: andmed', paigutus, size=(1024,800))

#"ehitame" esimese akna paigutuse.

syndmus, sisestatud = aken.read()

if syndmus == sg.WIN_CLOSED:
    aken.close()
#akna sulgemisel lõpetab programm töö

elif syndmus == 'Roulette':
    aken.close() #Põhiaken suletakse kui vajutatakse Roulette nupule
    
    #loome uue paigutuse uue akna jaoks
    paigutus2 = [[sg.Text('BigBassBonex', text_color='black', font=("Helvetica", 12))],
                [sg.Text('Numbrid 1-13; 15-31 tagastavad kahekordse summa, 14 tagastab 7X')],
                [sg.Text('Millisele numbrile panustate? ', size=(15,2)), sg.Slider(range=(0,31), orientation='h', size=(50,25), key='L')],
                [sg.Text('Mitme euroga panustate? ')],
                [sg.InputText(key="panus")],
                [sg.Submit('Sisesta'), sg.Cancel('Välju')]]

    aken = sg.Window('2. aken: Roulette', paigutus2, size=(1024,800))
    sisestatud2, sisestatud2 = aken.read()
    
    
    
    #kui vajutatakse nuppu 'Slots', pannakse põhiaken kinni ja avaneb uus aken
elif syndmus == 'Slots':
    aken.close()

    #loome jällegi uue akna

    paigutus3 = [[sg.Text('BigRassBonex', text_color='black', font=("Helvetica", 12))],
            [sg.Text('Hetkel saab proovida vaid Roulette masinat.')]]


aken = sg.Window('2. aken: Slots', paigutus3, size=(1024,800))
sisestatud2, sisestatud2 = aken.read()
    
    
aken.close()
