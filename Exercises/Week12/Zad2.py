file1=open("d:\Университет\впр\упр\упр седмица 12\RandomBinFile.bin",mode="wb+")


text="This is good!"
encoded=text.encode("ascii")
file1.write(encoded)
file1.seek(0)
binary_data=file1.read()
text=binary_data.decode("ascii")
print(text)



