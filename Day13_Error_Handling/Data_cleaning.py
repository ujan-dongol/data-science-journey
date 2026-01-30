
data = [12, 4, 5, "sbv", "", "25"]

clean_data = []

for value in data:
    try: 
        clean_data.append(int(value))
    except ValueError:
        print("Invalid data skipped:", value) 
        
print("Clean data :", clean_data)           