#!/usr/bin/env python3


# LICENSE !!!!!
## Copyright (C) 2022 MuKonqi (Muhammed Abdurrahman)
## yasfetch is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, in args or
## (at your option) any later version.
## yasfetch is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## You should have received a copy of the GNU General Public License
## along with yasfetch.  If not, see <https://www.gnu.org/licenses/>.

import platform
v_system=platform.system()
if v_system != "Linux":
    exit("Your operating system is not supported.")

import distro
import socket
import getpass
import psutil
import sys
import os

v_distro=distro.name(pretty=True)
v_hostname=socket.gethostname()
v_platform=platform.platform()
v_username=getpass.getuser()
v_dir="/home/"+v_username+"/.config/yasfetch"
v_pkg_manager=""
color=""
lang=""
args=sys.argv[1:]

def main():
    v_uptime=os.popen('uptime -p').read()[:-1]
    v_cpu=str(psutil.cpu_percent(4))
    v_ram=str(psutil.virtual_memory()[2])

    sifir = "\033[0m"
    siyah = "\033[;30m"
    kirmizi = "\033[;31m"
    yesil = "\033[;32m"
    sari = "\033[;33m"
    mavi = "\033[;34m"
    pembe = "\033[;35m"
    turkuaz = "\033[;36m"
    beyaz = "\033[;37m"

    if os.path.isfile(v_dir+"/color/1.txt"):
        color=siyah
    elif os.path.isfile(v_dir+"/color/2.txt"):
        color=kirmizi
    elif os.path.isfile(v_dir+"/color/3.txt"):
        color=yesil
    elif os.path.isfile(v_dir+"/color/4.txt"):
        color=sari
    elif os.path.isfile(v_dir+"/color/5.txt"):
        color=mavi
    elif os.path.isfile(v_dir+"/color/6.txt"):
        color=pembe
    elif os.path.isfile(v_dir+"/color/7.txt"):
        color=turkuaz
    elif os.path.isfile(v_dir+"/color/8.txt"):
        color=beyaz

    if os.path.isfile("/etc/debian_version"):
        v_pkg_manager="DPKG"
    if os.path.isfile("/bin/pacman") or os.path.isfile("/usr/bin/pacman"):
        v_pkg_manager="Pacman"
    if os.path.isfile("/usr/bin/yum"):
        v_pkg_manager="Yum"
    if os.path.isfile("/etc/fedora-release"):
        v_pkg_manager="DNF"
    if os.path.isfile("/etc/solus-release"):
        v_pkg_manager="EOPKG"
    if os.path.isfile("/etc/pisilinux-release"):
        v_pkg_manager="PiSi"
    if os.path.isdir("/etc/xbps.d"):
        v_pkg_manager="XBPS"

    if os.path.isfile(v_dir+"/lang/en.txt"):
        print(f"     Welcome to yasfetch {color}"+v_username+f"{sifir}!")
        print(f"{color}Hostname:           {sifir}"+v_hostname)
        print(f"{color}Distribution:       {sifir}"+v_distro)
        print(f"{color}Kernel:             {sifir}"+v_platform)
        if v_pkg_manager != "":
            print(f"{color}Package manager:    {sifir}"+v_pkg_manager)
        print(f"{color}CPU usage:          {sifir}%"+v_cpu)
        print(f"{color}RAM usage:          {sifir}%"+v_ram)
        print(f"{color}Uptime:             {sifir}"+v_uptime)
    elif os.path.isfile(v_dir+"/lang/tr.txt"):
        print(f"     yasfetch'e hoşgeldiniz {color}"+v_username+f"{sifir}!")
        print(f"{color}Ana bilgisayar adı: {sifir}"+v_hostname)
        print(f"{color}Dağıtım:            {sifir}"+v_distro) 
        print(f"{color}Çekirdek:           {sifir}"+v_platform)
        if v_pkg_manager != "":
            print(f"{color}Paket yönetcisi:    {sifir}"+v_pkg_manager)
        print(f"{color}CPU kullanımı:      {sifir}%"+v_cpu)
        print(f"{color}RAM kullanımı:      {sifir}%"+v_ram)
        print(f"{color}Çalışma süresi:     {sifir}"+v_uptime)
