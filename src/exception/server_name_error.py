class ServerNameNotFoundError(Exception):

    def __init__(self, server_name, message="Server name not found"):
        self.server_name = server_name
        self.message = f"{message}: {server_name}"
        super().__init__(self.message)