

class Four_Digits(object):
    
    regex = "[0-9]{4}"

    def to_python(self,value):
        return int(value)

    def to_url(self,value):
        return F"{value:04d}"



