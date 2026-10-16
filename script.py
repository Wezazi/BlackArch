import subprocess 

result = subprocess.run(
    ["sudo", "pacman", "-Syu", "--noconfirm"],
    capture_output = True,
    text = True
)


output = result.stdout
errors = result.stderr
lines = output.splitlines()


for line in lines:
    #print(lines)
    if "are in conflict" in line: #':: <x> and <y> are in conflict'
        #print(line)
        refined = line.replace("::", "")
        refined = refined.replace("are in conflict", "")
        refined = refined.strip()
        conflicts = refined.split(" and ")
    else:
        continue
        
        
print(conflicts)

#for conflict in conflict:
