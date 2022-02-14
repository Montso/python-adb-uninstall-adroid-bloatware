import subprocess
import re
import os

os.chdir("C:/Users/monts/Downloads/platform-tools")
print(os.getcwd())

def grep(cmd = ".\\adb shell pm list packages"):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    out = out.decode("ascii")
    out = out.split("\r\n")

    return out

r = lambda x: re.search("facebook", x) != None

def main():
    out = grep()
    pkg = list(filter(r, out)) 
    pkg = [x.removeprefix("package:") for x in pkg] # remove prefix "package:" 
    print(pkg)
    while len(pkg) != 0:
        print(pkg[-1])
        print(grep(".\\adb shell pm uninstall --user 0 {}".format(pkg[-1])))
        pkg.pop(-1)

        out = grep()
        pkg = list(filter(r, out))


if __name__ == "__main__":
    main()