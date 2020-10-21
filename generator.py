import hashlib

def generator(path):
     with open(path) as f:
        lines = f.readlines()
        s = 0
        while s < len(lines):
            yield (hashlib.md5(lines[s].encode())).hexdigest()
            s += 1

for item in generator("Text.txt"):
    print(item)