import subprocess 

while True:
    result = subprocess.run(
        ["sudo", "pacman", "-Syu", "--noconfirm"],
        capture_output = True,
        text = True
    )


    output = result.stdout
    errors = result.stderr
    lines = output.splitlines()
    for line in lines:
        print(line)


    #changed to set instead of list to make sure each value is unique
    conflicts = set() #this confused me because initially i did conficts = {} which gave me an error: "dict object has no add attribute. So it created a dictionary instead of a set which is why i got that error. When declaring sets you need to use set() but if you are declaring and defining you can type it like this: conflicts = {<value1>, <value2>, etc} because then it can see whether it's a set or dict based on if the curly brackets contains values or key:value pairs
    
    
    
    if "are in conflict" in output:

        for line in lines:
            if "are in conflict" in line:
                refined = line.replace("::", "")
                refined = refined.split(" are in conflict")
                refined = refined[0]
                refined = refined.strip()
                problems = refined.split(" and ")
                for problem in problems:
                    conflicts.add(problem)
            else:
                continue
    elif "breaks dependency" in output:
        for line in lines:
            if "breaks dependency '" in line:
                refined = line.split("' required by ")
                refined = refined[1]
                problem = refined.strip()
                conflicts.add(problem)
                
    elif "exists in filesystem" in output:
        for line in lines:
            if "exists in filesystem" in line and "owned by" in line:
                #.replace() doesn't seem to work for some unknown reason so i changed i'm gonna tru .split() instead
                refined = line.split(")")
                refined = refined[0]
                refined = line.split("owned by ")
                refined = refined[1]
                problem = refined.strip()
                conflicts.add(problem)
                
            elif "exists in filesystem" in line:
                refined = line.split(" exists in filesystem")
                refined = refined[0]
                refined = refined.rsplit("/", 1)
                refined = refined[1]
                problem = refined.strip()
                conflicts.add(problem)
                
            else:
                continue
            
    elif "exists in both" in output:
        for line in lines:
            if "exists in both" in line:
                refined = line.split("exists in both ")
                refined = refined [1]
                refined = refined.strip()
                refined = refined.replace("'", "")
                problems = refined.split(" and ")
                for problem in problems:
                    conflicts.add(problem)
                                

    else:
        break
                
            
    while True:  
        print(conflicts)
        def removeFunction(conflicts):
            return subprocess.run(
                ["sudo", "pacman", "-R", "--noconfirm", *conflicts], # The asterisk in *conflicts outputs each item in the list as a seperate package in the command. My earlier script did joined = " ".join(conflicts) and then i set joined inside ["sudo", "pacman", "-R", joined] but this is wrong because joined got interpreted as a single package name
                capture_output = True,
                text = True
            )
            
            
        remove = removeFunction(conflicts)
        output = remove.stdout
        errors = remove.stderr
        
        if "required by" in output:
            lines = output.splitlines()
            for line in lines:
                if "required by" in line:
                    refined = line.split("required by ")
                    problem = refined[1]
                    if problem in conflicts:
                        continue
                    else:
                        conflicts.add(problem)
                else:
                    continue
                
        #Don't underestimate how big of a difference this does:
        elif "target not found:" in errors:
            lines = errors.splitlines()
            for line in lines:
                if "target not found:" in line:
                    refined = line.split("target not found: ")
                    unFound = refined[1]
                    conflicts.remove(unFound)
                else:
                    continue
        
        else:
            break
            
        
        
#To make tab in nano be 4 spaces like vscode: 
#sudo nano ~/.nanorc (/root/.nanorc). Type set tabsize 4 and set tabstospaces
        