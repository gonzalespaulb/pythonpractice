# file = open("./100days/test.txt")
# contents = file.read()
# print(contents)
# file.close()

# This way you won't have to remember to close the file
# W will overwrite everything
# A will append it to the next line
# Cannot use two different modes

with open("./100days/test.txt", mode="a") as file:
    # contents = file.read()
    # print(contents)
    file.write("This is Paul Again!!!")