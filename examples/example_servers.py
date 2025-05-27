from aq3d_api.containers.servers import Servers


def get_servers() -> Servers:
    # Creating a Servers instance which fetches the server data
    # from the api directly and automatically updates with fresh data.
    return Servers(fromapi=True,
                   auto_update_fromapi=True,
                   update_interval=60)


servers = get_servers()

# Creating a snapshot of the servers current data.
server_snaps = servers.create_snapshots()
