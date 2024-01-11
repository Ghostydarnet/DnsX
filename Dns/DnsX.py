import requests
import pyfiglet
import datetime
import time



print(pyfiglet.figlet_format("DNSX"))
days = datetime.datetime.now()
print(days)


print("""
      [creado por [Ghostyh4]]
      [version -- V1]
      [plataforma --- github]
      [name script [DnsX]]""")



date = input("\n coloque el url que desea  para obtener informacion :")
inyector = requests.get(date)




print("\n |caragando espere....|")

time.sleep(5)
print(f'estado de codigo: {inyector.status_code}')
print(f'datos : {inyector.links}')
print(f'encabezado: {inyector.headers}')
print(f'info : {inyector.history}')
print(f'metadatos: {inyector.text}')
