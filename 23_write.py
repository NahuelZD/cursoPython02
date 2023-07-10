with open('./text.txt', 'r+') as file: # 'r+' permiso para lectura y escritura. 'w+' sobrescribe el archivo
    for line in file:
        print(line)
    file.write('\nNuevo en el archivo\n')