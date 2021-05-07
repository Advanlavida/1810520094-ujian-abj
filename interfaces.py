while True:
    konfirmasi = input("Input Data Trunk Interface Baru ? (yes/no) : ")
    if konfirmasi == "no" or konfirmasi == "No":
        file=open("db-interfaces.txt", "r")
        for item in file:
            item = item.strip()
            print(item)
        file.close()
        break

    if konfirmasi == "yes" or konfirmasi == "Yes":
        print("***********************************")
        file=open("db-interfaces.txt", "a")
        newhostname = input("Masukkan hostname switch : ")
        newinterface = input("Masukkan nama interface : ")
        print("-----------------------------------")
    file.write("Hostname Switch : " + newhostname + 
    ", Name : " + newinterface + "\n")
file.close()