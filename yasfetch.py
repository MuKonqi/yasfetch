#!/usr/bin/env python3

# Copyright (C) 2024 MuKonqi (Muhammed S.)

# yasfetch is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# yasfetch is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with yasfetch.  If not, see <https://www.gnu.org/licenses/>.

import os
import sys
import getpass
import threading
import subprocess
import datetime
import socket
import platform
import distro
import psutil
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import *


if os.path.isfile("/etc/debian_version"):
    pkg = "DEB"
elif os.path.isfile("/etc/fedora-release"):
    pkg = "RPM"
elif os.path.isfile("/bin/zypper") or os.path.isfile("/usr/bin/zypper"):
    pkg = "RPM"
elif os.path.isfile("/etc/arch-release"):
    pkg = "Pacman"
else:
    pkg = None

username = getpass.getuser()

align_center = Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter


class MainWidget(QScrollArea):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.setWidgetResizable(True)
        self.setAlignment(align_center)
        self.setWidget(QWidget(parent = self))
        self.widget().setLayout(QGridLayout(self.widget()))
        
        self.temps_worked = False
        self.temps_labels = {}
        self.temps_number = 0
        self.fans_worked = False
        self.fans_labels = {}
        self.fans_number = 0
        self.batt_worked = False
        self.batt_labels = {}
        
        self.welcome_label = QLabel(parent = self.widget(), alignment = align_center, 
                                    text = f"Hello {username}!")
        self.weather_label = QLabel(parent = self.widget(), alignment = align_center, 
                                    text = f"Weather forecast via wttr.in: Getting")
        self.system_label = QLabel(parent = self.widget(), alignment = align_center, 
                                   text = 'System')
        self.hostname_label = QLabel(parent = self.widget(), alignment = align_center, 
                                     text = f"Hostname: {socket.gethostname()}")
        self.distro_label = QLabel(parent = self.widget(), alignment = align_center, 
                                   text = f"Distrubiton: {distro.name(pretty = True)}")
        self.kernel_label = QLabel(parent = self.widget(), alignment = align_center, 
                                   text = f"Kernel: {platform.platform()}")
        self.packages_label = QLabel(parent = self.widget(), alignment = align_center, 
                                     text = f"Number of packages: ")
        self.uptime_label = QLabel(parent = self.widget(), alignment = align_center, 
                                   text = f"Uptime: "
                                   + str(datetime.timedelta(seconds = float(os.popen('cat /proc/uptime').read().split()[0]))))
        self.boot_time_label = QLabel(parent = self.widget(), alignment = align_center, 
                                      text = f"Boot time: "
                                      + datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%d.%m.%Y %H:%M:%S'))
        self.usages_label = QLabel(parent = self.widget(), alignment = align_center, 
                                   text = 'Usages')
        self.cpu_label = QLabel(parent = self.widget(), alignment = align_center, 
                                text = f"CPU: Getting")
        self.disk_label = QLabel(parent = self.widget(), alignment = align_center, 
                                 text = f"Disk: %{str(psutil.disk_usage('/')[3])}")
        self.ram_label = QLabel(parent = self.widget(), alignment = align_center, 
                                text = f"RAM: %{str(psutil.virtual_memory().percent)}")
        self.swap_label = QLabel(parent = self.widget(), alignment = align_center, 
                                 text = f"Swap: %{str(psutil.swap_memory().percent)}")
        
        self.welcome_label.setStyleSheet("QLabel{font-size: 14pt;}")
        self.system_label.setStyleSheet("QLabel{font-size: 14pt; margin-top: 14px;}")
        self.usages_label.setStyleSheet("QLabel{font-size: 14pt; margin-top: 14px;}")
        
        self.widget().layout().addWidget(self.welcome_label, 0, 0, 1, 4)
        self.widget().layout().addWidget(self.weather_label, 1, 0, 1, 4)
        self.widget().layout().addWidget(self.system_label, 2, 0, 1, 4)
        self.widget().layout().addWidget(self.hostname_label, 3, 0, 1, 4)
        self.widget().layout().addWidget(self.distro_label, 4, 0, 1, 4)
        self.widget().layout().addWidget(self.kernel_label, 5, 0, 1, 4)
        self.widget().layout().addWidget(self.packages_label, 6, 0, 1, 4)
        self.widget().layout().addWidget(self.uptime_label, 7, 0, 1, 4)
        self.widget().layout().addWidget(self.boot_time_label, 8, 0, 1, 4)
        self.widget().layout().addWidget(self.usages_label, 9, 0, 1, 4)
        self.widget().layout().addWidget(self.cpu_label, 10, 0)
        self.widget().layout().addWidget(self.disk_label, 10, 1)
        self.widget().layout().addWidget(self.ram_label, 10, 2)
        self.widget().layout().addWidget(self.swap_label, 10, 3)
        
        self.weather_thread = threading.Thread(target = self.get_weather, daemon = True)
        self.weather_thread.start()
        
        self.packages_thread = threading.Thread(target = self.get_packages, daemon = True)
        self.packages_thread.start()
        
        self.cpu_thread = threading.Thread(target = self.get_cpu, daemon = True)
        self.cpu_thread.start()
        
        if hasattr (psutil, "sensors_temperatures") and psutil.sensors_temperatures():
            self.temps_worked = True
            self.temps_grid = 11
            self.get_temps = psutil.sensors_temperatures()
            self.temps_labels[self.temps_number] = QLabel(parent = self.widget(), alignment = align_center, 
                                                          text = 'Temparatures')
            self.temps_labels[self.temps_number].setStyleSheet("QLabel{font-size: 14pt; margin-top: 14px;}")
            self.widget().layout().addWidget(self.temps_labels[self.temps_number], self.temps_grid, 0, 1, 4)
            for self.temps_hardware, self.temps_hardwares in self.get_temps.items():
                self.temps_grid += 1
                self.temps_number += 1
                self.temps_labels[self.temps_number] = QLabel(parent = self.widget(), alignment = align_center, 
                                  text = f"Hardware: {self.temps_hardware}")
                if self.temps_number == 1:
                    self.temps_labels[self.temps_number].setStyleSheet("QLabel{font-size: 12pt;}")
                else:
                    self.temps_labels[self.temps_number].setStyleSheet("QLabel{font-size: 12pt; margin-top: 12px;}")
                self.widget().layout().addWidget(self.temps_labels[self.temps_number], self.temps_grid, 0, 1, 4)
                for self.temps in self.temps_hardwares:
                    self.temps_grid  += 1
                    self.temps_number += 1
                    self.temps_labels[self.temps_number] = QLabel(parent = self.widget(), alignment = align_center, 
                                                                  text = f"{self.temps.label or self.temps_hardware}: Current = {self.temps.current} °C, " 
                                                                  + f"high = {self.temps.high} °C, critical = {self.temps.critical} °C")
                    self.widget().layout().addWidget(self.temps_labels[self.temps_number], self.temps_grid, 0, 1, 4)
        
        if hasattr (psutil, "sensors_fans") and psutil.sensors_fans():
            self.fans_worked = True
            if self.temps_worked == True:
                self.fans_grid = self.temps_grid + 1
            else:
                self.fans_grid = 11
            self.get_fans = psutil.sensors_fans()
            self.fans_labels[self.fans_number] = QLabel(parent = self.widget(), alignment = align_center, 
                                                        text = 'Fans')
            self.fans_labels[self.fans_number].setStyleSheet("QLabel{font-size: 14pt; margin-top: 14px;}")
            self.widget().layout().addWidget(self.fans_labels[self.fans_number], self.fans_grid, 0, 1, 4)
            for self.fans_hardware, self.fans_hardwares in self.get_fans.items():
                self.fans_grid += 1
                self.fans_number += 1
                self.fans_labels[self.fans_number] = QLabel(parent = self.widget(), alignment = align_center, 
                                                            text = f"hardware: {self.fans_hardware}")
                if self.fans_number == 1:
                    self.fans_labels[self.fans_number].setStyleSheet("QLabel{font-size: 12pt;}")
                else:
                    self.fans_labels[self.fans_number].setStyleSheet("QLabel{font-size: 12pt; margin-top: 12px;}")
                self.widget().layout().addWidget(self.fans_labels[self.fans_number], self.fans_grid, 0, 1, 4)
                for self.fans in self.fans_hardwares:
                    self.fans_grid += 1
                    self.fans_number += 1
                    self.fans_labels[self.fans_number] = QLabel(parent = self.widget(), alignment = align_center, 
                                                                text = f"{self.fans.label or self.fans_hardware}: {self.fans.current} RPM")
                    self.widget().layout().addWidget(self.fans_labels[self.fans_number], self.fans_grid, 0, 1, 4)
        
        if hasattr (psutil, "sensors_battery") and psutil.sensors_battery():
            self.batt_worked = True
            if self.fans_worked == True:
                self.batt_grid = self.fans_grid + 1
            elif self.temps_worked == True:
                self.batt_grid = self.temps_grid + 1
            else:
                self.batt_grid = 10
            self.get_batt = psutil.sensors_battery()
            self.batt_labels[1] = QLabel(parent = self.widget(), alignment = align_center, 
                                                        text = 'Battery')
            self.batt_labels[1].setStyleSheet("QLabel{font-size: 14pt; margin-top: 14px;}")
            self.batt_labels[2] = QLabel(parent = self.widget(), alignment = align_center, 
                                                            text = f"Charge: {str(round(self.get_batt.percent, 2))}")
            if self.get_batt.power_plugged:
                self.batt_labels[3] = QLabel(parent = self.widget(), alignment = align_center,
                                             text = f"Remaining: {str(datetime.timedelta(seconds = self.get_batt.secsleft))}")
                self.batt_labels[4] = QLabel(parent = self.widget(), alignment = align_center,
                                             text = f"Status: "
                                             + str('Charging' if self.get_batt.percent < 100 else 'Charged'))
                self.batt_labels[5] = QLabel(parent = self.widget(), alignment = align_center,
                                             text = 'Plugged-in: Yes')
            else:
                self.batt_labels[3] = QLabel(parent = self.widget(), alignment = align_center,
                                             text = f"Remaining: {str(datetime.timedelta(seconds = self.get_batt.secsleft))}")
                self.batt_labels[4] = QLabel(parent = self.widget(), alignment = align_center,
                                             text = f"Status: Discharging")
                self.batt_labels[5] = QLabel(parent = self.widget(), alignment = align_center,
                                             text = 'Plugged-in: No')
            self.widget().layout().addWidget(self.batt_labels[1], self.batt_grid, 0, 1, 4)
            self.widget().layout().addWidget(self.batt_labels[2], self.batt_grid + 1, 0, 1, 4)
            self.widget().layout().addWidget(self.batt_labels[3], self.batt_grid + 2, 0, 1, 4)
            self.widget().layout().addWidget(self.batt_labels[4], self.batt_grid + 3, 0, 1, 4)
            self.widget().layout().addWidget(self.batt_labels[5], self.batt_grid + 4, 0, 1, 4)
        
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.go_refresh)
        self.timer.start()        
        
    def get_weather(self):
        self.weather_label.setText(f"Weather forecast via wttr.in: "
                                   + subprocess.Popen(f'curl wttr.in/?format="%l:+%C+%t+%w+%h+%M"', 
                                                      shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
                                   .communicate()[0])

    def get_packages(self): 
        if pkg != None:
            if os.path.isfile("/etc/debian_version"):
                self.traditional_packages_cmd = 'apt list --installed| wc -l'
            elif os.path.isfile("/etc/fedora-release"):
                self.traditional_packages_cmd = 'dnf5 list --installed | wc -l'
            elif os.path.isfile("/bin/zypper") or os.path.isfile("/usr/bin/zypper"):
                self.traditional_packages_cmd = 'rpm -qa | wc -l'
            elif os.path.isfile("/etc/arch-release"):
                self.traditional_packages_cmd = 'pacman -Q | wc -l'
            self.traditional_packages_num = (subprocess.Popen(self.traditional_packages_cmd,
                                                            shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
                                            .communicate()[0])
            self.flatpak_packages_num = (subprocess.Popen("flatpak list | wc -l",
                                                            shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
                                        .communicate()[0])
            self.packages_label.setText(f"Number of packages: {self.traditional_packages_num} ({pkg}), {self.flatpak_packages_num} (Flatpak)".replace("\n", ""))
        
        else:
            self.packages_label.hide()
        
    def get_cpu(self):
        while True:
            self.cpu_label.setText(f"CPU: %{str(psutil.cpu_percent(4))}")
        
    def refresh(self):
        self.uptime_label.setText(f"Uptime: "
                                + str(datetime.timedelta(seconds = float(os.popen('cat /proc/uptime').read().split()[0]))))
        self.disk_label.setText(f"Disk: %{str(psutil.disk_usage('/')[3])}")
        self.ram_label.setText(f"RAM: %{str(psutil.virtual_memory().percent)}")
        self.swap_label.setText(f"Swap: %{str(psutil.swap_memory().percent)}")
        
        if hasattr (psutil, "sensors_temperatures") and psutil.sensors_temperatures():
            self.get_temps = psutil.sensors_temperatures()
            for self.temps_hardware, self.temps_hardwares in self.get_temps.items():
                self.temps_labels[self.temps_number].setText(f"Hardware: {self.temps_hardware}")
                for self.temps in self.temps_hardwares:
                    self.temps_labels[self.temps_number].setText(f"{self.temps.label or self.temps_hardware}: current = {self.temps.current} °C " 
                                                                 + f"high = {self.temps.high} °C, critical = {self.temps.critical} °C")
        
        if hasattr (psutil, "sensors_fans") and psutil.sensors_fans():
            self.get_fans = psutil.sensors_fans()
            for self.fans_hardware, self.fans_hardwares in self.get_fans.items():
                self.fans_labels[self.fans_number].setText(f"Hardware: {self.fans_hardware}")
                for self.fans in self.fans_hardwares:
                    self.fans_labels[self.fans_number].setText(f"{self.fans.label or self.fans_hardware}: {self.fans.current} RPM")
        
        if hasattr (psutil, "sensors_battery") and psutil.sensors_battery():
            self.get_batt = psutil.sensors_battery()
            self.batt_labels[2].setText(f"Charge: {str(round(self.get_batt.percent, 2))}")
            if self.get_batt.power_plugged:
                self.batt_labels[3].setText(f"Remaining: {str(datetime.timedelta(seconds = self.get_batt.secsleft))}")
                self.batt_labels[4].setText(f"Status: "
                                            + str('Charging') if self.get_batt.percent < 100 else 'Charged')
                self.batt_labels[5].setText('Plugged-in: Yes')
            else:
                self.batt_labels[3].setText(f"Remaining: {str(datetime.timedelta(seconds = self.get_batt.secsleft))}")
                self.batt_labels[4].setText(f"Status: Discharging")
                self.batt_labels[5].setText('Plugged-in: No')

    def go_refresh(self):
        self.refresh_thread = threading.Thread(target = self.refresh, daemon = True)
        self.refresh_thread.start()
        
        
if __name__ == "__main__":
    application = QApplication(sys.argv)

    window = QMainWindow()
    window.setGeometry(0, 0, 960, 540)
    window.setWindowTitle("Yasfetch")
    window.setCentralWidget(MainWidget())
    window.show()

    application.exec()