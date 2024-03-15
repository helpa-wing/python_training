# Zadání věku uživatele
vek = int(input('Kolik je ti let? '))


# Kontrola na neobvykle vysoký věk
if vek > 100:
    print('Wow, to je úctyhodný věk! Nejsi náhodou upír?')

# Kontrola věku a výpis věku za 5 let
if vek >= 18:
    print('Jsi dospělý.')
    vek_za_pet_let = vek + 5
    print('Za 5 let ti bude', vek_za_pet_let, 'let.')

# Další kontrola pro velmi nízký věk
elif vek < 0:
    print('Věk nemůže být záporný! Zadal jsi to správně?')

else:
    print('Jsi nezletilý.')
