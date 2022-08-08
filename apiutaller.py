#!/usr/bin/env python3



# LICENSE !!!!!
## Copyright (C) 2022 MuKonqi (Muhammed Abdurrahman)
## apiutaller is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## apiutaller is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## You should have received a copy of the GNU General Public License
## along with apiutaller.  If not, see <https://www.gnu.org/licenses/>.

# README !
## Dear developer,
### You can make comment lines if you want skip some steps.
### You must set up variables in apiutaller.py.
### In the README.md you must specify that the user should run the apiutaller with root user.

# BENİOKU !
## Sevgili geliştirici,
### Bazı adımları atlamak istersiziz yorum satırları yapabilirsiniz.
### apiutaller.py'de değişkenleri ayarlamalısınız.
### README.md'de, kullanıcının apiutaller'ı root kullanıcı ile çalıştırması gerektiğini belirtmelisiniz.



# Import necessary modules for apiutaller!
import os
from sys import platform



# VARIABLES !!!!!
## Don't forget to change and control them!
## Warning! You must use "" when you don't use any.
appname="yasfetch" # Don't forget to change this! This is necessary for apiutaller.
appfolder="/usr/bin/" # Don't forget to change this! This is necessary for apiutaller.
appfileold="yasfetch.py" # Don't forget to change this! This is necessary for apiutaller.
appfilenew="yasfetch" # Don't forget to change this! This is necessary for apiutaller.
policyfile=any # Options: policy file and any
appdesktopfile=any # Options: desktop file and any
mainappfolder="/usr/local/bin/" # Options: Your way for your main app folder or any
mainappfoldername="yasfetch" # Options your main app folder for icon, modules etc. or any
licensename="GPLv3" # Don't forget to change this! This is necessary for apiutaller.
appdev="MuKonqi" # Don't forget to change this! This is necessary for apiutaller.
debian_apt_support="true" # Options: true and false
debian_apt_dependencies="python3" # Options: "dependencies" and any
fedora_dnf_support="true" # Options: true and false
fedora_dnf_dependencies="python3" # Options: "dependencies" and any
arch_pacman_support="true" # Options: true and false
arch_pacman_dependencies="python3" # Options: "dependencies" and any
opensuse_yum_support="true" # Options: true and false
opensuse_yum_dependencies="python3" # Options: "dependencies" and any
solus_eopkg_support="true" # Options: true and false
solus_eopkg_dependencies="python3" # Options: "dependencies" and any
void_xbps_support="true" # Options: true and false
void_xbps_dependencies="python3" # Options: "dependencies" and any
pisi_pisi_support="true" # Options: true and false
pisi_pisi_dependencies="python3" # Options: "dependencies" and any
other_gnulinux_support="true" # Options: true and false
python_pip_dependencies=any # Options: "dependencies" and any
python3_pip3_dependencies="psutil" # Options: "dependencies" and any



# Below is the version of apiutaller.
apiutaller="v1.4"



