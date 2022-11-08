# Krátký script na kontrolu instalovaného modulu:
try:
    import jupyter # <- zde si můžeš zadat jakýkoliv název modulu
    print("Jupyter je instalován.")
except ModuleNotFoundError:
    print("Jupyter se nepovedlo nainstalovat.")
    
try:
    import pandas
    print("Pandas je instalován.")
except ModuleNotFoundError:
    print("Pandas se nepovedlo nainstalovat.")
    
try:
    import matplotlib
    print("Matplotlib je instalován.")
except ModuleNotFoundError:
    print("Matplotlib se nepovedlo nainstalovat.")
    
try:
    import requests
    print("Requests je instalován.")
except ModuleNotFoundError:
    print("Requests se nepovedlo nainstalovat.")
    
try:
    import seaborn
    print("Seaborn je instalován.")
except ModuleNotFoundError:
    print("Seaborn se nepovedlo nainstalovat.")