if v_system == "Linux":
    if not os.path.isdir(v_dir) or not os.path.isdir(v_dir+"/color") or not os.path.isdir(v_dir+"/lang"):
        os.system("cd /home/"+v_username+"/.config/ ; mkdir yasfetch ; cd yasfetch ; mkdir color ; mkdir lang")
        input1=input("Can't found language and color setting. First, select a language.\nDil ve renk ayarı bulunamadı. İlk önce bir dil seçin.\n\nOptions / Seçenekler: en / tr\nAnswer / Cevap: ")
        
        if input1 == "en":
            os.system("cd "+v_dir+"/lang/ ; touch en.txt")
            input2=input("English selected.\n\nPlease select a color. This color will be used in the actual output of yasfetch.\nOptions: black / red / green / yellow / blue / pink / turquoise / white\nAnswer: ")
            if input2 == "black":
                os.system("cd "+v_dir+"/color/ ; touch 1.txt")
                print("Successful!\n\n\n")
                main()
            elif input2 == "red":
                os.system("cd "+v_dir+"/color/ ; touch 2.txt")
                print("Successful!\n\n\n")
                main()
            elif input2 == "green":
                os.system("cd "+v_dir+"/color/ ; touch 3.txt")
                print("Successful!\n\n\n")
                main()
            elif input2 == "yellow":
                os.system("cd "+v_dir+"/color/ ; touch 4.txt")
                print("Successful!\n\n\n")
                main()
            elif input2 == "blue":
                os.system("cd "+v_dir+"/color/ ; touch 5.txt")
                print("Successful!\n\n\n")
                main()
            elif input2 == "pink":
                os.system("cd "+v_dir+"/color/ ; touch 6.txt")
                print("Successful!\n\n\n")
                main()
            elif input2 == "turquoise":
                os.system("cd "+v_dir+"/color/ ; touch 7.txt")
                print("Successful!\n\n\n")
                main()
            elif input2 == "white":
                os.system("cd "+v_dir+"/color/ ; touch 8.txt")
                print("Successful!\n\n\n")
                main()

        elif input1 == "tr":
            os.system("cd "+v_dir+"/lang/ ; touch tr.txt")
            input2=input("Türkçe seçildi.\n\nLütfen bir renk seçin. Bu renk, yasfetch'in asıl çıktısında kullanılacaktır.\nSeçenekler: siyah / kırmızı / yeşil / sarı / mavi / pembe / turkuaz / beyaz\nCevap: ")
            if input2 == "siyah":
                os.system("cd "+v_dir+"/color/ ; touch 1.txt")
                print("Başarılı!\n\n\n")
                main()
            elif input2 == "kırmızı":
                os.system("cd "+v_dir+"/color/ ; touch 2.txt")
                print("Başarılı!\n\n\n")
                main()
            elif input2 == "yeşil":
                os.system("cd "+v_dir+"/color/ ; touch 3.txt")
                print("Başarılı!\n\n\n")
                main()
            elif input2 == "sarı":
                os.system("cd "+v_dir+"/color/ ; touch 4.txt")
                print("Başarılı!\n\n\n")
                main()
            elif input2 == "mavi":
                os.system("cd "+v_dir+"/color/ ; touch 5.txt")
                print("Başarılı!\n\n\n")
                main()
            elif input2 == "pembe":
                os.system("cd "+v_dir+"/color/ ; touch 6.txt")
                print("Başarılı!\n\n\n")
                main()
            elif input2 == "turkuaz":
                os.system("cd "+v_dir+"/color/ ; touch 7.txt")
                print("Başarılı!\n\n\n")
                main()
            elif input2 == "beyaz":
                os.system("cd "+v_dir+"/color/ ; touch 8.txt")
                print("Başarılı!\n\n\n")
                main()

    if "help" in args or "yardım" in args or "-h" in args or "-y" in args:
        if os.path.isfile(v_dir+"/lang/en.txt"):
            print("help or -h     Show help (this) screen")
            print("settings       Show settings screen")
        elif os.path.isfile(v_dir+"/lang/tr.txt"):
            print("yardım veya y      Yardım (bu) ekranını göster")
            print("ayarlar            Ayarlar ekranını göster")


    elif "settings" in args or "ayarlar" in args:
        if os.path.isfile(v_dir+"/lang/en.txt"):
            input11=input("Please select an option. Options:\n1 -> Change Language to Turkish (Türkçe)\n2 -> Change Color Preference\nAnswer: ")
            if input11 == "1":
                os.system("cd "+v_dir+"/lang/ ; rm * ; touch tr.txt")
                print("Türkçe dili uygulandı.\n\n\n")
                main()
            if input11 == "2":
                input12=input("\n\nPlease choose a color. This color will be used in the actual output of yasfetch.\nOptions: black / red / green / yellow / blue / pink / turquoise / white\nAnswer: ")
                if input12 == "black":
                    os.system("cd "+v_dir+"/color/ ; touch 1.txt")
                    print("Succesful!\n\n\n")
                    main()
                elif input12 == "red":
                    os.system("cd "+v_dir+"/color/ ; touch 2.txt")
                    print("Succesful!\n\n\n")
                    main()
                elif input12 == "green":
                    os.system("cd "+v_dir+"/color/ ; touch 3.txt")
                    print("Succesful!\n\n\n")
                    main()
                elif input12 == "yellow":
                    os.system("cd "+v_dir+"/color/ ; touch 4.txt")
                    print("Succesful!\n\n\n")
                    main()
                elif input12 == "blue":
                    os.system("cd "+v_dir+"/color/ ; touch 5.txt")
                    print("Succesful!\n\n\n")
                    main()
                elif input12 == "pink":
                    os.system("cd "+v_dir+"/color/ ; touch 6.txt")
                    print("Succesful!\n\n\n")
                    main()
                elif input12 == "turquoise":
                    os.system("cd "+v_dir+"/color/ ; touch 7.txt")
                    print("Succesful!\n\n\n")
                    main()
                elif input12 == "white":
                    os.system("cd "+v_dir+"/color/ ; touch 8.txt")
                    print("Succesful!\n\n\n")
                    main()
        elif os.path.isfile(v_dir+"/lang/tr.txt"):
            input11=input("Lütfen bir seçenek seçin. Seçenekler:\n1 -> Dili İngilizce (English) Yap\n2 -> Renk Tercihini Değiştir\nCevap: ")
            if input11 == "1":
                os.system("cd "+v_dir+"/lang/ ; rm * ; touch en.txt")
                print("English language is applied.\n\n\n")
                main()
            if input11 == "2":
                input12=input("\n\nLütfen bir renk seçin. Bu renk, yasfetch'in asıl çıktısında kullanılacaktır.\nSeçenekler: siyah / kırmızı / yeşil / sarı / mavi / pembe / turkuaz / beyaz\nCevap: ")
                if input12 == "siyah":
                    os.system("cd "+v_dir+"/color/ ; touch 1.txt")
                    print("Başarılı!\n\n\n")
                    main()
                elif input12 == "kırmızı":
                    os.system("cd "+v_dir+"/color/ ; touch 2.txt")
                    print("Başarılı!\n\n\n")
                    main()
                elif input12 == "yeşil":
                    os.system("cd "+v_dir+"/color/ ; touch 3.txt")
                    print("Başarılı!\n\n\n")
                    main()
                elif input12 == "sarı":
                    os.system("cd "+v_dir+"/color/ ; touch 4.txt")
                    print("Başarılı!\n\n\n")
                    main()
                elif input12 == "mavi":
                    os.system("cd "+v_dir+"/color/ ; touch 5.txt")
                    print("Başarılı!\n\n\n")
                    main()
                elif input12 == "pembe":
                    os.system("cd "+v_dir+"/color/ ; touch 6.txt")
                    print("Başarılı!\n\n\n")
                    main()
                elif input12 == "turkuaz":
                    os.system("cd "+v_dir+"/color/ ; touch 7.txt")
                    print("Başarılı!\n\n\n")
                    main()
                elif input12 == "beyaz":
                    os.system("cd "+v_dir+"/color/ ; touch 8.txt")
                    print("Başarılı!\n\n\n")
                    main()
    else:
        main()
