from ics import Calendar, Event
import datetime
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
            start_time_modify = date + ' ' + start_time + ':00'
            start_time_obj = datetime.datetime.strptime(start_time_modify, '%Y-%m-%d %H:%M:%S')
            start_time_after_str = start_time_obj + datetime.timedelta(hours=-1)
            e.begin = str(start_time_after_str)

            #e.geo = "51.78;19.48"
            print("Ile ma trwać wydarzenie (w minutach)")
            end_time = int(input())
            time_obj = datetime.datetime.strptime(start_time_modify, '%Y-%m-%d %H:%M:%S')
            time_after_str = time_obj + datetime.timedelta(minutes=end_time)
            e.end = str(time_after_str)
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