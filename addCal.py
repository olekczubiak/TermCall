from ics import Calendar, Event
c = Calendar()
e = Event()

class TermCall:
    def __init__(self):
        print("Podaj nazwe wydarzenia: ")
        name = input()
        e.name = name
        print("Podaj date wydarzenia pamietaj o formacie 20RR-MM-DD")
        date = input()
        print("Czy wydarzenie ma trwać cały dzień? (y/n) ")
        confirm_date = input().capitalize()
        if confirm_date == "Y":
            e.begin = date + ' 00:00:00'
            e.make_all_day()
            #Zapisuje cały dzień
        else:
            print("Podaj godzine rozpoczecia: (format 00:00)")
            start_time = input()
            e.begin = date + ' ' + start_time
            print("Podaj godzine zakonczenia: (format 00:00)")
            end_time = input()

            e.end = date + ' ' + end_time
        print("Podaj lokalizacje wydarzenia lub zostaw puste pole: ")
        where = input()
        e.location = where
        print("Podaj opis wydarzenia lub zostaw puste pole: ")
        description = input()
        e.description = description
        c.events.add(e)
        print(c.events)
        print('Czy chcesz zrobic z tego plik? - zapis (y/n)')
        confirm_save = input().capitalize()
        if confirm_save == 'Y':
            print('zapisuje do pliku')
            with open('my.ics', 'w') as my_file:
                my_file.writelines(c)
            
        else:
            print('koniec')



TermCall()