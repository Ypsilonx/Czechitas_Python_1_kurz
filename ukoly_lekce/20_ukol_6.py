# Krátký script na kontrolu instalovaného modulu:
try:
    import jupyter # <- zde si můžeš zadat jakýkoliv název modulu
    print("module is installed")
except ModuleNotFoundError:
    print("module is not installed")