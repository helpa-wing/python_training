while True:
  print("""Vstupte do úžasného světa divokého království, kde realita splývá s přírodou.
  Vítáme vás v naší virtuální Zoologické zahradě,
  domově rozmanitého společenství zvířat ze všech koutů světa. """)
  print('O kterém z následujících podivných zvířat by ses chtěl dozvědět více?')
  user_input = input("""V digitálním světě programátorské zoologické zahrady se skrývají fascinující zvířata,
  o kterých málokdo ví. Jedním z nich je Binární Brouk.
  Dalším tajemným tvorem jsou Regulátorový Racci.
  Dále zde máme speciální druh Pseudokódový Papoušek,
  Strukturovaný Simpanz a Hashový hroch.
  O kterém by ses chtěl dozvědět více?""")
  if user_input == "Binární Brouk":
    print ("""Binární Brouk je unikátní bytost v naší digitální zoologické zahradě.
  Žije v binárním světě a komunikuje pomocí nul a jedniček podobně jako Morseova abeceda.
  Je to expert na zpracování binárních dat a má schopnost identifikovat chyby v digitálních systémech.
  Jeho adaptabilita v rychle se měnícím digitálním prostředí činí z Binárního Brouka cenného pomocníka
  v programování a ladění kódu.""")
  elif user_input == "Regulátorový Racci":
    print ("""Regulátorový Racci je fascinující digitální tvor,
  který má schopnost udržovat rovnováhu v programovém kódu.
  Své jméno získal díky schopnosti regulovat a vyvažovat různé aspekty softwaru,
  jako je paměť a výkon. Tento raci je mistrem v detekci a opravě neefektivních algoritmů,
  což jej činí nepostradatelným v ekosystému digitální zoologické zahrady.""")
  elif user_input == "Pseudokódový Papoušek":
    print ("""Pseudokódový Papoušek je zvíře s unikátní schopností napodobovat a reprodukovat pseudokód.
  Tento papoušek je známý svým talentem pro převádění složitých algoritmů a programovacích instrukcí do jednodušší,
  lidsky srozumitelné formy. Jeho přítomnost v digitální zoologické zahradě pomáhá programátorům
  lépe porozumět a vizualizovat procesy stojící za jejich kódem.""")
  elif user_input == "Strukturovaný Simpanz":
    print ("""Strukturovaný Simpanz je zvláštní digitální tvor
  vynikající ve vytváření organizovaného a efektivního kódu.
  Tento simpanz je expert na strukturování kódu pomocí logických bloků a tříd,
  což zajišťuje čistotu a snadnou čitelnost. Jeho schopnost vnímat a implementovat strukturované programovací vzory
  činí z něj cenného průvodce světem softwarového inženýrství v naší digitální zoologické zahradě. """)
  elif user_input == "Hashový hroch":
    print ("""Hashový Hroch je zajímavé digitální zvíře,
  které se specializuje na bezpečnostní aspekty programování.
  Má schopnost vytvářet a rozpoznávat silné hashovací funkce,
  které se používají pro ochranu dat a jejich bezpečnou identifikaci.
  Tento hroch je neocenitelným strážcem datové integrity v naší digitální zoologické zahradě,
  pomáhá chránit informace před neoprávněným přístupem a manipulací.""")
  user_input = input ("""Jestli vás zajímají další zvířata tak napište "ano" pokud ne tak "ne".
  Program se poté zavře""")
  if user_input == "ano":
    print("test")
  elif user_input == "ne":
    break