import subprocess
subprocess.call(["powershell.exe", "D:\Python\getserverinfo.ps1"])
subprocess.call(["powershell.exe", "(get-service).Name"])

#subprocess.Popen('echo "Arockia"', shell=True)
#p = subprocess.Popen(["powershell.exe", "D:\Python\getserverinfo.ps1"])
#p.communicate()

#subprocess.run('echo "Arockia"', shell=True)

