class clockTime:

    hours = 0
    minutes = 0
    seconds = 0

    # setting values
    # set hour values
    def setHours(self, hours):
        self.hours = hours

    # set minute values
    def setMinutes(self, minutes):
        self.minutes = minutes

    # set seconds values
    def setSeconds(self, seconds):
        self.seconds = seconds

    # set time to set values of seconds, minutes and hours calling their respective functions
    def setTime(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    # set time format in hours:minutes:seconds
    def showTime(self):
        print(str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds))

clock = clockTime()

#get user input for hours, minutes, seconds
hours = input("Enter integer value for hours: ")

while int(hours) > 23 or int(hours) < 0:
    print("Please enter a value between 0-23.")
    hours = input("Enter integer value for hours: ")

minutes = input("Enter integer value for minutes: ")

while int(minutes) > 59 or int(minutes) < 0:
    print("Please enter a value between 0-59.")
    minutes = input("Enter integer value for minutes: ")

seconds = input("Enter integer value for seconds: ")

while int(seconds) > 59 or int(seconds) < 0:
    print("Please enter a value between 0-59.")
    seconds = input("Enter integer value for seconds: ")

#set object time
clock.setTime(hours, minutes, seconds)

#print out the values
clock.showTime()