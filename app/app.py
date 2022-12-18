import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    function_temp_memory = list()
    file_name=str(input_file_name)
    
    with open(file_name) as f:
        reader = csv.reader(f)
        for row in reader:
            function_temp_memory.append(row)
        counter = 1000
        data_stored = list()
        while counter < 10000 :
            for g in range(0,len(function_temp_memory)):
                code = str(counter)
                if hashlib.sha256(code.encode('utf-8')).hexdigest() == function_temp_memory[g][1]:
                    data_stored.append([function_temp_memory[g][0],counter]) 
            counter += 1

        
    with open(output_file_name, 'w', newline="",) as f:
        writer = csv.writer(f)
        for i in data_stored:
            writer.writerow(i)
        
# thank you jaddi you were awsome
