liczby = [1, 5, 7, 15, 20, 49, 60];
szukana = int(input("podaj liczbę do wyszukania: "));

for i in range(len(liczby)):
    if liczby[i] == szukana:
        print(f"liczba {szukana} jest w zbiorze liczb");
    else:
        print("liczby nie znaleziono");