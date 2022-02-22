import subprocess
import re
import os

adb_path = os.environ["ADB-PATH"]
os.chdir(adb_path)  # go to folder with adb tool
print(os.getcwd())

def grep(cmd = ".\\adb shell pm list packages"):

    # This function grabs the output of command on the shell/terminal
    # The default command is to list the (app) packages installed on the phone
    
    # variable out is the string from the output 
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  # Argument cmd is your command
    out, err = p.communicate()
    out = out.decode("ascii")

    # Turns each output line to a list item. Each line is delimited by \r\n
    out = out.split("\r\n")

    return out

uninstall_pkg = "facebook"
r = lambda x: re.search(uninstall_pkg, x) != None  

def main():
    out = grep()
    pkg = list(filter(r, out))  # Filters to get only the packages belonging to Facebook app
    pkg = [x.removeprefix("package:") for x in pkg] # remove prefix "package:" 
    print(pkg)
    while len(pkg) != 0:
        # The loop repeats until all unwanted packages have been uninstalled

        print(pkg[-1])

        # Command to uninstall package: '.\adb shell pm uninstall --user 0 pkg_name'
        print(grep(".\\adb shell pm uninstall --user 0 {}".format(pkg[-1])))
        pkg.pop(-1)

        out = grep()
        pkg = list(filter(r, out))


if __name__ == "__main__":
    main()