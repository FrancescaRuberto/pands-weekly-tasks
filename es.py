#This program should reads in a text file and outputs the number of e's it contains
#Author: Francesca Ruberto

def count_es(filename):
    # Import os to check file 
    import os 

    # We need to count the occurrences of the letter "e" in the text file
    # Let's assume the file exist in the same directory as our script
    # Let's also assume that the filename provided is just the name of the title

    #Let's check if the file exist
    if not os.path.exists(filename):
        #In case the file doesn't exist, we'll print an error message
        print("Error: it looks like the file doesn't exist")
        return
    
    #Let's check if the file is a text file
    if not filename.endswith(".txt"):
        #In case the file is not a text file, we'll print an error message
        print("Error: the file doesn't seem to be a txt")
        return
    
    #Let's try opening the file for reading
    file = open(filename, "r")

    #Now let's check if there are issues with reading the file
    if file is None:
        #In case an issue presents, we'll print an error message
        print("Error: it's not possibile to read the file")
        return

# Read the entire content of the file into a string
    text = file.read()
    
    # Close the file to avoid issues
    file.close()
    
    # Now, let's count how many 'e's are there in the text
    count = text.count('e')
    
    # Print the count
    print(count)

if __name__ == "__main__":
    # We're assuming that our file is named 'moby-dick.txt'.
    filename = "moby-dick.txt"
    
    # Let's call our function to count 'e's in the file
    count_es(filename)


    
   
    