def main_install():
    if python_pip_dependencies != any:
        os.system("pip install "+python_pip_dependencies)
    elif python3_pip3_dependencies != any:
        os.system("pip3 install "+python3_pip3_dependencies)

    os.system("chmod +x *")

    if os.path.isdir(appfolder):
        pass
    else:
        os.system("mkdir "+appfolder)
    os.system("cd app ; chmod +x "+appfileold+" ; cp "+appfileold+" "+appfolder+appfilenew)
    if os.path.isfile(appfolder+appfilenew):
        if policyfile == any and appdesktopfile == any and mainappfolder == any and mainappfoldername == any:
            if lang == "en":
                exit("Successful! You have "+appname+" at the moment. Thank you for choosing us!")
            if lang == "tr":
                exit("Başarılı! Siz artık "+appname+" programına sahipsiniz. Bizi seçtiğiniz için teşekkürler!")        
    else:
        if lang == "en":
            exit("Error! This step is first. Closing apiutaller...")
        if lang == "tr":
            exit("Hata! Bu adım birinci. apitaller kapatılıyor...")        

    if policyfile != any:
        if os.path.isdir("/usr/share/polkit-1/actions"):
            pass
        else:
            os.system("mkdir /usr/share/polkit-1/actions")
        os.system("cd app ; chmod +x "+policyfile+" ; cp "+policyfile+" /usr/share/polkit-1/actions/")
        if os.path.isfile("/usr/share/polkit-1/actions/"+policyfile):
            if appdesktopfile == any and mainappfolder == any and mainappfoldername == any:
                if lang == "en":
                    exit("Successful! You have "+appname+" at the moment. Thank you for choosing us!")
                if lang == "tr":
                    exit("Başarılı! Siz artık "+appname+" programına sahipsiniz. Bizi seçtiğiniz için teşekkürler!")        
        else:
            if lang == "en":
                exit("Error! This step is second. Closing apiutaller...")
            if lang == "tr":
                exit("Hata! Bu adım ikinci. apitaller kapatılıyor...")
    if appdesktopfile != any:
        if os.path.isdir("/usr/share/applications"):
            pass
        else:
            os.system("mkdir /usr/share/applications")
        os.system("cd app ; cp "+appdesktopfile+" /usr/share/applications")
        if os.path.isfile("/usr/share/applications/"+appdesktopfile):
            if mainappfolder == any and mainappfoldername == any:
                if lang == "en":
                    exit("Successful! You have "+appname+" at the moment. Thank you for choosing us!")
                if lang == "tr":
                    exit("Başarılı! Siz artık "+appname+" programına sahipsiniz. Bizi seçtiğiniz için teşekkürler!")        
        else:
            if lang == "en":
                exit("Error! This step is third. Closing apiutaller...")
            if lang == "tr":
                exit("Hata! Bu adım üçüncü. apitaller kapatılıyor...")
    
    if mainappfolder != any and mainappfoldername != any:
        if os.path.isdir(mainappfolder):
            pass
        else:
            if mainappfolder == "/usr/local/bin":
                os.system("mkdir /usr/local ; mkdir /usr/local/bin/")
            else:
                os.system("mkdir "+mainappfolder)
        os.system("mkdir "+mainappfolder+mainappfoldername)
        os.system("cd app ; cp -r * "+mainappfolder+mainappfoldername)
        if policyfile != any:
            os.system("cd "+mainappfolder+mainappfoldername+" ; rm "+policyfile)
        if appdesktopfile != any:
            os.system("cd "+mainappfolder+mainappfoldername+" ; rm "+appdesktopfile)
        os.system("cd "+mainappfolder+mainappfoldername+" ; rm "+appfileold)
        os.system("mkdir "+mainappfolder+mainappfoldername+"/apiutaller")
        os.system("cp apiutaller.py "+mainappfolder+mainappfoldername+"/apiutaller")
        if os.path.isdir(mainappfolder+mainappfoldername):
            if lang == "en":
                exit("Successful! You have "+appname+" at the moment. Thank you for choosing us!")
            if lang == "tr":
                exit("Başarılı! Siz artık "+appname+" programına sahipsiniz. Bizi seçtiğiniz için teşekkürler!")        
        else:
            if lang == "en":
                exit("Error! This step is last. Closing apiutaller...")
            if lang == "tr":
                exit("Hata! Bu adım sonuncu. apitaller kapatılıyor...")            

