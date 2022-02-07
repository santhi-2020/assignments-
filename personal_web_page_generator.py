#This program constructs simple HTML
name = input('Enter your name: ')
description = input('Describe yourself: ')

#construct the string using user input
data = "<head></head><body><center><h1>%s</h1></center><hr>%s</hr></body></html>" % (name , description) 

#open the file with the name and write the content
with open(r'C:\Users\psanthi\Downloads\ass-3\todaysNBAScores.html', 'w') as htmlfile:
    htmlfile.write(data)
    htmlfile.close()
