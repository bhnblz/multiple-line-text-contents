def write_lines():
    # Open a file
    with open("write_file.txt", "w") as my_file:
        # while true
        while True:
            # Input line
            line = input("Enter line: ")
            my_file.write(line)
    
            # If you will input more lines
            choices = input("Are there more lines? If so, enter Y for yes and N for no: ")
            
            # If choices is N, break
            if choices == "N":
                break
        my_file.close()

# Call the function
write_lines()