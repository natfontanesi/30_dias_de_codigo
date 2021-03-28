def make_readable(seconds):
    hh=seconds//3600 
    mm= seconds //60 %60
    ss= seconds %60
    
    
    str = "{:02d}:{:02d}:{:02d}".format(hh,mm,ss)
    
    return str
    

    