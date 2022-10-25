"""
Napisati regex za provjeru validnosti unosa e-maila. E-Mail mora biti formata ime.prezime@fpmoz.sum.ba
Nakon toga napisati regex za provjeru eduId koji mora biti formata iprezimeX@sum.ba gdje je i prvo slovo
imena + prezime.
X predstavlja bilo koji broj (moze ici u beskonacnost), a taj broj ne mora postojati (može biti samo
iprezime@sum.ba).
Od korisnika zatražiti unos maila i eduid te ispisati uspješnost.
"""
import re
regex = '^[a-z0-9]+[\._]+[a-z0-9]+@fpmoz\.sum.ba$'
regex2 = '^[a-z0-9]+[0-9]?@sum\.ba$'
while 1:
    email = input("Unesite E-Mail: ")
    eduid = input("Unesite eduId: ")
    if (re.search(regex, email)):
        if(re.search(regex2, eduid)):
            print("E-mail i eduId valjan")
            break
    else:
        print("Pokusajte ponovno")
    



