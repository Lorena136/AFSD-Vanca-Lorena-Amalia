import string

# Declarați șirul copiat de pe internet
text = "În weekend, în Arabia Saudită a început a doua ediție a Săptămânii Modei. Evenimentul este dedicat designerilor de acolo. Zeci de designeri și-au prezentat creațiile care ar putea rivaliza cu cele ale unor branduri cu greutate și deja cunoscute în toată lumea."

# Împărțim șirul în două părți egale
middle = len(text) // 2
first_part = text[:middle]
second_part = text[middle:]

# Pe prima parte:
# Transformăm toate literele în majuscule
first_part = first_part.upper()

# Eliminăm toate spațiile goale de la începutul și finalul șirului
first_part = first_part.strip()

# Pe a doua parte:
# Inversăm ordinea caracterelor
second_part = second_part[::-1]

# Transformăm prima literă în majusculă
second_part = second_part.capitalize()

# Eliminăm toate caracterele de punctuație (., ,, !, ?)
second_part = second_part.translate(str.maketrans(" ", " ", string.punctuation))

# Combinăm cele două părți și afișăm rezultatul
result = first_part + second_part
print(result)
