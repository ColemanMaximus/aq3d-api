import requests
from aq3d_api.servers import Server

servers_api_url = "https://game.aq3d.com/api/game/GetServerList"

def get_servers(url: str) -> list:
    json_res = requests.get(url).json()
    return [Server.create_raw(server) for server in json_res["Servers"]]

servers = get_servers(servers_api_url)