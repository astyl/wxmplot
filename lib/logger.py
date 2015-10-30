import logging

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
wxmplotLogger = logging.getLogger('wxmplot')
wxmplotLogger.propagate
wxmplotLogger.setLevel(logging.DEBUG)
wxmplotLogger.addHandler(ch)


def getLogger():
    """ return the logger for the application """
    return logging.getLogger("wxmplot")

class LogClass(object):
    """ simple class that provide the attribute
    'log' for classes that inherit from it"""
    log = getLogger()

if __name__ == "__main__":
    class HelloClass(LogClass):       
        def print_messages(self):
            print "CHECK THE LEVELS (ERROR>WARN>INFO>DEBUG)"
            self.log.error("hello ! ERROR")
            self.log.warn("hello ! WARN")
            self.log.info("hello ! INFO")
            self.log.debug("hello ! DEBUG")
            
    hc= HelloClass()       
    hc.print_messages()
    
    