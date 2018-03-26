def maximo(num1,num2):
	if num1>num2:
		print 'el numero '+str(num1)+' es mayor a '+str(num2)
	else:
		print 'el numero '+str(num2)+' es mayor a '+str(num1)

def maximo3numeros(num1,num2,num3):
	if num1>num2 and num1>num3:
		print 'el numero '+str(num1)+' es mayor a '+str(num2)+' y mayor a '+str(num3)
	elif num2>num1 and num2>num3:
		print 'el numero '+str(num2)+' es mayor a '+str(num1)+' y mayor a '+str(num3)

	else:
		print 'el numero '+str(num3)+' es mayor a '+str(num2)+' y mayor a '+str(num1)

#maximo3numeros(7,9,6)
def lentarreglo(arreglo):
	print "formar 1"+str(len(arreglo))
	count=0
	for data in arreglo:
		
		count=count+1
		print data
	print "Forma 2:"+str(count)

def devulvevocal(palabra):
	palabra=palabra.strip(' ')
	if palabra=='a' or palabra=='e' or palabra=='i' or palabra=='o' or palabra=='u':
		print 'si es una vocal texto de prueba'
	else:
		print 'no es vocal asdadsd'
		print 'no es vocal asdadsd'
		print 'no es vocal asdadsd'
		print 'no es vocal asdadsd'

	
arre={"s","dd",'sssss'}
#lentarreglo(arre)
devulvevocal('e   ')

