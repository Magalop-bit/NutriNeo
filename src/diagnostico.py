from PyQt6.QtWidgets import * # type: ignore
from PyQt6.QtCore import * # type: ignore
from PyQt6.QtGui import QPixmap

from credits import CreditsDialog
import pandas as pd

import sys
import os

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        width = int(360*1.25)
        heigth = int(400*1.25)

        self.setFixedSize(width, heigth)
        central = QWidget()
        self.setCentralWidget(central)
        

        main_layout = QVBoxLayout()
        central.setLayout(main_layout)

        container = QWidget()
        form_layout = QGridLayout()
        container.setLayout(form_layout)

        bg_path = self.resource_path("data/interfaz_2.png")
        bg_path = bg_path.replace("\\", "/")
        
        central.setObjectName("central")

        central.setStyleSheet(f"""
        #central {{
            border-image: url("{bg_path}") 0 0 0 0 stretch stretch;
        }}

        QLineEdit {{
            background-color:  rgb(117, 208, 224);
            color: black;              /* text inside input */
            padding: 4px;
            border-radius: 8px;

            selection-background-color: white;
            selection-color: black;
        }}

        QLabel {{
            color: black;
            font-weight: bold;         /* optional, looks nicer */
        }}

        QPushButton {{
            background-color:  rgb(30, 30, 30);
        }}

        QComboBox {{
            background-color:  rgb(235, 188, 94);
            color: black;
        }}

        /* rgb(117, 208, 224) */

        QPushButton {{
            background-color:  rgb(39, 151, 170);
            color: white;
        }}
        """)

        self.weeks = QLineEdit()
        self.days = QLineEdit()
        self.weight = QLineEdit()
        self.lenght = QLineEdit() #type: ignore

        self.male_label = ""
        self.female_label = ""
        self.diagnostic = ""

        self.language = QComboBox()
        self.language.addItem("Español")
        self.language.addItem("English")
        self.language.currentIndexChanged.connect(self.update_language)

        self.age_weeks_label = QLabel()
        self.age_days_label = QLabel()
        self.weight_label = QLabel()
        self.length_label = QLabel()
        self.sex_label = QLabel()

        self.sex = QComboBox()
        self.sex.addItem(self.male_label, userData="male")
        self.sex.addItem(self.female_label, userData="female")

        self.button = QPushButton(self.diagnostic)
        self.button.clicked.connect(self.diagnose)

        self.credits_button = QPushButton()
        self.credits_button.clicked.connect(self.show_credits)

        self.result = QLabel("")  

        form_layout.addWidget(self.language, 0, 2, 1, 2)
        
        self.age_weeks_label.setFixedWidth(90)
        self.credits_button.setFixedWidth(100)
        self.result.setFixedWidth(230)
        self.result.setFixedHeight(70)


        # Add your widgets to form_layout instead of layout
        form_layout.addWidget(self.age_weeks_label, 0, 0)
        form_layout.addWidget(self.weeks, 0, 1)

        form_layout.addWidget(self.age_days_label, 1, 0)
        form_layout.addWidget(self.days, 1, 1)

        form_layout.addWidget(self.weight_label, 2, 0)
        form_layout.addWidget(self.weight, 2, 1)

        form_layout.addWidget(self.length_label, 3, 0)
        form_layout.addWidget(self.lenght, 3, 1)

        form_layout.addWidget(self.sex_label, 4, 0)
        form_layout.addWidget(self.sex, 4, 1)

        form_layout.addWidget(self.button, 5, 0, 1, 2)
        form_layout.addWidget(self.result, 6, 0, 1, 2)

        form_layout.addWidget(self.credits_button, 5, 2, 1, 2)

        self.credits_button.setStyleSheet("""
            background-color: grey;
        """)

        # Center the container
        main_layout.addStretch()
        main_layout.addWidget(container, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addStretch()

        self.update_language()

    def get_table(self):
        if self.sex.currentData() == "male":
            return self.resource_path("data/male_percentile_weight.csv"), self.resource_path("data/male_percentile_length.csv")
        else:
            return self.resource_path("data/female_percentile_weight.csv"), self.resource_path("data/female_percentile_length.csv")

    def diagnose(self):
        w_table, l_table = self.get_table()
        error = False

        try:
            assert w_table is not None and l_table is not None, "Tables not found"
            assert self.weeks.text() != "" and self.days.text() != "" and self.weight.text() != "" and self.lenght.text() != "", "All fields must be filled"
            assert self.weeks.text().isdigit() and self.days.text().isdigit(), "Weeks and days must be integers"
            df_w = pd.read_csv(w_table)
            df_l = pd.read_csv(l_table)

            weight = float(self.weight.text())
            lenght = float(self.lenght.text())
            weight_p_10 = df_w[df_w["weeks"] == int(self.weeks.text())][df_w["days"] == int(self.days.text())]["p10_weight"].values[0] #type: ignore
            weight_p_90 = df_w[df_w["weeks"] == int(self.weeks.text())][df_w["days"] == int(self.days.text())]["p90_weight"].values[0] #type: ignore
            lenght_p_10 = df_l[df_l["weeks"] == int(self.weeks.text())][df_l["days"] == int(self.days.text())]["p10_length"].values[0]
            weight_p_10 = float(weight_p_10)
            weight_p_90 = float(weight_p_90)
            lenght_p_10 = float(lenght_p_10)

            error = False
        except (ValueError, KeyError, IndexError, AssertionError):
            error = True

        if error:
            self.result.setText("Invalid inputs")
        else:
            diagnostics = []
            if weight < weight_p_10: #type: ignore
                diagnostics.append(self.SGA)
            if weight < 2.5:
                diagnostics.append(self.LBW)
            if weight > weight_p_90: #type: ignore
                diagnostics.append(self.LGA)
            if weight > 4.0:
                diagnostics.append("Macrosomia (MAC)")
            if lenght < lenght_p_10: #type: ignore
                diagnostics.append(self.IL)
            if not diagnostics:
                diagnostics.append("Normal")

            self.result.setText("\n".join(diagnostics))

    def update_language(self):
        if self.language.currentText() == "Español":
            self.age_weeks_label.setText("Edad (semanas)")
            self.age_days_label.setText("Edad (días)")
            self.weight_label.setText("Peso (kg)")
            self.length_label.setText("Longitud (cm)")
            self.sex_label.setText("Sexo")

            self.male_label = "Masculino"
            self.female_label = "Femenino"
            self.diagnostic = "Diagnosticar"

            self.SGA = "Pequeño para la Edad Gestacional (PEG)"
            self.LBW = "Bajo Peso al Nacer (BPN)"
            self.LGA = "Grande para la Edad Gestacional (GEG)"
            self.IL = "Longitud Insuficiente (LI)"

            self.credits_button.setText("Créditos/Citas")
            
        else:
            self.age_weeks_label.setText("Age (weeks)")
            self.age_days_label.setText("Age (days)")
            self.weight_label.setText("Weight (kg)")
            self.length_label.setText("Length (cm)")
            self.sex_label.setText("Sex")

            self.male_label = "Male"
            self.female_label = "Female"
            self.diagnostic = "Diagnose"

            self.SGA = "Small Gestational Age (SGA)"
            self.LBW = "Low Birth Weight (LBW)"
            self.MAC = "Large Gestational Age (LGA)"
            self.IL = "Insuficient Length (IL)"

            self.credits_button.setText("Credits/Citations")

        # Update combo box
        current_index = self.sex.currentIndex()
        self.sex.clear()
        self.sex.addItem(self.male_label, userData="male")
        self.sex.addItem(self.female_label, userData="female")
        self.sex.setCurrentIndex(current_index)

        # Update button text
        self.button.setText(self.diagnostic)

    def show_credits(self):
        dialog = CreditsDialog(self.language.currentText())
        dialog.exec()
        
    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path) # type: ignore
        return os.path.join(os.path.abspath("."), relative_path)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    width = int(360*1.25)
    heigth = int(400*1.25)
    w.resize(width, heigth)
    w.show()
    sys.exit(app.exec())
