filename = "chat.txt"

# Function called to return a list of 
# dictionaries. Each dictionary is an 
# individual message 
def get_chat():
    full_chat = []
    with open(filename) as file:
        for line in file:
            cleaner = line.rstrip("\n\r")
            full_chat.append({"message": cleaner})
    return full_chat
    #return {"message":"Why?"}


# Function called to add to messages
# by writing the new message to the end of 
# the file
def add_message(message):
    with open(filename, "a") as file:
        file.write(message + "\n")
