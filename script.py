import subprocess 

result = subprocess.run(
    ["sudo", "pacman", "-Syu", "--noconfirm"]
)

#The script output was messier than when i manually typed the command and I'm not good with editing output layout so i removed capture_output=True and the print. 
#The script now returns the original terminal output, as if you typed the command manually
