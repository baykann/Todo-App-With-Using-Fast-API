string = input("Please give an input :")    #Kullanıcıdan girdi alıyoruz.
length = len(string)  

reverse = ("")

for i in range(length-1,-1,-1) :  

    reverse += string[i] #Girdimizi length değişkeni kadar for döngüsüyle sondan başa doğru reverse değişkenine yazdırıyoruz.

print(reverse)