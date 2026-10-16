import subprocess 

result = subprocess.run(
    ["sudo", "pacman", "-Syu", "--noconfirm"],
    capture_output = True,
    text = True
)

output = result.stdout
print(output)

#the problem with the previos version was that i coudln't output it to the terminal AND use the output in my script
#Just adding Text= True solved the previous problem that i had with capture_output=True



