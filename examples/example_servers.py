from aq3d_api.servers import Servers


def get_servers() -> Servers:
    return Servers(fromapi=True)


servers = get_servers()
