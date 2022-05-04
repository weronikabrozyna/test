print("Jaką operację chcesz wykonać?(dodawanie, odejmowanie, mnożenie, dzielenie)")

operacja = input()
print("Podaj pierwszą liczbę:")
pierwsza_liczba=int(input())
print("Podaj drugą liczbę:")
druga_liczba=int(input())
if operacja == "dodawanie":
    print("Wynikiem dodawania tych liczb jest:",pierwsza_liczba+druga_liczba)
elif operacja == "odejmowanie":
    print("Wynikiem odejmowania tych liczb jest:",pierwsza_liczba-druga_liczba)
elif operacja == "mnożenie":
    print("Wynikiem mnożenia tych liczb jest:",pierwsza_liczba*druga_liczba)
elif operacja == "dzielenie":
    print("Wynikiem dzielenia tych liczb jest:",pierwsza_liczba/druga_liczba)
else:
    print("Nie potrafię zrobić takiej operacji.")
