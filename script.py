import subprocess 

result = subprocess.run(
    ["sudo", "pacman", "-Syu", "--noconfirm"],
    capture_output = True,
    text = True
)


output = result.stdout
errors = result.stderr
lines = output.splitlines()


conflicts = []


for line in lines:
    if "are in conflict" in line: #':: <x> and <y> are in conflict'
        refined = line.replace("::", "")
        refined = refined.replace("are in conflict", "")
        refined = refined.strip()
        problems = refined.split(" and ")
        for problem in problems:
            conflicts.append(problem)
    else:
        continue
        
        
def removeFunction(conflicts):
    return subprocess.run(
        ["sudo", "pacman", "-R", "--noconfirm", *conflicts], # The asterisk in *conflicts outputs each item in the list a seperate package in the command. My earlier script did joined = " ".join(conflicts) and then i set joined inside ["sudo", "pacman", "-R", joined] but this is wrong because joined got interpreted as a single package names
        capture_output = True,
        text = True
    )
    
    
remove = removeFunction(conflicts)

output = remove.stdout
errors = remove.stderr


lines = output.splitlines()

for line in lines:
    if "required by" in line:
        refined = line.split("required by ")
        problem = refined[1]
        if problem in conflicts:
            continue
        else:
            conflicts.append(problem)
    else:
        continue
        
eLines = errors.splitlines()
for line in eLines:
    if "target not found:" in line:
        refined = line.split("target not found: ")
        unFound = refined[1]
        conflicts.remove(unFound)
        removeFunction(conflicts)
    
        

        



