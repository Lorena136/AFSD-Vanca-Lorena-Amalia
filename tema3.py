# Definirea datelor de bază
meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

# 1. Comenzi
print("Servirea comenzilor:")

# Procesăm comenzile manual, folosind indexare
student_1 = studenti[0]  # Liviu
comanda_1 = comenzi[0]   # guias
tava_1 = tavi.pop()      # elimină tava
istoric_comenzi.append(comanda_1)
print(f"{student_1} a comandat {comanda_1}.")

student_2 = studenti[1]  # Ion
comanda_2 = comenzi[1]   # ceafa
tava_2 = tavi.pop()      # elimină tava
istoric_comenzi.append(comanda_2)
print(f"{student_2} a comandat {comanda_2}.")

student_3 = studenti[2]  # George
comanda_3 = comenzi[2]   # ceafa
tava_3 = tavi.pop()      # elimină tava
istoric_comenzi.append(comanda_3)
print(f"{student_3} a comandat {comanda_3}.")

student_4 = studenti[3]  # Ana
comanda_4 = comenzi[3]   # papanasi
tava_4 = tavi.pop()      # elimină tava
istoric_comenzi.append(comanda_4)
print(f"{student_4} a comandat {comanda_4}.")

student_5 = studenti[4]  # Florica
comanda_5 = comenzi[4]   # ceafa
tava_5 = tavi.pop()      # elimină tava
istoric_comenzi.append(comanda_5)
print(f"{student_5} a comandat {comanda_5}.")

# 2. Inventar
print("\nInventar:")
# Numărarea porțiilor comandate
numar_guias = istoric_comenzi.count("guias")
numar_ceafa = istoric_comenzi.count("ceafa")
numar_papanasi = istoric_comenzi.count("papanasi")

# Afișăm câte porții s-au comandat
print(f"S-au comandat {numar_guias} guias, {numar_ceafa} ceafa, {numar_papanasi} papanasi.")
# Afișăm câte tăvi au rămas
print(f"Mai sunt {len(tavi)} tavi.")

# Verificăm disponibilitatea produselor
disponibilitate_ceafa = meniu.count("ceafa") > 0
disponibilitate_papanasi = meniu.count("papanasi") > 0
disponibilitate_guias = meniu.count("guias") > 0

print(f"Mai este ceafa: {disponibilitate_ceafa}.")
print(f"Mai sunt papanasi: {disponibilitate_papanasi}.")
print(f"Mai sunt guias: {disponibilitate_guias}.")

# 3. Finanțe
total_venit = (
    istoric_comenzi.count("papanasi") * 7 +
    istoric_comenzi.count("ceafa") * 10 +
    istoric_comenzi.count("guias") * 5
)

# Afișăm venitul total
print(f"\nCantina a încasat: {total_venit} lei.")

# Produse care costă cel mult 7 lei
produse_mici = [produs for produs in preturi if produs[1] <= 7]

print(f"Produse care costă cel mult 7 lei: {produse_mici}.")