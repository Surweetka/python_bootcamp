wiek = int(input(f"Podaj swój rok urodzenia: "))

# import time
#
# localtime = time.asctime(time.localtime(time.time()))
# print(f"Aktualny czas: {localtime}")

import datetime

year = datetime.datetime.now().year
print(f"Aktualna data: {year}")

if year - wiek >= 18:
    print(f"Jesteś pełnoletni/a.")
else:
    print(f"Nie jesteś jeszcze pełnoletni/a.")
