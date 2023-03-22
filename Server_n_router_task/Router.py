class Router:

    def __init__(self):
        # Buffer of the Router
        self.__buffer = []
        # Set of servers, to simplify the link/unlink method
        self.__servers = set()

    def append_data(self, data):
        """method appends data to buffer, called by Server"""
        self.__buffer.append(data)

    def link(self, server):
        """Links the server to the router, by calling link_router method.
        Then appends Server object to set of Servers"""
        server.link_router(self)
        self.__servers.add(server)

    def unlink(self, server):
        """unlinks server from the router by calling unlink_router method
        Then removes server object from set of Servers"""
        server.unlink_router()
        self.__servers.remove(server)

    def get_data(self):
        """Returns buffer of Router"""
        return self.__buffer

    def get_connected_servers_ip(self):
        """Return list of connected ips"""
        return [i.get_ip() for i in self.__servers]

    def send_data(self):
        """
        servers : [list]
            Because set is unsubscript-able we need to use list

        ips : [list]
            List of connected servers

        Goes over all data and uses method Server.accept_data

        Server names goes from servers list by indexing ips (ip number getting destination ip
        using data.get_destination_ip) and sends decrypted Data without destination IP.
        """
        servers = list(self.__servers)
        ips = self.get_connected_servers_ip()
        for data in self.__buffer:
            if data.get_destination_ip() in ips:
                servers[ips.index(data.get_destination_ip())].accept_data(data.get_string())
        self.__buffer = []





