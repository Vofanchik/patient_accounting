import sqlite3
from pprint import pprint


class DataBase:
    def __init__(self):
        self.id = None
        self.conn = sqlite3.connect('patients_account.db')
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS patients(
            id integer primary key,
            Data_postupleniia TEXT,
            Vremya_postuplenia text,
            Nomer_istorii_bolezni TEXT,
            Familiia TEXT,
            Imia TEXT,
            Otchestvo TEXT,
            Pol TEXT,
            Kategoriia TEXT,
            Kontraktnaia_sluzhba TEXT,
            UrO TEXT,
            UMO TEXT,
            Komandir_chasti TEXT,
            Zamestitel_komandira TEXT,
            Voinskaia_chast TEXT,
            Podrazdelenie_TerO TEXT,
            Data_rozhdeniia TEXT,
            Data_prizyva TEXT,
            Molodoi_prizyv TEXT,
            OMS TEXT,
            Po_dogovoru TEXT,
            Tekushchee_otdelenie TEXT,
            Status TEXT,
            Diagnoz TEXT,
            Nahoditsia_na_nabliudenii_u_dezhurnogo_vracha TEXT,
            ORZ TEXT,
            Pnevmoniia TEXT,
            VVK TEXT,
            Travma TEXT,
            Hirurgicheskii TEXT,
            Dolzhnost TEXT,
            Informatciia_o_rodnykh TEXT,
            Kontaktnyi_telefon TEXT,
            Obrazovanie TEXT,
            Semeinoe_polozhenie TEXT,
            Deti TEXT,
            Seriia_udostovereniia_lichnosti TEXT,
            Nomer_udostovereniia_lichnosti TEXT,
            Kem_napravlen_na_VVK TEXT,
            Perevod TEXT,
            Data_perevoda TEXT,
            Diagnoz_pri_perevode TEXT,
            Predydushchee_otdelenie TEXT,
            Tekushchee_lechebnoe_uchrezhdenie TEXT,
            Predydushchee_lechebnoe_uchrezhdenie TEXT,
            Data_vypiski TEXT,
            Vypisnoi_diagnoz TEXT,
            Data_smerti TEXT,
            Data_napravleniia text,
            Nomer_napravleniia text,
            Grazhdanstvo text,
            El_pochta text,
            Subekt_RF text,
            Raion text,
            Gorod text,
            Naselyonnyi_punkt text,
            Ulitca text,
            Dom text,
            Stroenie_Korpus text,
            Kvartira text,
            Mestnost text,        
            Mesto_raboty_ucheby text,
            Polis_obiazatelnogo_strahovaniia text,
            Data_vydachi_polisa text,
            Dannye_o_strakh_organizatcii text,
            SNILS text,
            Osnovnoi_vid_oplaty text,
            postupil_v text, 
            Forma_okazaniia_meditcinskoi_pomoshchi text )''')

        self.conn.commit()

    def add_items(self, **kwargs):  # создаем расходник
        self.cur.execute("INSERT INTO patients(Data_postupleniia, Vremya_postuplenia, Nomer_istorii_bolezni,Familiia, "
                         "Imia,Otchestvo,Pol, Kategoriia,Kontraktnaia_sluzhba,UrO, UMO,Komandir_chasti,"
                         "Zamestitel_komandira,Voinskaia_chast,Podrazdelenie_TerO,Data_rozhdeniia,Data_prizyva,"
                         "Molodoi_prizyv, OMS, Po_dogovoru,Tekushchee_otdelenie, Status,Diagnoz,"
                         "Nahoditsia_na_nabliudenii_u_dezhurnogo_vracha,ORZ,Pnevmoniia,VVK,Travma,"
                         "Hirurgicheskii,Dolzhnost,Informatciia_o_rodnykh,Kontaktnyi_telefon,Obrazovanie,"
                         "Semeinoe_polozhenie,Deti,Seriia_udostovereniia_lichnosti,Nomer_udostovereniia_lichnosti,"
                         "Kem_napravlen_na_VVK,Perevod,Data_perevoda,Diagnoz_pri_perevode,Predydushchee_otdelenie,"
                         "Tekushchee_lechebnoe_uchrezhdenie, Predydushchee_lechebnoe_uchrezhdenie,Data_vypiski,"
                         "Vypisnoi_diagnoz,Data_smerti,Data_napravleniia,Nomer_napravleniia,Grazhdanstvo,El_pochta,"
                         "Subekt_RF,Raion,Gorod,Naselyonnyi_punkt,Ulitca,Dom,Stroenie_Korpus,Kvartira,Mestnost,"
                         "Mesto_raboty_ucheby,Polis_obiazatelnogo_strahovaniia,Data_vydachi_polisa,"
                         "Dannye_o_strakh_organizatcii,SNILS,Osnovnoi_vid_oplaty, postupil_v,"
                         " Forma_okazaniia_meditcinskoi_pomoshchi) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,"
                         "?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?"
                         ",?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (kwargs['Data_postupleniia'],
                                                                            kwargs['Vremya_postuplenia'],
                                                                            kwargs['Nomer_istorii_bolezni'],
                                                                            kwargs['Familiia'],
                                                                            kwargs['Imia'],
                                                                            kwargs['Otchestvo'],
                                                                            kwargs['Pol'],
                                                                            kwargs['Kategoriia'],
                                                                            kwargs['Kontraktnaia_sluzhba'],
                                                                            kwargs['UrO'],
                                                                            kwargs['UMO'],
                                                                            kwargs['Komandir_chasti'],
                                                                            kwargs['Zamestitel_komandira'],
                                                                            kwargs['Voinskaia_chast'],
                                                                            kwargs['Podrazdelenie_TerO'],
                                                                            kwargs['Data_rozhdeniia'],
                                                                            kwargs['Data_prizyva'],
                                                                            kwargs['Molodoi_prizyv'],
                                                                            kwargs['OMS'],
                                                                            kwargs['Po_dogovoru'],
                                                                            kwargs['Tekushchee_otdelenie'],
                                                                            kwargs['Status'],
                                                                            kwargs['Diagnoz'],
                                                                            kwargs['Nahoditsia_na_nabliudenii_u_dezhurnogo_vracha'],
                                                                            kwargs['ORZ'],
                                                                            kwargs['Pnevmoniia'],
                                                                            kwargs['VVK'],
                                                                            kwargs['Travma'],
                                                                            kwargs['Hirurgicheskii'],
                                                                            kwargs['Dolzhnost'],
                                                                            kwargs['Informatciia_o_rodnykh'],
                                                                            kwargs['Kontaktnyi_telefon'],
                                                                            kwargs['Obrazovanie'],
                                                                            kwargs['Semeinoe_polozhenie'],
                                                                            kwargs['Deti'],
                                                                            kwargs['Seriia_udostovereniia_lichnosti'],
                                                                            kwargs['Nomer_udostovereniia_lichnosti'],
                                                                            kwargs['Kem_napravlen_na_VVK'],
                                                                            kwargs['Perevod'],
                                                                            kwargs['Data_perevoda'],
                                                                            kwargs['Diagnoz_pri_perevode'],
                                                                            kwargs['Predydushchee_otdelenie'],
                                                                            kwargs['Tekushchee_lechebnoe_uchrezhdenie'],
                                                                            kwargs['Predydushchee_lechebnoe_uchrezhdenie'],
                                                                            kwargs['Data_vypiski'],
                                                                            kwargs['Vypisnoi_diagnoz'],
                                                                            kwargs['Data_smerti'],
                                                                            kwargs['Data_napravleniia'],
                                                                            kwargs['Nomer_napravleniia'],
                                                                            kwargs['Grazhdanstvo'],
                                                                            kwargs['El_pochta'],
                                                                            kwargs['Subekt_RF'],
                                                                            kwargs['Raion'],
                                                                            kwargs['Gorod'],
                                                                            kwargs['Naselyonnyi_punkt'],
                                                                            kwargs['Ulitca'],
                                                                            kwargs['Dom'],
                                                                            kwargs['Stroenie_Korpus'],
                                                                            kwargs['Kvartira'],
                                                                            kwargs['Mestnost'],
                                                                            kwargs['Mesto_raboty_ucheby'],
                                                                            kwargs['Polis_obiazatelnogo_strahovaniia'],
                                                                            kwargs['Data_vydachi_polisa'],
                                                                            kwargs['Dannye_o_strakh_organizatcii'],
                                                                            kwargs['SNILS'],
                                                                            kwargs['Osnovnoi_vid_oplaty'],
                                                                            kwargs['postupil_v'],
                                                                            kwargs['Forma_okazaniia_meditcinskoi_pomoshchi'],))
        self.conn.commit()

        return self.cur.lastrowid

    def show_patients(self):
        return self.cur.execute('''SELECT * FROM patients''').fetchall()

    def show_parients_fio_story(self):
        return self.cur.execute('''SELECT id,Data_postupleniia,Vremya_postuplenia,Nomer_istorii_bolezni,Familiia,Imia,Otchestvo
         FROM patients''').fetchall()

    def show_patient_by_id(self, pat_id):
        pl = self.cur.execute('''SELECT * FROM patients where id = (?)''',(pat_id,)).fetchone()
        pat_dict = {'id':pl[0],
                    'Data_postupleniia':pl[1],
                    'Vremya_postuplenia':pl[2],
                    'Nomer_istorii_bolezni':pl[3],
                    'Familiia':pl[4],
                    'Imia':pl[5],
                    'Otchestvo':pl[6],
                    'Pol':pl[7],
                    'Kategoriia':pl[8],
                    'Kontraktnaia_sluzhba':pl[9],
                    'UrO':pl[10],
                    'UMO':pl[11],
                    'Komandir_chasti':pl[12],
                    'Zamestitel_komandira':pl[13],
                    'Voinskaia_chast':pl[14],
                    'Podrazdelenie_TerO':pl[15],
                    'Data_rozhdeniia':pl[16],
                    'Data_prizyva':pl[17],
                    'Molodoi_prizyv':pl[18],
                    'OMS':pl[19],
                    'Po_dogovoru':pl[20],
                    'Tekushchee_otdelenie':pl[21],
                    'Status':pl[22],
                    'Diagnoz':pl[23],
                    'Nahoditsia_na_nabliudenii_u_dezhurnogo_vracha':pl[24],
                    'ORZ':pl[25],
                    'Pnevmoniia':pl[26],
                    'VVK':pl[27],
                    'Travma':pl[28],
                    'Hirurgicheskii':pl[29],
                    'Dolzhnost':pl[30],
                    'Informatciia_o_rodnykh':pl[31],
                    'Kontaktnyi_telefon':pl[32],
                    'Obrazovanie':pl[33],
                    'Semeinoe_polozhenie':pl[34],
                    'Deti':pl[35],
                    'Seriia_udostovereniia_lichnosti':pl[36],
                    'Nomer_udostovereniia_lichnosti':pl[37],
                    'Kem_napravlen_na_VVK':pl[38],
                    'Perevod':pl[39],
                    'Data_perevoda':pl[40],
                    'Diagnoz_pri_perevode':pl[41],
                    'Predydushchee_otdelenie':pl[42],
                    'Tekushchee_lechebnoe_uchrezhdenie':pl[43],
                    'Predydushchee_lechebnoe_uchrezhdenie':pl[44],
                    'Data_vypiski':pl[45],
                    'Vypisnoi_diagnoz':pl[46],
                    'Data_smerti':pl[47],
                    'Data_napravleniia':pl[48],
                    'Nomer_napravleniia':pl[49],
                    'Grazhdanstvo':pl[50],
                    'El_pochta':pl[51],
                    'Subekt_RF':pl[52],
                    'Raion':pl[53],
                    'Gorod':pl[54],
                    'Naselyonnyi_punkt':pl[55],
                    'Ulitca':pl[56],
                    'Dom':pl[57],
                    'Stroenie_Korpus':pl[58],
                    'Kvartira':pl[59],
                    'Mestnost':pl[60],
                    'Mesto_raboty_ucheby':pl[61],
                    'Polis_obiazatelnogo_strahovaniia':pl[62],
                    'Data_vydachi_polisa':pl[63],
                    'Dannye_o_strakh_organizatcii':pl[64],
                    'SNILS':pl[65],
                    'Osnovnoi_vid_oplaty':pl[66],
                    'postupil_v': pl[67],
                    'Forma_okazaniia_meditcinskoi_pomoshchi': pl[68]

}
        return pat_dict

    def update_patient(self, pat_id, **kwargs):
        self.cur.execute("UPDATE patients SET "
                        "Data_postupleniia = ?,"
                        "Vremya_postuplenia = ?,"
                        "Nomer_istorii_bolezni = ?,"
                        "Familiia = ?,"
                        "Imia = ?,"
                        "Otchestvo = ?,"
                        "Pol = ?,"
                        "Kategoriia = ?,"
                        "Kontraktnaia_sluzhba = ?,"
                        "UrO = ?,"
                        "UMO = ?,"
                        "Komandir_chasti = ?,"
                        "Zamestitel_komandira = ?,"
                        "Voinskaia_chast = ?,"
                        "Podrazdelenie_TerO = ?,"
                        "Data_rozhdeniia = ?,"
                        "Data_prizyva = ?,"
                        "Molodoi_prizyv = ?,"
                        "OMS = ?,"
                        "Po_dogovoru = ?,"
                        "Tekushchee_otdelenie = ?,"
                        "Status = ?,"
                        "Diagnoz = ?,"
                        "Nahoditsia_na_nabliudenii_u_dezhurnogo_vracha = ?,"
                        "ORZ = ?,"
                        "Pnevmoniia = ?,"
                        "VVK = ?,"
                        "Travma = ?,"
                        "Hirurgicheskii = ?,"
                        "Dolzhnost = ?,"
                        "Informatciia_o_rodnykh = ?,"
                        "Kontaktnyi_telefon = ?,"
                        "Obrazovanie = ?,"
                        "Semeinoe_polozhenie = ?,"
                        "Deti = ?,"
                        "Seriia_udostovereniia_lichnosti = ?,"
                        "Nomer_udostovereniia_lichnosti = ?,"
                        "Kem_napravlen_na_VVK = ?,"
                        "Perevod = ?,"
                        "Data_perevoda = ?,"
                        "Diagnoz_pri_perevode = ?,"
                        "Predydushchee_otdelenie = ?,"
                        "Tekushchee_lechebnoe_uchrezhdenie = ?,"
                        "Predydushchee_lechebnoe_uchrezhdenie = ?,"
                        "Data_vypiski = ?,"
                        "Vypisnoi_diagnoz = ?,"
                        "Data_smerti = ?,"
                        "Data_napravleniia = ?,"
                        "Nomer_napravleniia = ?,"
                        "Grazhdanstvo = ?,"
                        "El_pochta = ?,"
                        "Subekt_RF = ?,"
                        "Raion = ?,"
                        "Gorod = ?,"
                        "Naselyonnyi_punkt = ?,"
                        "Ulitca = ?,"
                        "Dom = ?,"
                        "Stroenie_Korpus = ?,"
                        "Kvartira = ?,"
                        "Mestnost = ?,"
                        "Mesto_raboty_ucheby = ?,"
                        "Polis_obiazatelnogo_strahovaniia = ?,"
                        "Data_vydachi_polisa = ?,"
                        "Dannye_o_strakh_organizatcii = ?,"
                        "SNILS = ?,"
                        "Osnovnoi_vid_oplaty = ?,"
                        "postupil_v = ?,"
                        "Forma_okazaniia_meditcinskoi_pomoshchi = ?"
                         

                         " where id = {}".format(pat_id), (kwargs['Data_postupleniia'],
                                                            kwargs['Vremya_postuplenia'],
                                                            kwargs['Nomer_istorii_bolezni'],
                                                            kwargs['Familiia'],
                                                            kwargs['Imia'],
                                                            kwargs['Otchestvo'],
                                                            kwargs['Pol'],
                                                            kwargs['Kategoriia'],
                                                            kwargs['Kontraktnaia_sluzhba'],
                                                            kwargs['UrO'],
                                                            kwargs['UMO'],
                                                            kwargs['Komandir_chasti'],
                                                            kwargs['Zamestitel_komandira'],
                                                            kwargs['Voinskaia_chast'],
                                                            kwargs['Podrazdelenie_TerO'],
                                                            kwargs['Data_rozhdeniia'],
                                                            kwargs['Data_prizyva'],
                                                            kwargs['Molodoi_prizyv'],
                                                            kwargs['OMS'],
                                                            kwargs['Po_dogovoru'],
                                                            kwargs['Tekushchee_otdelenie'],
                                                            kwargs['Status'],
                                                            kwargs['Diagnoz'],
                                                            kwargs['Nahoditsia_na_nabliudenii_u_dezhurnogo_vracha'],
                                                            kwargs['ORZ'],
                                                            kwargs['Pnevmoniia'],
                                                            kwargs['VVK'],
                                                            kwargs['Travma'],
                                                            kwargs['Hirurgicheskii'],
                                                            kwargs['Dolzhnost'],
                                                            kwargs['Informatciia_o_rodnykh'],
                                                            kwargs['Kontaktnyi_telefon'],
                                                            kwargs['Obrazovanie'],
                                                            kwargs['Semeinoe_polozhenie'],
                                                            kwargs['Deti'],
                                                            kwargs['Seriia_udostovereniia_lichnosti'],
                                                            kwargs['Nomer_udostovereniia_lichnosti'],
                                                            kwargs['Kem_napravlen_na_VVK'],
                                                            kwargs['Perevod'],
                                                            kwargs['Data_perevoda'],
                                                            kwargs['Diagnoz_pri_perevode'],
                                                            kwargs['Predydushchee_otdelenie'],
                                                            kwargs['Tekushchee_lechebnoe_uchrezhdenie'],
                                                            kwargs['Predydushchee_lechebnoe_uchrezhdenie'],
                                                            kwargs['Data_vypiski'],
                                                            kwargs['Vypisnoi_diagnoz'],
                                                            kwargs['Data_smerti'],
                                                            kwargs['Data_napravleniia'],
                                                            kwargs['Nomer_napravleniia'],
                                                            kwargs['Grazhdanstvo'],
                                                            kwargs['El_pochta'],
                                                            kwargs['Subekt_RF'],
                                                            kwargs['Raion'],
                                                            kwargs['Gorod'],
                                                            kwargs['Naselyonnyi_punkt'],
                                                            kwargs['Ulitca'],
                                                            kwargs['Dom'],
                                                            kwargs['Stroenie_Korpus'],
                                                            kwargs['Kvartira'],
                                                            kwargs['Mestnost'],
                                                            kwargs['Mesto_raboty_ucheby'],
                                                            kwargs['Polis_obiazatelnogo_strahovaniia'],
                                                            kwargs['Data_vydachi_polisa'],
                                                            kwargs['Dannye_o_strakh_organizatcii'],
                                                            kwargs['SNILS'],
                                                            kwargs['Osnovnoi_vid_oplaty'],
                                                            kwargs['postupil_v'],
                                                            kwargs['Forma_okazaniia_meditcinskoi_pomoshchi'],
                                                           ))
        self.conn.commit()

    def delete_patient(self, id_patient: int):
        self.cur.execute('DELETE from patients where id = {}'.format(id_patient))
        self.conn.commit()

if __name__ == '__main__':
    db = DataBase()
    pprint(db.show_patient_by_id(9))
    # b = 'Data_postupleniia,Vremya_postuplenia,Nomer_istorii_bolezni,Familiia,Imia,Otchestvo,Pol,Kategoriia,Kontraktnaia_sluzhba,UrO,UMO,Komandir_chasti,Zamestitel_komandira,Voinskaia_chast,Podrazdelenie_TerO,Data_rozhdeniia,Data_prizyva,Molodoi_prizyv,OMS,Po_dogovoru,Tekushchee_otdelenie,Status,Diagnoz,Nahoditsia_na_nabliudenii_u_dezhurnogo_vracha,ORZ,Pnevmoniia,VVK,Travma,Hirurgicheskii,Dolzhnost,Informatciia_o_rodnykh,Kontaktnyi_telefon,Obrazovanie,Semeinoe_polozhenie,Deti,Seriia_udostovereniia_lichnosti,Nomer_udostovereniia_lichnosti,Kem_napravlen_na_VVK,Perevod,Data_perevoda,Diagnoz_pri_perevode,Predydushchee_otdelenie,Tekushchee_lechebnoe_uchrezhdenie,Predydushchee_lechebnoe_uchrezhdenie,Data_vypiski,Vypisnoi_diagnoz,Data_smerti,Data_napravleniia,Nomer_napravleniia,Grazhdanstvo,El_pochta,Subekt_RF,Raion,Gorod,Naselyonnyi_punkt,Ulitca,Dom,Stroenie_Korpus,Kvartira,Mestnost,Mesto_raboty_ucheby,Polis_obiazatelnogo_strahovaniia,Data_vydachi_polisa,Dannye_o_strakh_organizatcii,SNILS,Osnovnoi_vid_oplaty'
    # for i in b.split(','):
    #     print(f"kwargs['{i}'],")