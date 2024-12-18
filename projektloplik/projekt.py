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
import os
import PySimpleGUI as sg
import copy
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

slots_spinned = False

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

while True:

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

    eesnimi = values['eesnimi']
    pank = values['pank']

    if event == sg.WIN_CLOSED:
        window.close()
        break
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
                        [sg.Text(f'Roulette võiduvõimalus: {color}, {roulette_win}')],
                        [sg.Text('Teie panus oli: ' + str(bet_amount))],
                        [sg.Text('Teie panustatud number oli: ' + str(bet_number) + ' (' + color_chosen + ')')],
                        [sg.Text('Teie võidetud summa on: ' + str(cashback))],
                        [sg.Text('Pangakontole ' + (pank) + ' on laekunud võit!')],
                        [sg.Submit('Välju')]
                    ]

            
            window = sg.Window('3. window: Tulemus', layout3, size=(1024,800))
            while True:
                event3, values3 = window.read()

                if event3 == sg.WIN_CLOSED or event3 == 'Välju':
                    window.close()
                    quit()

        #kui vajutatakse nuppu 'Slots', pannakse põhiwindow kinni ja avaneb uus window
    elif event == 'Slots':

        # sulgeme vana akna

        window.close()

        # faili tee pildile
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_dir, 'casinoslotsmachine.png')

        # teeme esmase layouti

        layout4 = [
                    [sg.Image(filename=image_path)],
                    [sg.Text('Nimi: ' + eesnimi, text_color='green')],
                    [sg.Text('Pangakonto: ' + pank, text_color='green')],
                    [sg.Text('BigBassBonex', text_color='black', font=("Helvetica", 12))],
                    [sg.Text('Slots masin - kahekordista oma pangakonto!', text_color='red', font=("Helvetica", 12))],
                    [sg.Text('Mitme euroga panustate? ')],
                    [sg.InputText(key="panus")],
                    [sg.Button("Tulista!", key="P")],
                    [sg.Button("Tagasi...", key="T")]
                    ]
        
        # faili teed slots machine ikoonidele
        
        slots_icon_7 = os.path.join(base_dir, 'slotmachine_7.png')
        slots_icon_fruit = os.path.join(base_dir, 'slotmachine_fruit.png')

        # list mis sisaldab ikoone (teen selle selleks, et hiljem suvaliselt valida siit ikooni faili tee)

        slots = [slots_icon_7, slots_icon_fruit]

        # loome uue akna

        window = sg.Window('4. window: Slots', layout4, size=(1024,800))

        while (True):

            event4, values4 = window.read()

            # see if statement on true, kui mangija vajutab 'Tulista!' nupule
            if (event4 == 'P'):

                # sule vana aken
                window.close()

                #vali suvalised numbrid nullist yheni
                rand_int = random.randint(0, 1)
                rand_int_2 = random.randint(0, 1)
                rand_int_3 = random.randint(0, 1)

                # koostame uue layouti, mis seekord sisaldab ka meie suvaliselt valitud ikoone uksteise jarel
                layout4 = [
                [sg.Image(filename=image_path)],
                [sg.Text('Nimi: ' + eesnimi, text_color='green')],
                [sg.Text('Pangakonto: ' + pank, text_color='green')],
                [sg.Text('BigBassBonex', text_color='black', font=("Helvetica", 12))],
                [sg.Text('Slots masin - kahekordista oma pangakonto!', text_color='red', font=("Helvetica", 12))],
                [sg.Text('Mitme euroga panustate? ')],
                [sg.InputText(key="panus")],
                [sg.Button("Tulista!", key="P")],
                [sg.Button("Tagasi...", key="T")],
                [sg.Image(filename=slots[rand_int]), sg.Image(filename=slots[rand_int_2]), sg.Image(filename=slots[rand_int_3])],
                ]

                #slots võidu arvutamine
                bet_amount = int(values4['panus'])
                slotwin = bet_amount * 7

                # kui mangija sai kolm samasugust ikooni jarjest siis on ta voitja
                if (rand_int == rand_int_2 and rand_int == rand_int_3):
                    layout4.append([sg.Text('Sa võitsid ' + str(slotwin) + ' eurot. Palju õnne! Sinu pangakontole: ' + (pank) + ' on laekunud võit!', text_color='red', font=("Helvetica", 12))])
                # loo uus aken peale slot machine spinnimist
            
                window = sg.Window('4. window: Slots', layout4, size=(1024,800))

            # see if statement on true, kui mangija vajutab 'Tagasi..' nupule
            elif (event4 == 'T'):
                break
            # see if statement on true, kui mangija sulgeb akna ristist
            elif (event4 == sg.WIN_CLOSED):
                quit()


        window.close()