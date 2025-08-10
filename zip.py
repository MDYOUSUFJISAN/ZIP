import zipfile



zip= input("Enter  Zip File Path: ")
zip_file= zip_file.Zip_File(zip)

pw= input("Enter Password list path: ")


file= open( pw,"r")

for Password in file:
	Password.Password.strip()
	try:
			zip.extractall(pwd=bytes(password, 'utf-8'))
			print("password is: "+password)
			break
	except:
		print("wrong password: "+password)



#wordlist = "wordlist.txt"  # এখানে সম্ভাব্য পাসওয়ার্ডগুলো থাকবে, এক লাইনে একটাই

#with zipfile.ZipFile(zip_file) as zf:
#    with open(wordlist, 'r') as file:
#        for line in file:
#            password = line.strip()
#            try:
#                zf.extractall(pwd=bytes(password, 'utf-8'))
#                print(f"[✓] Password found: {password}")
#                break
#            except:
#                print(f"[×] Trying: {password}")