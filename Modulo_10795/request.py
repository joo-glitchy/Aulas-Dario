import requests as re


for i in range(6500, 7194):
    request=re.get("https://trainingserver.atec.pt/TrainingServer/Mulberry/JSON/Controls/Calendar/getCalendarDataSource.ashx?command=_SelectAllSchedulesDataSetGivenByUserId&oId=14529&idField=DataValueField&titleField=DataTextField&startDateField=DataStartField&endDateField=DataEndField&backgroundColorField=&textColorField=textcolor&eventColorField=color&description=description&picField=pic&urlField=url&start=1771804800&end=1772409600&_=1771938550463")
    for key, value in request.text.json():
        if "Pedro Carlos Mestre dos Santos" in value:
            print({key:value})

    
