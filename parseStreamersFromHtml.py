import re

# This program extracts a string between [original-title="] and [">] without the
# brackets, appends the extracted string onto a twitch.tv URL, and outputs it 
# into a file named "links.html". This primarily useful if to create a list of 
# selectable Twitch.tv profile links out of an HTML document taken from a Twitch
# user's 'Following' page.

# Opens fileWithHtmlCode.txt file in read mode. This is the file with the HTML 
# code.
with open('fileWithHtmlCode.txt', 'r') as readMe:
    # Initialize a variable for total number of streamers.
    numStreamers = 0

    # Creates a new file links.html.
    newFile = open("newFileLinks.html", "w")

    # Writes the HTML tags.
    newFile.write("<html>\n<body>\n")

    # For each line as "line" variable in fileWithHtmlCode.txt...
    for line in readMe:
        # If a line has the string 'ember' in it...
        if 'ember' in line:

            # Inserts search parameter for desired string.
            lineFound = re.search('original-title="(.+?)">', line)

            if lineFound:
                desiredString = lineFound.group(1)

                # Appends Twitch name to URL and output to console.
                print("www.twitch.tv/" + desiredString)

                # Writes the full selectable link with the Twitch name appended.
                newFile.write("<a href=\"https://www.twitch.tv/"+desiredString+\
                    "\">"+desiredString+"</a><br>\n")

                # Increments the count variable.
                numStreamers += 1
    # Writes the rest of the HTML tags.
    newFile.write("</body>\n</html>\n")

print(numStreamers)
