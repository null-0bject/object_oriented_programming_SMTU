class Data:

    def __init__(self, data, ip):
        self.__data = data
        self.__destination_ip = ip

    def get_string(self):
        """returns data value of the Data class"""
        return self.__data

    def get_destination_ip(self):
        """returns data destination ip of the Data class"""
        return self.__destination_ip

