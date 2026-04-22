# NutriNeo

NutriNeo is a simple desktop application designed to assist in nutritional evaluation using percentile data. It is intended for users with minimal technical or informatics knowledge, so the interface and execution process are kept as straightforward as possible.

Features:

- Easy-to-use graphical interface
- Nutritional assessment based on percentile data
- Supports male and female datasets for weight and length
- Standalone executable (no programming knowledge required to use)

# How to Use the Application

## Option 1: Run the Executable (.exe)

If you already have the compiled .exe file:

1. Locate the file main.exe
2. Double-click to open it
3. Use the graphical interface to input the required data

No installation or additional setup is required.

## Option 2: Run from Source Code

If you want to run the application from the source code:

1. Install Python

Make sure you have Python 3 installed on your system.

2. Install Dependencies

Open a terminal in the project folder and install the required packages:

```bash
pip install -r requirements.txt
```

3. Run the Application

```bash
python main.py
```

-------

# Rebuilding the Executable (.exe)

If you need to generate the executable file again, use the following command:

```bash
pyinstaller --onefile --windowed \
--add-data "data/female_percentile_length.csv;data" \
--add-data "data/female_percentile_weight.csv;data" \
--add-data "data/male_percentile_length.csv;data" \
--add-data "data/male_percentile_weight.csv;data" \
--add-data "data/interfaz_2;data" \
main.py
```

> [!NOTE]
> This is a useful note that readers should see even when skimming.
> - Make sure you run this command from the root directory of the project.
> - The generated .exe file will appear in the dist/ folder.
> - The --windowed option ensures that no console window appears when running the app.
> - The --add-data flags are required to include the necessary data files inside the executable.

# Target Users

This application is designed for:

- Health professionals
- Students
- General users with little or no programming experience
