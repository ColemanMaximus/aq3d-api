import aq3d_api.servers as servers

server = servers.Server(1, "Red Dragon")
server.max_players = 5000
server.players = 500
print(server.name, server.max_players, server.is_full)
