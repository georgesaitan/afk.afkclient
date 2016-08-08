class Test:

    def getData(self,parser):
        if parser.page_data is not None:
            location = parser.locationInfo()

            return location.__dict__