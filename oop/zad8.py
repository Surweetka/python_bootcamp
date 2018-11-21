def bold(func):
    def wrapper(*args, **kwargs):
        wynik = func(*args, **kwargs)
        return "<b>" + wynik + "<\\b>"
    return wrapper

def italic(func):


# @bold
def nasza_funkcja():
    return "Jakiś napis"

nasza_funkcja = bold(nasza_funkcja)

print(nasza_funkcja())