import requests
import json
import os
import pathlib

aesurl = "https://benbotfn.tk/api/v1/aes"
os.chdir(pathlib.Path(__file__).parent.absolute())

print("Grabbing AES Keys...")
response = json.loads(requests.get(aesurl).text)
aes = response["mainKey"]

runCommand = f"umodel.exe -path={os.getcwd()} -game=ue4.27 -aes={aes} "

for i in response["dynamicKeys"].values():
    runCommand += f"-aes={i} "

os.system(runCommand)
