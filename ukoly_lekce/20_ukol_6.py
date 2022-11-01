try:
    import jupyter
    print("module is installed")
except ModuleNotFoundError:
    print("module is not installed")