infile = open('password.txt', 'r')  # opening files
text = infile.read()
infile.close()

print(text)
# outfile = for saving files