def control_and_install():
    if os.path.isfile("/etc/debian_version"):
        if debian_apt_dependencies != any and debian_apt_support == "true":
            os.system("apt install -y "+debian_apt_dependencies)
            main_install()
        elif debian_apt_dependencies == any and debian_apt_support == "true":
            main_install()
        elif debian_apt_support == "false":
            if lang == "en":
                exit("I'm sorry, you can't use "+appname+"! Because your distro not supported from "+appname+".\nClosing apiutaller...")
            if lang == "tr":
                exit("Üzgünüm, siz "+appname+" uygulamasını kullanamazsınız! Çünkü sizin dağıtımın "+appname+" tarafından desteklenmiyor.\napiutaller kapatılıyor...")            


    elif os.path.isfile("/etc/fedora-release"):
        if fedora_dnf_dependencies != any and fedora_dnf_support == "true":
            os.system("dnf install -y "+fedora_dnf_dependencies)
            main_install()
        elif fedora_dnf_dependencies == any and fedora_dnf_support == "true":
            main_install()
        elif fedora_dnf_support == "false":
            if lang == "en":
                exit("I'm sorry, you can't use "+appname+"! Because your distro not supported from "+appname+".\nClosing apiutaller...")
            if lang == "tr":
                exit("Üzgünüm, siz "+appname+" uygulamasını kullanamazsınız! Çünkü sizin dağıtımın "+appname+" tarafından desteklenmiyor.\napiutaller kapatılıyor...")            

    elif os.path.isfile("/bin/pacman") or os.path.isfile("/usr/bin/pacman"):
        if arch_pacman_dependencies != any and arch_pacman_support == "true":
            os.system("pacman -S -y "+arch_pacman_dependencies+" --noconfirm")
            main_install()
        elif arch_pacman_dependencies == any and arch_pacman_support == "true":
            main_install()
        elif arch_pacman_support == "false":
            if lang == "en":
                exit("I'm sorry, you can't use "+appname+"! Because your distro not supported from "+appname+".\nClosing apiutaller...")
            if lang == "tr":
                exit("Üzgünüm, siz "+appname+" uygulamasını kullanamazsınız! Çünkü sizin dağıtımın "+appname+" tarafından desteklenmiyor.\napiutaller kapatılıyor...")            

    elif os.path.isfile("/usr/bin/yum"):
        if opensuse_yum_dependencies != any and opensuse_yum_support == "true":
            os.system("yum install -y "+opensuse_yum_dependencies)
            main_install()
        elif opensuse_yum_dependencies == any and opensuse_yum_support == "true":
            main_install()
        elif opensuse_yum_support == "false":
            if lang == "en":
                exit("I'm sorry, you can't use "+appname+"! Because your distro not supported from "+appname+".\nClosing apiutaller...")
            if lang == "tr":
                exit("Üzgünüm, siz "+appname+" uygulamasını kullanamazsınız! Çünkü sizin dağıtımın "+appname+" tarafından desteklenmiyor.\napiutaller kapatılıyor...")            

    elif os.path.isfile("/etc/solus-release"):
        if solus_eopkg_dependencies != any and solus_eopkg_support == "true":
            os.system("eopkg install -y "+solus_eopkg_dependencies)
            main_install()
        elif solus_eopkg_dependencies == any and solus_eopkg_support == "true":
            main_install()
        elif solus_eopkg_support == "false":
            if lang == "en":
                exit("I'm sorry, you can't use "+appname+"! Because your distro not supported from "+appname+".\nClosing apiutaller...")
            if lang == "tr":
                exit("Üzgünüm, siz "+appname+" uygulamasını kullanamazsınız! Çünkü sizin dağıtımın "+appname+" tarafından desteklenmiyor.\napiutaller kapatılıyor...")            

    elif os.path.isfile("/etc/pisilinux-release"):
        if pisi_pisi_dependencies != any and pisi_pisi_support == "true":
            os.system("pisi install -y "+pisi_pisi_dependencies)
            main_install()
        elif pisi_pisi_dependencies == any and pisi_pisi_support == "true":
            main_install()
        elif pisi_pisi_support == "false":
            if lang == "en":
                exit("I'm sorry, you can't use "+appname+"! Because your distro not supported from "+appname+".\nClosing apiutaller...")
            if lang == "tr":
                exit("Üzgünüm, siz "+appname+" uygulamasını kullanamazsınız! Çünkü sizin dağıtımın "+appname+" tarafından desteklenmiyor.\napiutaller kapatılıyor...")            

    elif os.path.isdir("/etc/xbps.d"):
        if void_xbps_dependencies != any and void_xbps_support == "true":
            os.system("xbps-install -y "+void_xbps_dependencies)
            main_install()
        elif void_xbps_dependencies == any and void_xbps_support == "true":
            main_install()
        elif void_xbps_support == "false":
            if lang == "en":
                exit("I'm sorry, you can't use "+appname+"! Because your distro not supported from "+appname+".\nClosing apiutaller...")
            if lang == "tr":
                exit("Üzgünüm, siz "+appname+" uygulamasını kullanamazsınız! Çünkü sizin dağıtımın "+appname+" tarafından desteklenmiyor.\napiutaller kapatılıyor...")            

    elif platform == "linux":
        if other_gnulinux_support == "true":
            main_install()
        else:
            if lang == "en":
                exit("I'm sorry, you can't use "+appname+"! Because your distro not supported from "+appname+".\nClosing apiutaller...")
            if lang == "tr":
                exit("Üzgünüm, siz "+appname+" uygulamasını kullanamazsınız! Çünkü sizin dağıtımın "+appname+" tarafından desteklenmiyor.\napiutaller kapatılıyor...")
    else:
        if lang == "en":
            exit("I'm sorry, you can't use "+appname+"! Because your OS not supported from "+appname+".\nClosing apiutaller...")
        if lang == "tr":
            exit("Üzgünüm, siz "+appname+" uygulamasını kullanamazsınız! Çünkü sizin İS'niz "+appname+" tarafından desteklenmiyor.\napiutaller kapatılıyor...")
    


