with open('training_newpulwamatweets.csv','w', encoding="utf8", errors="ignore") as newfile:
    with open('mytraining_pulwama.csv','r+', encoding="utf8", errors="ignore") as file:
        for line in file:
            if (not line.isspace()):
                newfile.write(line)