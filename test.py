import arrow
import datetime
import main
from dateutil import tz



DT1 = arrow.get('11/20/2015 10:00', 'MM/DD/YYYY hh:mm').isoformat()
DT2 = arrow.get('11/20/2015 12:00', 'MM/DD/YYYY hh:mm').isoformat()
DT3 = arrow.get('11/19/2015 13:00', 'MM/DD/YYYY hh:mm').isoformat()
DT4 = arrow.get('11/19/2015 14:00', 'MM/DD/YYYY hh:mm').isoformat()
DT5 = arrow.get('11/23/2015 10:00', 'MM/DD/YYYY hh:mm').isoformat()
DT6 = arrow.get('11/23/2015 15:00', 'MM/DD/YYYY hh:mm').isoformat()
DT7 = arrow.get('11/22/2015 10:00', 'MM/DD/YYYY hh:mm').isoformat()
DT8 = arrow.get('11/24/2015 11:00', 'MM/DD/YYYY hh:mm').isoformat()
D1 = arrow.get('11/26/2015', 'MM/DD/YYYY').isoformat()
D2 = arrwo.get('11/23/2015', 'MM/DD/YYYY').isoformat()


event1 = [{"start":{"dateTime": DT1}, "end":{"dateTime":DT2}},{"start":{"dateTime":DT3},"end":
{"dateTime":DT4}},{"start":{"date":D1}, "end":{"date": D2}}]

event2 = [{"start":{"dateTime": DT7}, "end":{"dateTime":DT8}}]

event3 = []


calendar1 = {"events": event1}
calendar2 = {"events": event2}
calendar3 = {"events":event3}

calendars1 = [calendar1]
calendars2 = [calendar2]
calendars3 = [calendar1,calendar2]
calendars4 = [calendar3]
calendars5 = []

bound1 = {"begin_dateTime": arrow.get('11/19/2015 09:00','MM/DD/YYYY hh:mm').isoformat()
		   "end_dateTime": arrow.get('11/23/2015 14:00','MM/DD/YYYY hh:mm').isoformat()
		   "begin_date": arrow.get('11/19/2015','MM/DD/YYYY').isoformat()
		   "end_date":arrow.get('11/23/2015', 'MM/DD/YYYY').isoformat()
		   }
bound2 = {"begin_dateTime": arrow.get('11/19/2015 11:00','MM/DD/YYYY hh:mm').isoformat()
		   "end_dateTime": arrow.get('11/23/2015 13:00','MM/DD/YYYY hh:mm').isoformat()
		   "begin_date": arrow.get('11/19/2015','MM/DD/YYYY').isoformat()
		   "end_date":arrow.get('11/23/2015', 'MM/DD/YYYY').isoformat()
		   }



"""
check dateTime events
check a free time interval is removed when it contained within events
check a free time interval correctly updates the left endpoint when an event
intersects from the left
"""
def freeTime1():
	result = main.get_free_time(calendar3, bound1)
	print(result)
	assert result == [
					[arrow.get('11/18/2015 09:00','MM/DD/YYYY hh:mm').isoformat(),arrow.get('11/18/2015 17:00', 'MM/DD/YYYY hh:mm').isoformat()]
					[arrow.get('11/19/2015 09:00','MM/DD/YYYY hh:mm').isoformat(),arrow.get('11/19/2015 17:00', 'MM/DD/YYYY hh:mm').isoformat()]
					[arrow.get('11/23/2015 09:00','MM/DD/YYYY hh:mm').isoformat(),arrow.get('11/23/2015 17:00', 'MM/DD/YYYY hh:mm').isoformat()]
					]

"""
check date events
check default time interval 
"""

def freeTime2():
	result = main.get_free_time(calendar3,bound2)
	print(result)
	assert result == [
					[arrow.get('11/19/2015 08:00','MM/DD/YYYY hh:mm').isoformat(),arrow.get('11/19/2015 17:00', 'MM/DD/YYYY hh:mm').isoformat()]
					[arrow.get('11/23/2015 08:00','MM/DD/YYYY hh:mm').isoformat(),arrow.get('11/23/2015 17:00', 'MM/DD/YYYY hh:mm').isoformat()]
					]



"""
check empty calendar list
check default time interval 
"""

def freeTime3():
	result = main.get_free_time(calendars5,bound1)
	print(result)
	assert result == [
						[arrow.get('11/19/2015 08:00','MM/DD/YYYY hh:mm').isoformat(),arrow.get('11/19/2015 17:00', 'MM/DD/YYYY hh:mm').isoformat()]
						[arrow.get('11/23/2015 08:00','MM/DD/YYYY hh:mm').isoformat(),arrow.get('11/23/2015 17:00', 'MM/DD/YYYY hh:mm').isoformat()]
						]
















