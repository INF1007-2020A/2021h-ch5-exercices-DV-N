#!/usr/bin/env python
# -*- coding: utf-8 -*-
if __name__ == '__main__':


    from typing import List


    def convert_to_absolute(number: float) -> float:
        if number < 0:
            number = -number
        return number

    def use_prefixes() -> List[str]:
        prefixes, suffixe = 'JKLMNOPQ', 'ack'
        liste_nom = []
        for pre in prefixes :
            liste_nom.append(pre + suffixe)

        return liste_nom

    def prime_integer_summation() -> int:
        liste_nb_premier = []
        nb = 2
        while len(liste_nb_premier) < 100:
            for i in range(2,nb+1): #creer un loop infinie a cette etape, mon hypothese : pcq le 1 et le 2 ne respecte pas le range
                if nb%i ==0:
                    nb +=1
                    continue
                else:
                    liste_nb_premier.append(nb)
                    nb += 1
        return sum(liste_nb_premier) #24,133 is the sum of the first 100 primes, +1 pcq nb=2 l'exclu de la liste

    def factorial(number: int) -> int:
        fac = 1
        for i in range(1, number+1):
            fac *= i
        return fac


    def use_continue() -> None:
        for i in range(1,10+1):
            if i ==5:
                continue
            print(i)

    def verify_ages(groups: List[List[int]]) -> List[bool]:
        return []


    def main() -> None:
        number = -4.325
        print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

        print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

        print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

        number = 10
        print(f"La factiorelle du nombre {number} est: {factorial(number)}")

        print(f"L'affichage de la boucle est:")
        use_continue()

        groups = [
            [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
                  [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
                  [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
        ]
        print(f"Les différents groupes sont: {groups}")
        print(f"L'acceptance des groupes est: {verify_ages(groups)}")


    if __name__ == '__main__':
        main()
