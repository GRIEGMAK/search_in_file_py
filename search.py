import os, sys
file = sys.argv[1]
file_results = sys.argv[2]
string = sys.argv[3]
if not os.path.exists(file):
    file_name = open(file, "w")
    file_name.close()
file_name_search = open(file_results, "a")
f = open(file)
for line in f:
    if line.find(string) != -1:
        file_name_search.write(line)
f.close()