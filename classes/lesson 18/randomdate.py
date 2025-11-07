import random
import time
def getRandomDate(startdate,enddate):
    print("printing random date between " + str(startdate) + " and " + str(enddate))
    randomgenerator = random.random()
    dateformat = '%m/%d/%Y'
    starttime= time.mktime(time.strptime(startdate,dateformat))
    endtime= time.mktime(time.strptime(enddate,dateformat))
    randomtime= starttime+randomgenerator*(endtime-starttime)
    randomdate=time.strftime(dateformat,time.localtime(randomtime))
    return randomdate
print(getRandomDate("1/1/2022","12/31/2022"))