def main_uninstall():

    os.system("cd "+appfolder+" ; rm "+appfilenew)
    if os.path.isfile(appfolder+appfilenew):
        if lang == "en":
            exit("Error! This step is first. Closing apiutaller...")
        if lang == "tr":
            exit("Hata! Bu adım birinci. apiutaller kapatılıyor...")
    else:
        if policyfile == any and appdesktopfile == any and mainappfolder == any and mainappfoldername == any:
            if lang == "en":
                exit("Successful! You haven't "+appname+" at the moment. We will be happy if you share the uninstalling reason with "+appdev+".")
            if lang == "tr":
                exit("Başarılı! Siz artık "+appname+" uygulamasına sahip değilsiniz. Kaldırma sebebinizi "+appdev+" ile paylaşırsanız biz mutlu olacağız.")

    if policyfile != any:    
        os.system("cd /usr/share/polkit-1/actions ; rm "+policyfile)
        if os.path.isfile("/usr/share/polkit-1/actions/"+policyfile):
            if lang == "en":
                exit("Error! This step is second. Closing apiutaller...")
            if lang == "tr":
                exit("Hata! Bu adım ikinci. apiutaller kapatılıyor...")
        else:
            if appdesktopfile == any and mainappfolder == any and mainappfoldername == any:
                if lang == "en":
                    exit("Successful! You haven't "+appname+" at the moment. We will be happy if you share the uninstalling reason with "+appdev+".")
                if lang == "tr":
                    exit("Başarılı! Siz artık "+appname+" uygulamasına sahip değilsiniz. Kaldırma sebebinizi "+appdev+" ile paylaşırsanız biz mutlu olacağız.")
    
    if appdesktopfile != any:
        os.system("cd /usr/share/applications ; rm "+appdesktopfile)
        if os.path.isfile("/usr/share/applications/"+appdesktopfile):
            if lang == "en":
                exit("Error! This step is third. Closing apiutaller...")
            if lang == "tr":
                exit("Hata! Bu adım üçüncü. apiutaller kapatılıyor...")
        else:
            if mainappfolder == any and mainappfoldername == any:
                if lang == "en":
                    exit("Successful! You haven't "+appname+" at the moment. We will be happy if you share the uninstalling reason with "+appdev+".")
                if lang == "tr":
                    exit("Başarılı! Siz artık "+appname+" uygulamasına sahip değilsiniz. Kaldırma sebebinizi "+appdev+" ile paylaşırsanız biz mutlu olacağız.")

    if mainappfolder != any and mainappfoldername != any:
        os.system("cd "+mainappfolder+" ; rm -rf "+mainappfoldername)
        if os.path.isdir(mainappfolder+mainappfoldername):
            if lang == "en":
                exit("Error! This step is last. Closing apiutaller...")
            if lang == "tr":
                exit("Hata! Bu adım sonuncu. apiutaller kapatılıyor...")
        else:
            if lang == "en":
                exit("Successful! You haven't "+appname+" at the moment. We will be happy if you share the uninstalling reason with "+appdev+".")
            if lang == "tr":
                exit("Başarılı! Siz artık "+appname+" uygulamasına sahip değilsiniz. Kaldırma sebebinizi "+appdev+" ile paylaşırsanız biz mutlu olacağız.")



