import sys
from datetime import datetime

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QFileDialog, QMessageBox
from docxtpl import DocxTemplate

from DataBase import DataBase
from UI_files.MainWindow import Ui_MainWindow
import selects


def from_dot_to_rec(how, dt):
    if how == 0:
        return datetime.strptime(dt, '%d.%m.%Y').strftime('%Y-%m-%d')
    else:return datetime.strptime(dt, '%Y-%m-%d').strftime('%d.%m.%Y')

def from_str_to_date(how, date_str):
    if how == 0:
        return datetime.strptime(date_str, '%d.%m.%Y')
    else: return datetime.strptime(date_str, '%Y-%m-%d')

def from_str_to_time(tm_str):
    return datetime.strptime(tm_str, '%H:%M').time()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.id=None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add_new_patient)
        self.ui.pushButton_2.clicked.connect(self.form_story)
        self.ui.pushButton_3.clicked.connect(self.delete_patient)
        self.ui.pushButton_5.clicked.connect(self.change_patient)

        self.ui.dateEdit_7.setDate(datetime.now())
        self.ui.timeEdit.setTime(datetime.now().time())
        self.complete_combos()
        self.fill_patient_table(db.show_parients_fio_story())
        self.ui.checkBox.stateChanged.connect(self.checkbox_changed)
        self.ui.comboBox_13.currentIndexChanged.connect(self.status_changed)

        self.ui.tableWidget.setColumnHidden(2, True)
        self.ui.tableWidget.itemDoubleClicked.connect(self.call_exist_patient)

    def call_exist_patient(self):
        self.id = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 2).text()
        context = db.show_patient_by_id(self.id)
        ui = self.ui
        ui.dateEdit_7.setDate(from_str_to_date(1,context['Data_postupleniia']))
        ui.timeEdit.setTime(from_str_to_time(context['Vremya_postuplenia']))
        ui.lineEdit_49.setText(context['Nomer_istorii_bolezni'])
        ui.lineEdit_48.setText(context['Familiia'])
        ui.lineEdit_47.setText(context['Imia'])
        ui.lineEdit_46.setText(context['Otchestvo'])
        ui.comboBox.setCurrentText(context['Pol'])
        ui.comboBox_2.setCurrentText(context['Kategoriia'])
        ui.comboBox_3.setCurrentText(context['Kontraktnaia_sluzhba'])
        ui.comboBox_4.setCurrentText(context['UrO'])
        ui.comboBox_5.setCurrentText(context['UMO'])
        ui.comboBox_6.setCurrentText(context['Komandir_chasti'])
        ui.comboBox_7.setCurrentText(context['Zamestitel_komandira'])
        ui.comboBox_8.setCurrentText(context['Voinskaia_chast'])
        ui.lineEdit_37.setText(context['Podrazdelenie_TerO'])
        ui.dateEdit.setDate(from_str_to_date(0,context['Data_rozhdeniia']))
        ui.dateEdit_2.setDate(from_str_to_date(0,context['Data_prizyva']))
        ui.comboBox_9.setCurrentText(context['Molodoi_prizyv'])
        ui.comboBox_10.setCurrentText(context['OMS'])
        ui.comboBox_11.setCurrentText(context['Po_dogovoru'])
        ui.comboBox_12.setCurrentText(context['Tekushchee_otdelenie'])
        ui.comboBox_13.setCurrentText(context['Status'])
        ui.lineEdit_29.setText(context['Diagnoz'])
        ui.comboBox_14.setCurrentText(context['Nahoditsia_na_nabliudenii_u_dezhurnogo_vracha'])
        ui.comboBox_15.setCurrentText(context['ORZ'])
        ui.comboBox_16.setCurrentText(context['Pnevmoniia'])
        ui.comboBox_17.setCurrentText(context['VVK'])
        ui.comboBox_18.setCurrentText(context['Travma'])
        ui.comboBox_19.setCurrentText(context['Hirurgicheskii'])
        ui.lineEdit_22.setText(context['Dolzhnost'])
        ui.lineEdit_21.setText(context['Informatciia_o_rodnykh'])
        ui.lineEdit_19.setText(context['Kontaktnyi_telefon'])
        ui.comboBox_23.setCurrentText(context['Obrazovanie'])
        ui.comboBox_22.setCurrentText(context['Semeinoe_polozhenie'])
        ui.lineEdit_16.setText(context['Deti'])
        ui.lineEdit_15.setText(context['Seriia_udostovereniia_lichnosti'])
        ui.lineEdit_14.setText(context['Nomer_udostovereniia_lichnosti'])
        ui.lineEdit_12.setText(context['Kem_napravlen_na_VVK'])
        ui.lineEdit_35.setText(context['Tekushchee_lechebnoe_uchrezhdenie'])
        ui.lineEdit_6.setText(context['Predydushchee_lechebnoe_uchrezhdenie'])
        ui.lineEdit_3.setText(context['Vypisnoi_diagnoz'])
        ui.dateEdit_4.setDate(from_str_to_date(0,context['Data_vypiski']))
        ui.dateEdit_6.setDate(from_str_to_date(0,context['Data_napravleniia']))
        ui.lineEdit.setText(context['Nomer_napravleniia'])
        ui.lineEdit_5.setText(context['Grazhdanstvo'])
        ui.lineEdit_41.setText(context['El_pochta'])
        ui.lineEdit_28.setText(context['Subekt_RF'])
        ui.lineEdit_42.setText(context['Raion'])
        ui.lineEdit_7.setText(context['Gorod'])
        ui.lineEdit_33.setText(context['Naselyonnyi_punkt'])
        ui.lineEdit_27.setText(context['Ulitca'])
        ui.lineEdit_38.setText(context['Dom'])
        ui.lineEdit_25.setText(context['Stroenie_Korpus'])
        ui.lineEdit_30.setText(context['Kvartira'])
        ui.comboBox_21.setCurrentText(context['Mestnost'])
        ui.lineEdit_23.setText(context['Mesto_raboty_ucheby'])
        ui.lineEdit_32.setText(context['Polis_obiazatelnogo_strahovaniia'])
        ui.lineEdit_39.setText(context['Dannye_o_strakh_organizatcii'])
        ui.lineEdit_34.setText(context['SNILS'])
        ui.dateEdit_8.setDate(from_str_to_date(0,context['Data_vydachi_polisa']))
        ui.comboBox_24.setCurrentText(context['Osnovnoi_vid_oplaty'])

        ui.lineEdit_9.setText(context['Diagnoz_pri_perevode'])
        ui.comboBox_20.setCurrentText(context['Predydushchee_otdelenie'])
        ui.dateEdit_3.setDate(from_str_to_date(0,context['Data_perevoda']))

        ui.dateEdit_5.setDate(from_str_to_date(0, context['Data_smerti']))

        ui.comboBox_25.setCurrentText(context['postupil_v'])
        ui.comboBox_26.setCurrentText(context['Forma_okazaniia_meditcinskoi_pomoshchi'])

        if context['Perevod'] == '':
            ui.checkBox.setChecked(False)
        else:ui.checkBox.setChecked(True)

        if context['Status'] == 'Умер':
            ui.dateEdit_5.setDisabled(False)

    def status_changed(self):
        if self.ui.comboBox_13.currentText()== 'Умер':
            self.ui.dateEdit_5.setDisabled(False)
        else: self.ui.dateEdit_5.setDisabled(True)

    def checkbox_changed(self):
        if self.ui.checkBox.checkState() == 0:
            self.ui.dateEdit_3.setDisabled(True)
            self.ui.lineEdit_9.setDisabled(True)
            self.ui.comboBox_20.setDisabled(True)
        else:
            self.ui.dateEdit_3.setDisabled(False)
            self.ui.lineEdit_9.setDisabled(False)
            self.ui.comboBox_20.setDisabled(False)

    def add_new_patient(self):
        ui = self.ui
        patient_info = {'Data_postupleniia': from_dot_to_rec(how=0, dt=self.ui.dateEdit_7.text()),
                        'Vremya_postuplenia': ui.timeEdit.text(),
                        'Nomer_istorii_bolezni': ui.lineEdit_49.text(),
                        'Familiia': ui.lineEdit_48.text(),
                        'Imia':ui.lineEdit_47.text(),
                        'Otchestvo': ui.lineEdit_46.text(),
                        'Pol': ui.comboBox.currentText(),
                        'Kategoriia': ui.comboBox_2.currentText(),
                        'Kontraktnaia_sluzhba': ui.comboBox_3.currentText(),
                        'UrO': ui.comboBox_4.currentText(),
                        'UMO': ui.comboBox_5.currentText(),
                        'Komandir_chasti': ui.comboBox_6.currentText(),
                        'Zamestitel_komandira': ui.comboBox_7.currentText(),
                        'Voinskaia_chast': ui.comboBox_8.currentText(),
                        'Podrazdelenie_TerO': ui.lineEdit_37.text(),
                        'Data_rozhdeniia': ui.dateEdit.text(),
                        'Data_prizyva': ui.dateEdit_2.text(),
                        'Molodoi_prizyv': ui.comboBox_9.currentText(),
                        'OMS': ui.comboBox_10.currentText(),
                        'Po_dogovoru': ui.comboBox_11.currentText(),
                        'Tekushchee_otdelenie': ui.comboBox_12.currentText(),
                        'Status': ui.comboBox_13.currentText(),
                        'Diagnoz': ui.lineEdit_29.text(),
                        'Nahoditsia_na_nabliudenii_u_dezhurnogo_vracha': ui.comboBox_14.currentText(),
                        'ORZ': ui.comboBox_15.currentText(),
                        'Pnevmoniia': ui.comboBox_16.currentText(),
                        'VVK':ui.comboBox_17.currentText(),
                        'Travma': ui.comboBox_18.currentText(),
                        'Hirurgicheskii': ui.comboBox_19.currentText(),
                        'Dolzhnost': ui.lineEdit_22.text(),
                        'Informatciia_o_rodnykh': ui.lineEdit_21.text(),
                        'Kontaktnyi_telefon': ui.lineEdit_19.text(),
                        'Obrazovanie': ui.comboBox_23.currentText(),
                        'Semeinoe_polozhenie': ui.comboBox_22.currentText(),
                        'Deti': ui.lineEdit_16.text(),
                        'Seriia_udostovereniia_lichnosti': ui.lineEdit_15.text(),
                        'Nomer_udostovereniia_lichnosti': ui.lineEdit_14.text(),
                        'Kem_napravlen_na_VVK': ui.lineEdit_12.text(),
                        'Tekushchee_lechebnoe_uchrezhdenie': ui.lineEdit_35.text(),
                        'Predydushchee_lechebnoe_uchrezhdenie': ui.lineEdit_6.text(),
                        'Data_vypiski': ui.dateEdit_4.text(),
                        'Vypisnoi_diagnoz': ui.lineEdit_3.text(),

                        'Data_napravleniia':ui.dateEdit_6.text(),
                        'Nomer_napravleniia': ui.lineEdit.text(),
                        'Grazhdanstvo': ui.lineEdit_5.text(),
                        'El_pochta': ui.lineEdit_41.text(),
                        'Subekt_RF': ui.lineEdit_28.text(),
                        'Raion': ui.lineEdit_42.text(),
                        'Gorod': ui.lineEdit_7.text(),
                        'Naselyonnyi_punkt': ui.lineEdit_33.text(),
                        'Ulitca': ui.lineEdit_27.text(),
                        'Dom': ui.lineEdit_38.text(),
                        'Stroenie_Korpus': ui.lineEdit_25.text(),
                        'Kvartira': ui.lineEdit_30.text(),
                        'Mestnost': ui.comboBox_21.currentText(),
                        'Mesto_raboty_ucheby': ui.lineEdit_23.text(),
                        'Polis_obiazatelnogo_strahovaniia': ui.lineEdit_32.text(),
                        'Data_vydachi_polisa': ui.dateEdit_8.text(),
                        'Dannye_o_strakh_organizatcii': ui.lineEdit_39.text(),
                        'SNILS': ui.lineEdit_34.text(),
                        'Osnovnoi_vid_oplaty': ui.comboBox_24.currentText(),
                        'postupil_v': ui.comboBox_25.currentText(),
                        'Forma_okazaniia_meditcinskoi_pomoshchi': ui.comboBox_26.currentText()

}
        if ui.checkBox.checkState() == 2:
            patient_info['Perevod'] = 'из отделения в отделение'
            patient_info['Data_perevoda'] = ui.dateEdit_3.text()
            patient_info['Diagnoz_pri_perevode'] = ui.lineEdit_9.text()
            patient_info['Predydushchee_otdelenie'] = ui.comboBox_20.currentText()
        else:
            patient_info['Perevod'] = ''
            patient_info['Data_perevoda'] = '01.01.1800'
            patient_info['Diagnoz_pri_perevode'] = ''
            patient_info['Predydushchee_otdelenie'] = ''


        if self.ui.comboBox_13.currentText()== 'Умер':
            patient_info['Data_smerti']=ui.dateEdit_5.text()
        else:
            patient_info['Data_smerti'] = '01.01.1800'
        db.add_items(**patient_info)
        # print(patient_info)
        self.fill_patient_table(db.show_parients_fio_story())

    def complete_combos(self):
        ui = self.ui
        ui.comboBox.addItems(selects.pol)
        ui.comboBox_2.addItems(selects.Kategoriia)
        ui.comboBox_3.addItems(selects.y_n)
        ui.comboBox_4.addItems(selects.y_n)
        ui.comboBox_5.addItems(selects.y_n)
        ui.comboBox_6.addItems(selects.y_n)
        ui.comboBox_7.addItems(selects.y_n)
        ui.comboBox_8.addItems(selects.Voinskaia_chast)
        ui.comboBox_9.addItems(selects.y_n)
        ui.comboBox_10.addItems(selects.y_n)
        ui.comboBox_11.addItems(selects.y_n)
        ui.comboBox_12.addItems(selects.otdelenie)
        ui.comboBox_13.addItems(selects.status)
        ui.comboBox_14.addItems(selects.y_n)
        ui.comboBox_15.addItems(selects.y_n)
        ui.comboBox_16.addItems(selects.y_n)
        ui.comboBox_17.addItems(selects.y_n)
        ui.comboBox_18.addItems(selects.y_n)
        ui.comboBox_19.addItems(selects.y_n)
        ui.comboBox_20.addItems(selects.otdelenie)
        ui.comboBox_21.addItems(selects.Mestnost)
        ui.comboBox_22.addItems(selects.Semeinoe_polozhenie)
        ui.comboBox_23.addItems(selects.Obrazovanie)
        ui.comboBox_24.addItems(selects.Osnovnoi_vid_oplaty)
        ui.comboBox_25.addItems(selects.postupil_v)
        ui.comboBox_26.addItems(selects.Forma_okazaniia_meditcinskoi_pomoshchi)

    def fill_patient_table(self, pats_list):
        patients_list_dict = []
        for pats in pats_list:
            patient = { 'id': pats[0],
                        'Data_postupleniia': pats[1],
                        'Vremya_postuplenia': pats[2],
                        'Nomer_istorii_bolezni': pats[3],
                        'Familiia': pats[4],
                        'Imia':pats[5],
                        'Otchestvo': pats[6]}

            patients_list_dict.append(patient)

        if patients_list_dict == []:
            self.ui.tableWidget.setRowCount(0)
        else:
            for co, it in enumerate(patients_list_dict):
                self.ui.tableWidget.setRowCount(co + 1)
                self.ui.tableWidget.setItem(co, 1, QTableWidgetItem("{}".format(it['Familiia']+
                                                                                " "+it['Imia']+" "+it['Otchestvo'])))
                self.ui.tableWidget.setItem(co, 0, QTableWidgetItem("{}".format(it['Nomer_istorii_bolezni'])))
                self.ui.tableWidget.setItem(co, 2, QTableWidgetItem("{}".format(it['id'])))

    def form_story(self):
        try:
            self.id = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 2).text()
            context = db.show_patient_by_id(self.id)
            context['Data_postupleniia'] = from_dot_to_rec(1, context['Data_postupleniia'])
            if context['Tekushchee_otdelenie'] in selects.otdelenie[:9]:
                context['profil_coec'] = 'Хирургический'

            else: context['profil_coec'] = 'Терапевтический'

            if context['Data_vydachi_polisa'] == '01.01.2000':
                context['Data_vydachi_polisa'] = ''

            if context['Kontraktnaia_sluzhba'] == 'да':
                context['ks'] = 'к/с'

            fname = QFileDialog.getSaveFileName(self, 'Save file',
                                                '', "MS Office Document text files (*.docx)")

            tpl = DocxTemplate('Source_tpl.docx')
            tpl.render(context)
            tpl.save(fname[0])

            tpl_sk = DocxTemplate('SK_tpl.docx')
            tpl_sk.render(context)
            tpl_sk.save(str(fname[0]).replace('.docx', ' стат карта.docx'))

        except: QMessageBox().warning(self, 'Предупреждение', "Выберите пациента", QMessageBox().Ok)

    def delete_patient(self):
        try:
            self.id = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 2).text()
            if QMessageBox().critical(self, 'Предупреждение', "Удалить {}?".format(self.ui.tableWidget.item
                                                                                       (self.ui.tableWidget.currentRow(),
                                                                                        1).text()),
                                   QMessageBox().Ok | QMessageBox.Cancel) == 1024:
                db.delete_patient(self.id)
                self.fill_patient_table(db.show_parients_fio_story())
        except:
            QMessageBox().warning(self, 'Предупреждение', "Выберите пациента", QMessageBox().Ok)

    def change_patient(self):
        try:
            ui = self.ui
            self.id = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 2).text()
            if QMessageBox().critical(self, 'Предупреждение', "Изменить {}?".format(self.ui.tableWidget.item
                                                                                       (self.ui.tableWidget.currentRow(),
                                                                                        1).text()),
                                      QMessageBox().Ok | QMessageBox.Cancel) == 1024:
                patient_info = {'Data_postupleniia': from_dot_to_rec(how=0, dt=self.ui.dateEdit_7.text()),
                                'Vremya_postuplenia': ui.timeEdit.text(),
                                'Nomer_istorii_bolezni': ui.lineEdit_49.text(),
                                'Familiia': ui.lineEdit_48.text(),
                                'Imia': ui.lineEdit_47.text(),
                                'Otchestvo': ui.lineEdit_46.text(),
                                'Pol': ui.comboBox.currentText(),
                                'Kategoriia': ui.comboBox_2.currentText(),
                                'Kontraktnaia_sluzhba': ui.comboBox_3.currentText(),
                                'UrO': ui.comboBox_4.currentText(),
                                'UMO': ui.comboBox_5.currentText(),
                                'Komandir_chasti': ui.comboBox_6.currentText(),
                                'Zamestitel_komandira': ui.comboBox_7.currentText(),
                                'Voinskaia_chast': ui.comboBox_8.currentText(),
                                'Podrazdelenie_TerO': ui.lineEdit_37.text(),
                                'Data_rozhdeniia': ui.dateEdit.text(),
                                'Data_prizyva': ui.dateEdit_2.text(),
                                'Molodoi_prizyv': ui.comboBox_9.currentText(),
                                'OMS': ui.comboBox_10.currentText(),
                                'Po_dogovoru': ui.comboBox_11.currentText(),
                                'Tekushchee_otdelenie': ui.comboBox_12.currentText(),
                                'Status': ui.comboBox_13.currentText(),
                                'Diagnoz': ui.lineEdit_29.text(),
                                'Nahoditsia_na_nabliudenii_u_dezhurnogo_vracha': ui.comboBox_14.currentText(),
                                'ORZ': ui.comboBox_15.currentText(),
                                'Pnevmoniia': ui.comboBox_16.currentText(),
                                'VVK': ui.comboBox_17.currentText(),
                                'Travma': ui.comboBox_18.currentText(),
                                'Hirurgicheskii': ui.comboBox_19.currentText(),
                                'Dolzhnost': ui.lineEdit_22.text(),
                                'Informatciia_o_rodnykh': ui.lineEdit_21.text(),
                                'Kontaktnyi_telefon': ui.lineEdit_19.text(),
                                'Obrazovanie': ui.comboBox_23.currentText(),
                                'Semeinoe_polozhenie': ui.comboBox_22.currentText(),
                                'Deti': ui.lineEdit_16.text(),
                                'Seriia_udostovereniia_lichnosti': ui.lineEdit_15.text(),
                                'Nomer_udostovereniia_lichnosti': ui.lineEdit_14.text(),
                                'Kem_napravlen_na_VVK': ui.lineEdit_12.text(),
                                'Tekushchee_lechebnoe_uchrezhdenie': ui.lineEdit_35.text(),
                                'Predydushchee_lechebnoe_uchrezhdenie': ui.lineEdit_6.text(),
                                'Data_vypiski': ui.dateEdit_4.text(),
                                'Vypisnoi_diagnoz': ui.lineEdit_3.text(),

                                'Data_napravleniia': ui.dateEdit_6.text(),
                                'Nomer_napravleniia': ui.lineEdit.text(),
                                'Grazhdanstvo': ui.lineEdit_5.text(),
                                'El_pochta': ui.lineEdit_41.text(),
                                'Subekt_RF': ui.lineEdit_28.text(),
                                'Raion': ui.lineEdit_42.text(),
                                'Gorod': ui.lineEdit_7.text(),
                                'Naselyonnyi_punkt': ui.lineEdit_33.text(),
                                'Ulitca': ui.lineEdit_27.text(),
                                'Dom': ui.lineEdit_38.text(),
                                'Stroenie_Korpus': ui.lineEdit_25.text(),
                                'Kvartira': ui.lineEdit_30.text(),
                                'Mestnost': ui.comboBox_21.currentText(),
                                'Mesto_raboty_ucheby': ui.lineEdit_23.text(),
                                'Polis_obiazatelnogo_strahovaniia': ui.lineEdit_32.text(),
                                'Data_vydachi_polisa': ui.dateEdit_8.text(),
                                'Dannye_o_strakh_organizatcii': ui.lineEdit_39.text(),
                                'SNILS': ui.lineEdit_34.text(),
                                'Osnovnoi_vid_oplaty': ui.comboBox_24.currentText(),
                                'postupil_v': ui.comboBox_25.currentText(),
                                'Forma_okazaniia_meditcinskoi_pomoshchi': ui.comboBox_26.currentText()
                                }
                if ui.checkBox.checkState() == 2:
                    patient_info['Perevod'] = 'из отделения в отделение'
                    patient_info['Data_perevoda'] = ui.dateEdit_3.text()
                    patient_info['Diagnoz_pri_perevode'] = ui.lineEdit_9.text()
                    patient_info['Predydushchee_otdelenie'] = ui.comboBox_20.currentText()
                else:
                    patient_info['Perevod'] = ''
                    patient_info['Data_perevoda'] = '01.01.1800'
                    patient_info['Diagnoz_pri_perevode'] = ''
                    patient_info['Predydushchee_otdelenie'] = ''

                if self.ui.comboBox_13.currentText()== 'Умер':
                    patient_info['Data_smerti']=ui.dateEdit_5.text()
                else:
                    patient_info['Data_smerti'] = '01.01.1800'

                db.update_patient(self.id, **patient_info)
                self.fill_patient_table(db.show_parients_fio_story())
        except: QMessageBox().warning(self, 'Предупреждение', "Выберите пациента", QMessageBox().Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = DataBase()
    mw = MainWindow()

    mw.setWindowIcon(QIcon(QPixmap('UI_files/patient.gif')))

    mw.show()

    sys.exit(app.exec_())