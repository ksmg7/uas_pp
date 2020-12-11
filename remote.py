import paramiko

def persegi():
    sisi = int(input("sisi: "))
    return sisi

def persegi_panjang():
    panjang = int(input("panjang: "))
    lebar = int(input("lebar: "))
    return [panjang, lebar]

def lingkaran():
    jari_jari = int(input("jari-jari: "))
    return jari_jari

def segitiga():
    alas = int(input("alas: "))
    tinggi = int(input("tinggi: "))
    return [alas, tinggi]

def connect(h, u, p, pr):
    pr.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pr.connect(hostname=h, username=u, password=p)

def sendData(bangun_datar):
    stdin,stdout,stderr = pr.exec_command("python3 linux_node.py")
    for x in bangun_datar:
        stdin.write(str(x) + "\n")

    output = stdout.readlines()
    error_output = stderr.readlines()

    for x in error_output:
        print(x, end="")

    for x in output:
        print(x, end="")

print("---------- Program menghitung bangun datar ----------")
print("----------       Pemrosesan Paralel        ----------\n")
print("pilih opsi Node di bawah ini : ")
print("[1] Node 1")
print("[2] Node 2")
node = int(input("Silahkan pilih Node : "))

hostname = ["192.168.0.41", "192.168.0.42"]
username = ["hooman", "hooman"]
password = ["hooman", "hooman"]
pr = paramiko.SSHClient()

if(node <= len(hostname)):
    connect(hostname[node - 1], username[node - 1], password[node - 1], pr)
else:
    print("silahkan masukkan pilihan yang benar.")
    exit()

print("\n---------- Program menghitung bangun datar ----------")
print("----------       Pemrosesan Paralel        ----------\n")
print("pilih opsi bangun datar di bawah ini : ")
print("[1] Persegi")
print("[2] Persegi Panjang")
print("[3] Segitiga")
print("[4] Lingkaran\n")

pilihan = int(input("silahkan pilih bangun datar : "))

if pilihan == 1:
    prsg = [pilihan]
    prsg.append(persegi())
    sendData(prsg)

elif pilihan == 2:
    perpan = [pilihan]
    panjang, lebar = persegi_panjang()
    perpan.append(panjang)
    perpan.append(lebar)
    sendData(perpan)

elif pilihan == 3:
    sgtiga = [pilihan]
    alas, tinggi = segitiga()
    sgtiga.append(alas)
    sgtiga.append(tinggi)
    sendData(sgtiga)

elif pilihan == 4:
    lingkar = [pilihan]
    jari = lingkaran()
    lingkar.append(jari)
    sendData(lingkar)

else:
    print("silahkan masukkan pilihan yang benar.\n")

