#Legyen ön is milliomos
egyenleg=0
print('Első kérdés:')                                                  #ELSŐ KÉRDÉS
print('1. Melyik bolygót nevezik a „Vörös bolygónak”?')
print('A) Vénusz')
print('B) Mars') #helyes
print('C) Jupiter')
print('D) Merkúr')
helyes = input('Helyesnek vélt válasz: ').strip().upper()
if helyes=='B' or helyes=='MARS':
    print('A válasza helyes.')
    egyenleg=1000
    print(f'{egyenleg}-Ft a jelenlegi nyereménye.')
    folyt = input('Szeretné folytatni? -->').strip().upper()
    if folyt == 'IGEN' or folyt == 'YES':
        print('Második kérdés:')                                        #MÁSODIK KÉRDÉS
        print('2. Ki írta az Egri csillagok című regényt?')
        print('A) Jókai Mór')
        print('B) Mikszáth Kálmán')
        print('C) Gárdonyi Géza ')#helyes
        print('D) Móricz Zsigmond')
        helyes = input('Helyesnek vélt válasz: ').strip().upper()
        if helyes=='C' or helyes=='GÁRDONYI GÉZA':
            print('A válasza helyes.')
            egyenleg=egyenleg*10
            print(f'{egyenleg}-Ft a jelenlegi nyereménye.')
            folyt = input('Szeretné folytatni? -->').strip().upper()
            if folyt == 'IGEN' or folyt == 'YES':
                print('Harmadik kérdés:')                               #HARMADIK KÉRDÉS
                print('3. Melyik állat a legnagyobb szárazföldi emlős?')
                print('A) Zsiráf')
                print('B) Vízi bivaly')
                print('C) Afrikai elefánt') #helyes
                print('D) Orrszarvú')
                helyes = input('Helyesnek vélt válasz: ').strip().upper()
                if helyes == 'C' or helyes == 'AFRIKAI ELEFÁNT':
                    print('A válasza helyes.')
                    egyenleg = egyenleg * 10
                    print(f'{egyenleg}-Ft a jelenlegi nyereménye.')
                    folyt = input('Szeretné folytatni? -->').strip().upper()
                    if folyt == 'IGEN' or folyt == 'YES':
                        print('Negyedik kérdés:')                       #NEGYEDIK KÉRDÉS
                        print('4. Hány perc egy óra?')
                        print('A) 50')
                        print('B) 100')
                        print('C) 30')
                        print('D) 60') #helyes
                        helyes = input('Helyesnek vélt válasz: ').strip().upper()
                        if helyes == 'D' or helyes == '60':
                            print('A válasza helyes.')
                            egyenleg = egyenleg * 10
                            print(f'{egyenleg}-Ft a jelenlegi nyereménye.')
                            folyt = input('Szeretné folytatni? -->').strip().upper()
                            if folyt == 'IGEN' or folyt == 'YES':
                                print('Ötödik kérdés:')                     #ÖTÖDIK KÉRDÉS
                                print('5. Melyik ország fővárosa Helsinki?')
                                print('A) Norvégia')
                                print('B) Svédország')
                                print('C) Finnország') #helyes válasz
                                print('D) Észtország')
                                helyes = input('Helyesnek vélt válasz: ').strip().upper()
                                if helyes == 'C' or helyes == 'FINNORSZÁG':
                                    print('A válasza helyes.')
                                    egyenleg = egyenleg * 10
                                    print(f'{egyenleg}-Ft a jelenlegi nyereménye.')
                                    folyt = input('Szeretné folytatni? -->').strip().upper()
                                    if folyt == 'IGEN' or folyt == 'YES':
                                        print('Hatodik kérdés:')                        #HATODIK KÉRDÉS
                                        print('6. Milyen hangszer van Beethoven nevéhez leginkább kötve?')
                                        print('A) Hegedű')
                                        print('B) Zongora')#helyes
                                        print('C) Cselló')
                                        print('D) Fuvola')
                                        helyes = input('Helyesnek vélt válasz: ').strip().upper()
                                        if helyes == 'B' or helyes == 'ZONGORA':
                                            print('A válasza helyes.')
                                            egyenleg = egyenleg * 10
                                            print(f'{egyenleg}-Ft a jelenlegi nyereménye.')
                                            folyt = input('Szeretné folytatni? -->').strip().upper()
                                            if folyt == 'IGEN' or folyt == 'YES':
                                                print('Hetedik kérdés:')                            #HETEDIK KÉRDÉS
                                                print('7. Melyik évben tört ki az első világháború?')
                                                print('A) 1912')
                                                print('B) 1914')#helyes
                                                print('C) 1918')
                                                print('D) 1920')
                                                helyes = input('Helyesnek vélt válasz: ').strip().upper()
                                                if helyes == 'B' or helyes == '1914':
                                                    print('A válasza helyes.')
                                                    egyenleg = egyenleg * 10
                                                    print(f'{egyenleg}-Ft a jelenlegi nyereménye.')
                                                    folyt = input('Szeretné folytatni? -->').strip().upper()
                                                    if folyt == 'IGEN' or folyt == 'YES':
                                                        print('Nyolcadik kérdés:')                                  #NYOLCADIK KÉRDÉS
                                                        print('8. Melyik vitamin hiánya okozza a skorbutot?')
                                                        print('A) A-vitamin')
                                                        print('B) B12-vitamin')
                                                        print('C) D-vitamin')
                                                        print('D) C-vitamin')#helyes
                                                        helyes = input('Helyesnek vélt válasz: ').strip().upper()
                                                        if helyes == 'D' or helyes == 'C-VITAMIN' or helyes == 'CVITAMIN' or helyes == 'C VITAMIN':
                                                            print('A válasza helyes.')
                                                            egyenleg = egyenleg * 10
                                                            print(f'{egyenleg}-Ft a jelenlegi nyereménye.')
                                                            folyt = input('Szeretné folytatni? -->').strip().upper()
                                                            if folyt == 'IGEN' or folyt == 'YES':
                                                                print('Kilencedik kérdés:')                                 #KILENCEDIK KÉRDÉS
                                                                print('9. Mi Magyarország pénzneme?')
                                                                print('A) Euró')
                                                                print('B) Korona')
                                                                print('C) Forint')
                                                                print('D) Zloty')
                                                                helyes = input('Helyesnek vélt válasz: ').strip().upper()
                                                                if helyes == 'C' or helyes == 'FORINT':
                                                                    print('A válasza helyes.')
                                                                    egyenleg = egyenleg * 10
                                                                    print(f'{egyenleg}-Ft a jelenlegi nyereménye.')
                                                                    folyt = input('Szeretné folytatni? -->').strip().upper()
                                                                    if folyt == 'IGEN' or folyt == 'YES':
                                                                        print('Tizedik kérdés:')                                #TIZEDIK KÉRDÉS
                                                                        print('10. Melyik sportágban használják a „love” kifejezést?')
                                                                        print('A) Kosárlabda')
                                                                        print('B) Kézilabda')
                                                                        print('C) Tenisz')#helyes
                                                                        print('D) Röplabda')
                                                                        helyes = input('Helyesnek vélt válasz: ').strip().upper()
                                                                        if helyes == 'C' or helyes == 'TENISZ':
                                                                            print('A válasza helyes, ezennel megnyerte a vetélkedőt!!!')
                                                                            egyenleg = egyenleg * 10
                                                                            print(f'{egyenleg}-Ft a jelenlegi nyereménye, ezzel elvitte a főnyereményt!!!')
                                                                        if folyt == 'NEM' or folyt == 'NO':
                                                                            print(f'A játéka véget ért, a nyereménye {egyenleg}-Ft')
                                                                    else:
                                                                        print('A válasza helytelen. Kiesett.')
                                                                if folyt == 'NEM' or folyt == 'NO':
                                                                    print(f'A játéka véget ért, a nyereménye {egyenleg}-Ft')
                                                            else:
                                                                print('A válasza helytelen. Kiesett.')
                                                        if folyt == 'NEM' or folyt == 'NO':
                                                            print(f'A játéka véget ért, a nyereménye {egyenleg}-Ft')
                                                    else:
                                                        print('A válasza helytelen. Kiesett.')
                                                if folyt == 'NEM' or folyt == 'NO':
                                                    print(f'A játéka véget ért, a nyereménye {egyenleg}-Ft')
                                            else:
                                                print('A válasza helytelen. Kiesett.')
                                        if folyt == 'NEM' or folyt == 'NO':
                                            print(f'A játéka véget ért, a nyereménye {egyenleg}-Ft')
                                    else:
                                        print('A válasza helytelen. Kiesett.')
                                if folyt == 'NEM' or folyt == 'NO':
                                    print(f'A játéka véget ért, a nyereménye {egyenleg}-Ft')
                            else:
                                print('A válasza helytelen. Kiesett.')
                        if folyt == 'NEM' or folyt == 'NO':
                            print(f'A játéka véget ért, a nyereménye {egyenleg}-Ft')
                    else:
                        print('A válasza helytelen. Kiesett.')
            if folyt == 'NEM' or folyt == 'NO':
                print(f'A játéka véget ért, a nyereménye {egyenleg}-Ft')
        else:
            print('A válasza helytelen. Kiesett.')
    if folyt == 'NEM' or folyt == 'NO':
        print(f'A játéka véget ért, a nyereménye {egyenleg}-Ft')
else:
    print('A válasza helytelen. Kiesett.')




