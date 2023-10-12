from datetime import datetime
class Agecalculator:
    def __init__(self,bday,bmonth,byears) -> None:
        # get current date and time and store it
        self.__nowdate=datetime.now()
        # get current year and store it
        self.__currentyear=int(self.__nowdate.strftime('%Y'))
        # get current month and store it
        self.__currentmonth=int(self.__nowdate.strftime('%m'))
        # get current day and store it
        self.__currentday=int(self.__nowdate.strftime('%d'))
        # get user birth day and store it
        self.__days=int(bday)
        # get user month day and store it
        self.__month=int(bmonth)
        # get user birth year and store it
        self.__years=int(byears)
        # get user age in year and month and days after age calculate
        self.__getyear=self.__age()['years']
        self.__getmonth=self.__age()['month']
        self.__getdays=self.__age()['days']
        # create function instanse variable create for __age function and __gettotaldays
        self.getage=self.__age
        self.getdays=self.__gettotaldays
    # create method for calculate of age    
    def __age(self):
        if(self.__currentday>self.__days) and (self.__currentmonth>self.__month) and (self.__currentyear>self.__years):
            days=self.__currentday-self.__days
            month=self.__currentmonth-self.__month
            years=self.__currentyear-self.__years
            age={
                "days":days,
                "month":month,
                "years":years
            }
            return age
        elif(self.__currentday<self.__days) and (self.__currentmonth>self.__month) and (self.__currentyear>self.__years):
            days=(self.__currentday+30)-self.__days
            month=(self.__currentmonth-1)-self.__month
            years=self.__currentyear-self.__years
            age={
                "days":days,
                "month":month,
                "years":years
            }
            return age
        elif(self.__currentday<self.__days) and (self.__currentmonth<self.__month) and (self.__currentyear>self.__years):
            days=(self.__currentday+30)-self.__days
            month=(self.__currentmonth-1)-self.__month
            month=(self.__currentmonth+12)-self.__month
            years=(self.__currentyear-1)-self.__years
            years=self.__currentyear-self.__years
            age={
                "days":days,
                "month":month,
                "years":years
            }
            return age
        elif(self.__currentday<self.__days) or (self.__currentday>self.__days) and (self.__currentmonth<self.__month) or (self.__currentmonth>self.__month) and (self.__currentyear<self.__years):
            try:
                raise ValueError('your age years is greater than from current year')
            except ValueError as obj:
                return f'ValueError!: {obj}'
    # create this method for calculate age in days        
    def __gettotaldays(self):
        return ((self.__getyear*365)+(self.__getmonth*30)+(self.__getdays))
