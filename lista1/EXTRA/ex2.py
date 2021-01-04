num = int(input("Por favor, entre com o número de segundos que deseja converter:"))

dias = num // 86400
horas =  (num % 86400) // 3600
minutos = ((num % 86400) % 3600) // 60
segundos = ((num % 86400) % 3600) % 60

print(dias, "dias,", horas, "horas,", minutos,"minutos e", segundos, "segundos." )
