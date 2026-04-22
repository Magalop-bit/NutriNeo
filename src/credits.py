import pandas as pd
from PyQt6.QtWidgets import * # type: ignore

class CreditsDialog(QDialog):
    def __init__(self, language="English"):
        super().__init__()
        self.setWindowTitle("Credits")
        self.resize(600, 500)

        layout = QVBoxLayout()

        text = QTextEdit()
        text.setReadOnly(True)

        label = QLabel()
        label.setWordWrap(True)

        if language == "Español":

            text.setPlainText(
                "Herramienta de diagnóstico nutricional neonatal (NutriNeo)\n\n"
                "Desarrollado por:\n"
                "- Marcos Galván López\n"
                "- Guadalupe López Rodriguez\n"
                "Diseño por: Monserraht Ibeth Olaco Quiroz\n\n"
                "Para el diagnostico de los recién nacidos se utilizarón los valores del percentil 10 y 90 de peso y longitud de \"The International Fetal and Newborn Growth Consortium for the 21st Century (INTERGROWTH-21st) [1]\" \n"
                " - Longitud Insuficiente (LI), <10th percentil (Longitud) [1]\n" 
                " - Pequeño para la Edad Gestacional (PEG), <10th percentil (Peso) [1]\n" 
                " - Grande para la Edad Gestacional (GEG), >90th percentil (Peso) [2,3]\n"
                " - Bajo Peso al Nacer (BPN: <2500 g) [4]\n" 
                " - Exceso de peso al nacer, definedo como Macrosomia (MAC: ≥4000 g) [5]\n\n"

                "Referencias:\n\n"
                "1.	Villar J, Cheikh Ismail L, Victora CG, Ohuma EO, Bertino E, Altman DG, et al. International standards for newborn weight, length, and head circumference by gestational age and sex: the Newborn Cross-Sectional Study of the INTERGROWTH-21st Project. Lancet. 2014;384(9946):857-68.\n"
                "2.	de Onis M, Habicht JP. Anthropometric reference data for international use: recommendations from a World Health Organization Expert Committee. Am J Clin Nutr. 1996;64(4):650-8.\n"
                "3.	Schlaudecker EP, Munoz FM, Bardaji A, Boghossian NS, Khalil A, Mousa H, et al. Small for gestational age: Case definition & guidelines for data collection, analysis, and presentation of maternal immunisation safety data. Vaccine. 2017;35(48 Pt A):6518-28.\n"
                "4.	Frank CE, Speechley KN, Macnab JJ, Campbell MK. Infants Born Large for Gestational Age and Developmental Attainment in Early Childhood. International journal of pediatrics. 2018;2018:9181497.\n"
                "5.	WHO. Comprehensive implementation plan on maternal, infant and young child nutrition 2012 [Available from: https://www.who.int/nutrition/topics/wha_65_6/en/].\n"
                "6.	Chatfield J. ACOG issues guidelines on fetal macrosomia. American College of Obstetricians and Gynecologists. Am Fam Physician. 2001;64(1):169-70.\n\n"

                "Solo para fines académicos, clínicos o científicos."
            )
        else:
            text.setPlainText(
                "Neonatal nutritional diagnostic tool (NutriNeo)\n\n"
                "Developed by:\n"
                "- Marcos Galván López\n"
                "- Guadalupe López Rodriguez\n"
                "Disign by: Monserraht Ibeth Olaco Quiroz\n\n" 
                "For the diagnosis of the new borns the 10 and 90, length and weight, percentiles were used, as specified in \"The International Fetal and Newborn Growth Consortium for the 21st Century (INTERGROWTH-21st) [1]\" \n"
                " - Insufficient Length (IL), <10th percentile (Length) [1]\n" 
                " - Small for Gestational Age (SGA), <10th percentile (Weight) [1]\n" 
                " - Large for Gestational Age (LGA), >90th percentile (Weight) [2,3]\n"
                " - Low Birth Weight (LBW: <2500 g) [4]\n" 
                " - Excess birth weight, defined as Macrosomia (MAC: ≥4000 g) [5]\n\n"

                "References:\n\n"
                "1.	Villar J, Cheikh Ismail L, Victora CG, Ohuma EO, Bertino E, Altman DG, et al. International standards for newborn weight, length, and head circumference by gestational age and sex: the Newborn Cross-Sectional Study of the INTERGROWTH-21st Project. Lancet. 2014;384(9946):857-68.\n"
                "2.	de Onis M, Habicht JP. Anthropometric reference data for international use: recommendations from a World Health Organization Expert Committee. Am J Clin Nutr. 1996;64(4):650-8.\n"
                "3.	Schlaudecker EP, Munoz FM, Bardaji A, Boghossian NS, Khalil A, Mousa H, et al. Small for gestational age: Case definition & guidelines for data collection, analysis, and presentation of maternal immunisation safety data. Vaccine. 2017;35(48 Pt A):6518-28.\n"
                "4.	Frank CE, Speechley KN, Macnab JJ, Campbell MK. Infants Born Large for Gestational Age and Developmental Attainment in Early Childhood. International journal of pediatrics. 2018;2018:9181497.\n"
                "5.	WHO. Comprehensive implementation plan on maternal, infant and young child nutrition 2012 [Available from: https://www.who.int/nutrition/topics/wha_65_6/en/].\n"
                "6.	Chatfield J. ACOG issues guidelines on fetal macrosomia. American College of Obstetricians and Gynecologists. Am Fam Physician. 2001;64(1):169-70.\n\n"

                "Just for academic, clinic and cientific purposes."
            )

        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.accept)

        layout.addWidget(text)
        layout.addWidget(close_btn)

        self.setLayout(layout)