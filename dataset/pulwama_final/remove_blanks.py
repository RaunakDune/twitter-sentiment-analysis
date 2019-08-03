lines_seen = set()
with open('testing_newpulwamatweets.csv','w', encoding="utf8", errors="ignore") as newfile:
    with open('testingjusttweetspulwama.csv','r+', encoding="utf8", errors="ignore") as file:
        for line in file:
            if (not line.isspace()) and (line.strip("\n") != '""') and (line not in lines_seen):
                newfile.write(line)
                lines_seen.add(line)