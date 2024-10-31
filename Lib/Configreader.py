from configparser import ConfigParser

def readdata(sec_name,key):
    config = ConfigParser()
    config.read("../Config/config.cfg")
    print(config.sections())
    #Email = config.get("login", "email")
    return config.get(sec_name,key)


def readElement(sec_name,key):
    config = ConfigParser()
    config.read("../Config/Elements.cfg")
    return config.get(sec_name,key)

#print(readdata("login", "email"))