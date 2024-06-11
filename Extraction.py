import glob
import os
import shutil

def extraction():
    for spt_file in glob.glob("spt_files/*.spt"):
        print(spt_file)
        txt_file = spt_file.replace(".spt", ".txt")
        os.system("wine tool/gsspt.exe "+spt_file+" "+txt_file)
        
        with open(txt_file, "r", encoding="utf-8") as fread:
            buffer = fread.read()

        with open("scripts_repaired/" + txt_file[10:], "w", encoding="utf-8") as fwrite:
            fwrite.write(buffer)

        os.remove(txt_file)

    menu()

def insert():
    file_name = []
    for txt_file in glob.glob("scripts_repaired/*.txt"):
        shutil.copy(txt_file, "./patch")
    for spt_file in glob.glob("spt_files/*.spt"):
        shutil.copy(spt_file, "./patch")
    
    for x in glob.glob("patch/*.*"):
        if x.endswith(".txt"):
            file_name.append(x)
    
    for x in file_name:
        spt_file = x.replace(".txt", ".spt")
        os.system("wine tool/gsspt.exe "+x+" "+spt_file)
        os.remove(x)

def menu():
    print("1 Extract text in Text_parched")
    print("2 Insert text")
    if not os.path.exists('patch'):
        os.makedirs('patch')
    if not os.path.exists('scripts_repaired'):
        os.makedirs('scripts_repaired')
    if not os.path.exists('spt_files'):
        os.makedirs('spt_files')

    option = int(input())
    if option == 1:
        extraction()
    if option == 2:
        insert()

menu()
