import requests

result = requests.get("https://datos.magyp.gob.ar/dataset/10105e94-c560-4b02-b15f-ef3ef764b833/resource/50f0edcc-4dfc-4afb-b78a-b164601d36ae/download/trigo-serie-1927-2024.csv")
with open("trigo-serie-1927-2024.csv", "wb") as file:
    file.write(result.content)
    