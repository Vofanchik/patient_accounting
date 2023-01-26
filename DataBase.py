import sqlite3

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
            Domashnii_adres TEXT,
            Kontaktnyi_telefon TEXT,
            Obrazovanie TEXT,
            Semeinoe_polozhenie TEXT,
            Deti TEXT,
            Seriia_udostovereniia_lichnosti TEXT,
            Nomer_udostovereniia_lichnosti TEXT,
            Nomer_strahovogo_polisa TEXT,
            Kem_napravlen_na_VVK TEXT,
            Perevod TEXT,
            Data_perevoda TEXT,
            Diagnoz_pri_perevode TEXT,
            Predydushchee_otdelenie TEXT,
            Tekushchee_otdelenie TEXT,
            Tekushchee_lechebnoe_uchrezhdenie TEXT,
            Predydushchee_lechebnoe_uchrezhdenie TEXT,
            Status TEXT,
            Data_vypiski TEXT,
            Vypisnoi_diagnoz TEXT,
            Data_smerti TEXT,

           
           
           story text NOT NULL UNIQUE,
           fio text NOT NULL, 
           date_start_illness TEXT,
           date_end_illness TEXT,
           cost real,
           status TEXT,
           division TEXT,
            UNIQUE ("story") ON CONFLICT IGNORE)''')
        self.conn.commit()