import re
REGEXP_PUNCTUATIONS = re.compile(
    r"\/`~!@#$%^&*()_\\-+=<>?:\"\|,.\/;'\\\·~！@#￥%……&*（）——\-+=\|《》？：“”、；‘'，。、"
)

def cleaning(s):
    s = str(s)
    s = REGEXP_PUNCTUATIONS.sub("",s.strip())
    s = re.sub('\s\W',' ',s)
    s = re.sub('\W,\s',' ',s)
    s = re.sub("\d+","",s)
    s = re.sub("\s+",' ',s)
    s = re.sub('[!@#$_]','',s)
    s = s.replace("co","")
    s = s.replace("https","")
    s = s.replace("[\w*]"," ")
    return s

