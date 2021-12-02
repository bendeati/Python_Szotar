# SZÓTÁR létrehozása és kezelés

torpek = {
    1: "Tudor",
    2: "Vidor",
    3: "Hapci",
    4: "Szende",
    5: "Szundi",
    6: "Morgó",
    7: "Kuka",
}

# A SZÓTÁR ELEMEINEK KIÍRÁSA, A SZÓTÁR BEJÁRÁSA
print("Csak úgy kiírom a szótárat...")
print(torpek)
print(f"A szótár elemszáma: {len(torpek)}")
print("Kiírom a KULCSOKAT:")
for elem in torpek.keys():
    print(elem, end=", ")

print("\nKiírom az ÉRTÉKEKET:")
for elem in torpek.values():
    print(elem, end=", ")

print("\nKiírom a párokat:")
for elem in torpek.items():
    print(elem)

print("\nMegint kiírom a párokat:")
for kulcs,ertek in torpek.items():
    print(kulcs, ertek)

# ELEM KÖZVETLEN ELÉRÉSE KULCS ALAPJÁN
print(f"\nA hetedik törpe: {torpek[7]}")
print(f"\nA hatodik törpe: {torpek.get(6)}")

# MEGÉRKEZIK HÓFEHÉRKE :)
print("Ki alszik az ágyamban?")
torpek[8] = "Hófehérke"
print(torpek[8])
print(f"A szótár elemszáma: {len(torpek)}")

# ELLENÖRZÉS - Lehet értékre és kulcsra is...
print("Kuka hazaért?")
if "Kuka" in torpek.values():
    print("Igen")
else:
    print("Nem")

# UPDATE
print("Ha már itthon van, nevezzük át...")
torpek.update({7: "Lomtár"})
print(torpek[7])
print(torpek)