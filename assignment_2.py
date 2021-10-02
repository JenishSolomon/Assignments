a = input("Input the Filename: ")

b = a.split(".")

if b[-1] == "py" :
    print ("Python")

elif b[-1] == "pdf" :
    print ("Portable Document File")

elif b[-1] == "txt" :
    print ("Text")



