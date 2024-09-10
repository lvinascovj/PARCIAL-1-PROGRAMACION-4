from user_interface import show_data

departamento = input("Por favor ingrese el nombre del departamento:")
municipio = input("\nPor favor ingrese el nombre del municipio:")
cultivo = input("\nPor favor ingrese el nombre del cultivo:")
topografia= input("\nPor favor ingrese la topografia del terreno:")
limite= int(input("\nPor favor ingrese la cantidad de  registros que desea mostrar:"))

show_data(departamento.upper(), municipio.upper(), cultivo.capitalize(), topografia.capitalize(), limite)