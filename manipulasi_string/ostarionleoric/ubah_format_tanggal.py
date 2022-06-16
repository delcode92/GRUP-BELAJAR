inputvar = "1990/02/25"
varpenampung =''
spliterinputvar = inputvar.split("/")
z=len(spliterinputvar)

for i in spliterinputvar:
    z=z-1
    varpenampung = varpenampung + spliterinputvar[z] + "/"
print(varpenampung)

