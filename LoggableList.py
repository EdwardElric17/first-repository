class LoggableList(list, Loggable):
    def append(self, elem):
        super().append(elem)
        self.log(elem)
        
        