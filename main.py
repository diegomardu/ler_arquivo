entrada = open("entrada.txt","r")
saida = open("saida.txt","w")

for i in entrada:
    if(len(i)>20):
        saida.write(i)

entrada.close(),saida.close()
