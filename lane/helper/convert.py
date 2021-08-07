def convert_time(given_time: int, time_format: str):
    week = 518400 
    day = 86400 
    hour = 3600 
    minute = 60 

    if time_format == 'w':
        cal_time = given_time * week 
    elif time_format == 'd':
        cal_time = given_time * day 
    elif time_format == 'h':
        cal_time = given_time * hour
    elif time_format == 'm':
        cal_time = given_time * minute
    
    return cal_time