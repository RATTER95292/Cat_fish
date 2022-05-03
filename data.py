import datetime

class clock:
    def __init__():
        pass
    def data(x):
        now = str(datetime.datetime.now())
        #ГОД
        year = now[0:4]

        #МЕСЯЦ
        _month_ = now[5:7]
        if int(_month_[0]) == 0:
            month = _month_[1]
        else:
            month = _month_
        if month == '1':
            _month_ = 'января'
        elif month == '2':
            _month_ = 'февраля'
        elif month == '3':
            _month_ = 'марта'
        elif month == '4':
            _month_ = 'апреля'
        elif month == '5':
            _month_ = 'мая'
        elif month == '6':
            _month_ = 'июня'
        elif month == '7':
            _month_ = 'июля'
        elif month == '8':
            _month_ = 'августа'
        elif month == '9':
            _month_ = 'сентября'
        elif month == '10':
            _month_ = 'октября'
        elif month == '11':
            _month_ = 'ноября'
        elif month == '12':
            _month_ = 'декабря'
        #ЧИСЛО
        _data_ = now[8:10]
        if int(_data_[0]) == 0:
            data = _data_[1]
        else:
            data = _data_
        if x == 1:
            data = data+' '+_month_+' '+year+' года'
        elif x  == 0:
            data = data+'/'+month+'/'+year
        return data
    def time():
        now = str(datetime.datetime.now())
        #ЧАС
        _hour_ = now[11:13]
        if int(_hour_[0]) == 0:
            hour = _hour_[1]
        else:
            hour = _hour_
        #МИНУТЫ
        _minute_ = now[14:16]
        if int(_minute_[0]) == 0:
            minute = _minute_[1]
        else:
            minute = _minute_
            time = hour+':'+minute
        return time
