import subprocess

modules_to_install = ["C:\\Users\\cibul\\Downloads\\noether-1.1-py3-none-any.whl", "C:\\Users\\cibul\\Downloads\\Django-4.2.4-py3-none-any.whl", "C:\\Users\\cibul\\Downloads\\measuring_tools-0.5.0-py3-none-any.whl"]
for module in modules_to_install:
    subprocess.call(['pip', 'install', module])