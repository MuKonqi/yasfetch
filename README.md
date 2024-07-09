# yasfetch
## Yet Another Simple Fetch
Get system informations and usages with a basic UI

## Supported platforms
Note: Getting number of packages only works on Debian GNU/Linux, Fedora Linux, Arch Linux, openSUSE Tumbleweed and distributions which based on them

- All GNU/Linux distributions

## Dependencies
### Normal packages
- Python3 (mostly python3 / openSUSE Tumbleweed: python312)
- curl (mostly curl)

### Python packages
- os, sys, getpass, threading, subprocess, datetime, socket, platform (mostly built-in)
- PyQt6 (mostly pip is used: PyQt6 / openSUSE Tumbleweed: python312-PyQt6)
- distro (mostly pip is used: distro / openSUSE Tumbleweed: python312-distro)
- psuitl (mostly pip is used: psutil / openSUSE Tumbleweed: python312-psutil)

## Running
- Warning: First install dependencies.
```curl -ssL https://raw.githubusercontent.com/MuKonqi/yasfetch/main/yasfetch.py | python3```

### License
GPLv3 or later