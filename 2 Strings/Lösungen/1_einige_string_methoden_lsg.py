"""
Aufgabe 1: Lass zählen, wie oft der Buchstabe "e" im folgenden String vorkommt.
Hinweis: Nutze die count() Funktion.
"""

txt = "Dieser Tag heute ist besonders schön, da ich ausschlafen konnte."

print(txt.count("e"))


"""
Aufgabe 2: Unter einem Instgram-Post sollen die folgenden Hashtags stehen. Generiere
den String mit den genannten Hashtags und dem entsprechenden Symbol.
Hinweis: Nutze die join() Funktion.
"""

tags = ("summervibes", "nightout", "goodtimes", "happylife")

# "#" vorne anfügen, da join erst nach dem ersten String das angegebene Symbol anfügt
x = "#" + "#".join(tags)

print(x)