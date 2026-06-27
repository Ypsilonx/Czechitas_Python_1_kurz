# Python – cvičební zápisník (Czechitas)

Osobní cvičební zápisník ke kurzům Pythonu od [Czechitas](https://www.czechitas.cz/)
vytvořeným na platformě **[Kódím.cz](https://kodim.cz/czechitas)**.

Obsah tohoto repozitáře jsou **vlastní poznámky, cvičení a řešení úkolů** — není to
náhrada za oficiální kurzy, ale doplněk k nim.

---

## Zdrojové kurzy

Lekce v tomto repozitáři pokrývají látku z těchto kurzů (doporučené pořadí studia):

| Kurz | Odkaz | Lekce v tomto repozitáři |
|---|---|---|
| Úvod do programování: Python | [kodim.cz/czechitas/uvod-do-progr-1](https://kodim.cz/czechitas/uvod-do-progr-1) | 01 – 03 |
| Úvod do programování 2 | [kodim.cz/czechitas/uvod-do-progr-2](https://kodim.cz/czechitas/uvod-do-progr-2) | 04 – 06 |
| Objektově orientované programování v Pythonu | [kodim.cz/czechitas/python-oop](https://kodim.cz/czechitas/python-oop) | 04 – 05 |
| Python pro data 1 | [kodim.cz/czechitas/python-data-1](https://kodim.cz/czechitas/python-data-1) | 07 – 12 |

---

## Struktura projektu

```
lekce_01_slovniky/                  # slovníky, základní datové struktury
lekce_02_cykly_seznam/              # seznamy, cykly for, range
lekce_03_funkce/                    # funkce, parametry, návratové hodnoty
lekce_04_tridy/                     # třídy, objekty, atributy
lekce_05_dedicnost_comprehensions/  # dědičnost, list/dict comprehensions
lekce_06_soubory/                   # práce se soubory (open, read, write)
lekce_07_jupyter_datetime/          # Jupyter notebooky, práce s datem a časem
lekce_08_pandas_zaklady/            # pandas – DataFrame, načítání dat
lekce_09_pandas_indexace/           # pandas – indexace, základní dotazy
lekce_10_agregace_spojovani/        # pandas – agregace, groupby, join
lekce_11_regularni_vyrazy/          # regulární výrazy v Pythonu a pandas
lekce_12_vizualizace/               # matplotlib – grafy a vizualizace
data/                               # sdílené datové soubory (CSV, JSON, TXT)
testovani/                          # drobné experimenty a zkoušení
```

Každá složka lekce obsahuje:
- `cviceni_*.py` nebo notebook `.ipynb` – cvičení z hodiny
- `ukol.py` nebo `ukol.ipynb` – řešení domácího úkolu

---

## Spuštění prostředí

Projekt používá [UV](https://docs.astral.sh/uv/) pro správu závislostí (Python 3.14).

```powershell
# Instalace závislostí a vytvoření .venv
uv sync

# Spuštění Jupyter Lab
uv run jupyter lab
```

Nebo klasicky přes pip:

```powershell
pip install -r requirements.txt
jupyter lab
```