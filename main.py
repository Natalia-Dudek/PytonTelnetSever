import asyncio
import subprocess

clients = []


class Client:
    counter = 1

    def __int__(self, reader, writer):
        self.reader = reader
        self.writer = writer
        self.id = Client.counter
        Client.counter += 1
        print("New client id == ", self.id)

    async def read(self):
        receive_data = await self.reader.read(1000000)
        message = receive_data.decode().strip()
        print("ID:", self.id, "message:", message)

    def write(self, data):
        self.writer.write(data.encode())


async def handle_client(reader, writer):
    client = Client(reader,writer)


# print(f"Connected to {writer.get_extra_info('peername')}")
#
# while True:
# 	data = await reader.read(100000)
# 	message = data.decode().strip()
# 	if not message:
# 		break
# 	print(f"Received message: {message}")
# print("Closing connection")
# writer.close()


async def start_server():
    server = await asyncio.start_server(handle_client, "127.0.0.1", 2000)
    print("Server started")
    await server.serve_forever()


asyncio.run(start_server())
