num = int(input("Por favor, entre com o número de segundos que deseja converter: "))

hora = num // 3600
minutos = (num % 3600) // 60
segundos = (num % 3600) % 60

print(hora, " Horas ", minutos, "minutos ", segundos, "segundos")
