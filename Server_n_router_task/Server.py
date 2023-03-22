class Server:
    __current_ip = 0

    def __init__(self):
        # Отвечает за присвоение ip серверу
        self.__ip = Server.__current_ip
        Server.__current_ip += 1

        # создание баффера и привязка экземпляра роутера к серверу
        self.__buffer = []
        self.__vault = []
        self.__router = None

    def get_ip(self):
        """ Returns server ip """
        return self.__ip

    def get_buffer(self):
        """Returns server buffer"""
        return self.__buffer

    def get_data(self):
        """Returns data from vault of server"""
        return self.__vault

    def unlink_router(self):
        """Unlinks router from the server"""
        self.__router = None

    def link_router(self, router):
        """Links server to the router"""
        self.__router = router

    def send_data(self, data):
        """call 'append_data method from Router class'
        that appends some Data to router buffer """
        self.__router.append_data(data)

    def accept_data(self, data):
        """ built-in method called by Router, that accepts any data from argument to buffer
         then calls buffer_to_vault method, that append data from buffer to vault
         and lastly empties the server buffer """
        self.__buffer.append(data)
        self.buffer_to_vault()
        self.__buffer = []

    def buffer_to_vault(self):
        """built-in method called by accept_data that accepts data from zero index of the buffer """
        self.__vault.append(self.__buffer[0])
