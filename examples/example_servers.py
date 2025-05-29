import sys
sys.path.append(".")

from aq3d_api.containers.servers import Servers


def get_servers() -> Servers:
    # Creating a Servers instance which fetches the server data
    # from the api directly and automatically updates with fresh data.
    return Servers({
        "auto-update": True,
        "update-interval": 60
    })


if __name__ == "__main__":
     # Create an Servers container with all servers.
    servers = get_servers()
    # Update the items container at least once to gather the API data.
    servers.update()

    # Print all server names and their statuses
    for server in servers:
        print(f"Server: {server.name}, Status: {server.status}")

    # Sorts the server by decending order of players
    # only if the servers are online.
    sorted_servers = servers.sorted_servers(online=True)

    # Gets the server with the most players.
    highest_populated_server = servers.highest_population

    # Creating a snapshot of the servers current data.
    server_snaps = servers.create_snapshots()
    print("Server snapshots created:", server_snaps)
