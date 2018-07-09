datafile_write = open("data/data.txt", 'a')

# raw_data = datafile_read.read()
#
# data = raw_data.split("\n")

def getHighScore():
    with open("data/data.txt", 'r') as datafile:

        biggest = 0
        for i in datafile.read().split("\n"):
            try:
                biggest = int(i) if int(i) > biggest else biggest
            except ValueError:
                break

        return biggest

def appendHighscore(score):
    with open("data/data.txt", 'a') as datafile:

        score = int(score)

        datafile.write(f"{score}\n")

appendHighscore(1213)
print(getHighScore())

#
# datafile_read.close()
# datafile_write.close()