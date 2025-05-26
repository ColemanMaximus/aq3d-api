from aq3d_api.servers import Servers


def get_servers() -> Servers:
    return Servers(fromapi=True, auto_update_fromapi=True)


servers = get_servers()
