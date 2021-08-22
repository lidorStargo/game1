import os
import platform
Ipuser= input("enetr your ip")
ossystem= platform.system()
ossystem= ossystem.lower()
print(ossystem)
if ossystem== "windows":
    print("choose your command:\n 1.ipconfig\n 2.ping\n 3.creat dir\n 4.get files and dir\n 5.get cwd\n")

    chose= input("enter your chose")
    while chose != "exit":
        chose= input("you can choose again")
        if chose == "ipconfig":
            print(os.system("Ipconfig"))
        elif chose== "ping":
            print(os.popen("ping 8.8.8.8>>ans.txt"))
            with open ("ans.txt", "r") as file:
                for x in file:
                    print(x)
        elif chose == "creat dir":
            os.mkdir("newdir")
        elif chose == "get files and dir":
            print(os.list.dir())
        elif chose == "get cwd":
            print (os.getcwd())
        else:
            print("unknowleg command")
elif ossystem == "linux":
    print("choose your command: 1.ifconfig\n 2.ping\n 3.creat dir\n 4.get fiels and dir\n 5.get cwd\n")
    chose = input("enter your chose")
    while chose != "exit":
        chose = input("you can choose again")
        if chose == "ifconfig":
            print(os.system("Ifconfig"))
        elif chose == "ping":
            print(os.popen("ping 8.8.8.8>>ans.txt"))
            with open ("ans.txt", "r") as file:
                for x in file:
                    print(x)
        elif chose == "creat dir":
            os.mkdir("newdir")
        elif chose == "get files and dir":
            print(os.list.dir())
        elif chose == "get cwd":
            print(os.getcwd())
        else:
            print("unknowleg command")
else:
    print ("unknowleg system")