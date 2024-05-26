import subprocess

arquivos = ["Nave.py", "Player.py","gameTest.py"]

for arquivo in arquivos:
    subprocess.run(['python', arquivo])
    