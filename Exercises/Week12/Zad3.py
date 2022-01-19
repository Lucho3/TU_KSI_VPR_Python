file1=open("RandomBinFile.bin",mode="rb")


file1.seek(0)
binary_data=file1.read()
text=binary_data.decode("ascii")
print(text[0:4])


