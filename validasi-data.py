import os
os.system('cls')
status = ''

header = """
    VALIDASI DATA
    """
print(header)
def username():
    print()
    inputan = input("Masukkan username : ")
    cek1 = len(inputan)
    cek2 = ' ' in inputan
    cek3 = inputan.capitalize()

    if cek1 > 9 and cek2 == False and cek3 == inputan:
        status = "Berhasil"
        return inputan, status

    else:
        status = "gagal"
        inputan = "username tidak valid"
        return inputan, status

def email():
    inputan = input("Masukkan email : ")
    cek1 = len(inputan)
    cek2 = ' ' in inputan
    cek3 = '@' and '.' in inputan
    if cek1 > 7 and cek2 == False and cek3 == True:
        status = "Berhasil"
        return inputan, status
    else:
        status = "Gagal"
        inputan = "Email tidak valid"
        return inputan, status

def phone():
    inputan = str(input("Masukkan Nomor Telpon : "))
    cek1 = len(inputan)
    if cek1 >= 12:
        status = "Berhasil"
        return inputan, status
    else:
        status = "Gagal"
        inputan = "Nomor tidak vaid"
        return inputan, status

def main():
    while True:
        user1, user2 = username()
        print("Username =", user1)
        print("Status   =", user2)
        if user2 == "Berhasil":
            break
        print()
    print()
    while True:
        user3, user4 = email()
        print("Email  =", user3)
        print("Status =", user4)
        if user4 == "Berhasil":
            break
        print()
    print()
    while True:
        user5, user6 = phone()
        print("Nomor Telp =", user5)
        print("Status     =", user6)
        if user6 == "Berhasil":
            break
        print()
    print()

main()
