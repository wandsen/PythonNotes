import time, subprocess

timeLeft = 60

while timeLeft > 0 :
    print('\n', timeLeft, end="")
    time.sleep(1)

    #this opens the chrome browswer and inputs the url
    if(timeLeft == 58):
        subprocess.Popen(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", 'www.facebook.com'])

    if(timeLeft == 57):
        subprocess.Popen(["C:\\Windows\\System32\\calc.exe"])
    if(timeLeft == 59):
        #opens the textfile
        subprocess.Popen(["start", "testfile2.txt"],  shell=True)
    timeLeft -= 1

    

