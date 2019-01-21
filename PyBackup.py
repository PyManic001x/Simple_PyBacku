#!/usr/bin/python3
import os
import sys
import shutil


class Backuping:
    def __init__(self, config_files, Dir_list, file_dir, restore_file):
        self.configs = config_files
        self.Directorys = Dir_list
        self.selected = file_dir
        self.restore = restore_file+".backup"

    def backing_up(self):
        print("[START]-Configs backuping...")
        print("-"*45)
        for i in range(0, len(self.configs)):
            try:
                shutil.copy(str(self.configs[i]), str(self.configs[i])+".backup")
                print("Finished backing up "+str(self.configs[i])+".backup")
                print("-"*45)
            except:
                print("Failed to backup: "+str(self.configs[i]))
                pass
        print("[FINISHED]-Configs backuping...")
        print("="*60)

    def copy_directorys(self):
        print("[START]-Directory backuping\nTHIS MIGHT TAKE A WHILE")
        print("-"*45)
        for i in range(0, len(self.Directorys)):
            try:
                os.system("cp -r "+str(self.Directorys[i])+" "+str(self.Directorys[i])+".backup")
                print("Finished backing up", str(self.Directorys[i])+"\nBackup location: ",str(self.Directorys[i])+".backup")
                print("-"*45)
            except:
                print("Failed backing up: "+str(self.Directorys[i]))
                pass
        print("[FINISHED]-Directory backuping")

    def Backup_the_entered_path(self):
        print("-"*45)
        try:
            os.system("cp -r "+str(self.selected)+" "+str(self.selected)+".backup")
            print("[FINISHED] -file backuping: ",str(self.selected)+".backup")
        except:
            print("[FAILED] to backup", str(self.selected))


    def Restore_selected(self):
        try:
            print(str(self.restore)+" to "+str(self.restore[:-7]))
            os.system("cp -r "+str(self.restore)+" "+str(self.restore[:-7]))
            print("[FINISHED] process successfully.")
        except:
                print("[Failed] to restore")




parrot_source_list = '/etc/apt/sources.list.d/parrot.list'
ssh_config_file = '/etc/ssh/sshd_config'
apache_conf = '/etc/apache2/apache2.conf'
apache_ports_conf = '/etc/apache2/ports.conf'

config_files = list()
config_files.append(parrot_source_list) #0
config_files.append(ssh_config_file) #1
config_files.append(apache_conf) #2
config_files.append(apache_ports_conf) #3

#backup dirs
Dir_list = list()
Dir_list.append("/etc") #0
Dir_list.append("/var") #1
Dir_list.append("/home") #2
Dir_list.append("/boot")
Dir_list.append("/bin")


print(
    "[PYMANIC BACKUP]------------------\n"
    "The [default] backup files are...\n",
    "parrot_apt_source_list\n",
    "sshd_config_file\n",
    "apache_conf\n",
    "apache_ports_conf\n",
    "The [default] directorys\n",
    "/etc\n",
    "/var\n",
    "/home\n",
    "/boot\n",
    "/bin\n",
    "-"*35,
        )

print("1. Want to backup defaults?".upper())
print("2. Want to backup your own selected [files/Dirs]? ".upper())
print("3. Restore selected")

selection = input("[SELECT]>>>>").strip()



if selection == '1':
    Backup = Backuping(config_files, Dir_list, "0", "0")
    Backup.backing_up()
    Backup.copy_directorys()


elif selection == '2':
    print(
        "-"*40,
        "\nEnter the path to backup file or directory",
        "\nFor quitting INPUT MODE enter 'Q'",
        "\nThe backup file will be stored in same directory as file/dir itself!"
    )
    while True:
        file_dir = input("[WHAT TO BACKUP]>>>").strip()
        if file_dir != 'Q':
            CP_SELECTED = Backuping(config_files, Dir_list, file_dir, "rand")
            CP_SELECTED.Backup_the_entered_path()
        else:
            print("Quitting input mode-----")
            sys.exit()


elif selection == '3':
    print("Enter what directory or file to restore.\nEnter 'Q' to quit...")
    while True:
        restore_file = input("[FILE PATH TO RESTORE]>>> ")
        if restore_file != 'Q':
            Restore_sec = Backuping(config_files, Dir_list, 0, restore_file)
            Restore_sec.Restore_selected()
        else:
            print("Quitting...")
            sys.exit()

