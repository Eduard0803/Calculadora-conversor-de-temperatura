print('Conversor de Temperatura')

temp=str(input('Digite a unidade de conversão: '))

if(temp == 'celsius' or temp == 'Celsius'):
    tempC = float(input('Digite a temperatura em Celsius: '))
    tempF = round((1.8*tempC+32), 2)
    tempK = round((tempC + 273.15), 2)
    print(f'{tempC} em Kelvin é = {tempK}')
    print(f'{tempC} em Fahrenheit é = {tempF}')
elif(temp == 'fahrenheit' or temp == 'Fahrenheit'):
    tempF = float(input('Digite a temperatura em Fahrenheit: '))
    tempC = 5*(tempF-32)/9
    tempK = (5*(tempF-32)/9)+273.15
    print(f'{tempF} em Celsius é = {tempC}')
    print(f'{tempF} em Kelvin é = {tempK}')
elif(temp == 'kelvin' or temp == 'Kelvin'):
    tempK = float(input('Digite a temperatura em Kelvin: '))
    tempC = round((tempK - 273.15), 2)
    tempF = round(((tempK - 273.15)*1.8+32), 2)
    print(f'{tempK} em Celsius é = {tempC}')
    print(f'{tempK} em Fahrenheit é = {tempF}')
else:
    print('Dados invalidos, Tente novamente')

