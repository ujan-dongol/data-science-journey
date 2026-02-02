
def load_marks(filename):
    marks = []
    
    file = open(filename, "r")
    for line in file:
        if line.strip():
            marks.append(int(line.strip()))
    file.close()
    
    return marks        