def bracket_check(line):
    while True:
        for i in range(len(line) - 1):
            if((line[i] == "(" and line[i+1] == ")") or 
               (line[i] == "[" and line[i+1] == "]") or 
               (line[i] == "{" and line[i+1] == "}")):
                del line[i : i+2]
                break
        else:
            return "NOT BALANCED"
        
        if(len(line) == 0):
            return "BALANCED"

line_count =  int(input())
for _ in range(line_count):
    print(bracket_check(list(input())))
