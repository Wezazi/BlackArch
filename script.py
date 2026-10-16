import subprocess 

result = subprocess.run(
    ["sudo", "pacman", "-Syu", "--noconfirm"],
    capture_output=True
)


output = result.stdout

print(output)