def info():
    if lang == "en":
        print("Welcome to apiutaller "+apiutaller+"!\napiutaller is under the GPLv3 license.\nDeveloper of apiutaller is MuKonqi (Muhammed Abdurrahman).")
        ioa=input("What do you want to do at the moment?\nOptions: install (for "+appname+"), uninstall (for "+appname+"), exit\nAnswer: ")
    if lang == "tr":
        print("apiutaller "+apiutaller+" programına hoşgeldiniz!\napiutaller GPLv3 lisansı altındadır.\napiutaller programının geliştiricisi MuKonqi (Muhammed Abdurrahman) idir.")
        ioa=input("Şuan ne yapmak istersiniz?\nSeçenekler: kur ("+appname+" için), sil ("+appname+" için), çıkış\nCevap: ")
    if ioa == "install" or ioa == "kur":
        control_and_install()
    if ioa == "uninstall" or ioa == "sil":
        main_uninstall()
    if ioa == "exit" or ioa == "çıkış":
        if lang == "en":
            exit("Closing apiutaller...")
        if lang == "tr":
            exit("apiutaller kapatılıyor...")



def operation():
    if lang == "en":
        oa=input("What do you want to do?\nOptions: install (for "+appname+"), uninstall (for "+appname+"), info (for apiutaller), exit\nAnswer: ")
    elif lang == "tr":
        oa=input("Ne yapmak istersiniz?\nSeçenekler: kur ("+appname+" için), sil ("+appname+" için), hakkında (apiutaller için), çıkış\nCevap: ")
    if oa == "install" or oa == "kur":
        control_and_install()
    if oa == "uninstall" or oa == "sil":
        main_uninstall()
    if oa == "info" or oa == "hakkında":
        info()
    if oa == "exit" or oa == "çıkış":
        if lang == "en":
            exit("Closing apiutaller...")
        if lang == "tr":
            exit("apiutaller kapatılıyor...")



def license():
    if lang == "en":
        license=input("Hello! I try installing or uninstalling "+appname+".\nI'm licensed with GPLv3!\n"+appname+" is under the "+licensename+"!\nDo you agree them?\nOptions: y or n\nAnswer: ")
        if license == "y":
            operation()
        if license == "n":
            exit("I'm sorry, you can't use "+appname+" and apiutaller, because you don't agree licenses!\nClosing apiutaller...")
    if lang == "tr":    
        license=input("Merhabalar! Ben "+appname+" uygulamasını kurmayı ya da silmeyi deneyeceğim.\nBen GPLv3 ile lisanslıyım!\n"+appname+" ise "+licensename+" ile lisanslı!\nBunları kabul ediyor musunuz?\nSeçenekler: e ya da h\nCevap: ")
        if license == "e":
            operation()
        if license == "h":
            exit("Üzgünüm, siz "+appname+" ile apiutaller'i kullanamazsınız, çünkü siz lisansları kabul etmediniz!\napuitaller kapatılıyor...")



lang="" # Don't change this variable!
print("Copyright (C) 2022 MuKonqi (Muhammed Abdurrahman)")
if not os.getuid() == 0:
    exit("\nOnly root can run apiutaller!\nSadece kök apiutaller'i çalıştırabilir.\nClosing... / Kapatılıyor...")
language=input("Choose English or Turkish as a language.\nLütfen İngilizce veya Türkçeyi bir dil olarak seçiniz.\nOptions / Seçenekler: en / tr\nLanguage / Dil: ")
if language == 'en':
    lang="en"
    print("English selected.")
    license()
if language == 'tr':
    lang="tr"
    print("Türkçe seçildi.")
    license()
