def File_Reader(file_name):
    try:
        f = open(file_name, "r")
        print(f.read())
        f.close()
    except:
        print("Exception!")


File_Reader("D:\Университет\впр\упр\упр седмица 9\Textche.txt")