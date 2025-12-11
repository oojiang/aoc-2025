type Devices = dict[str, set[str]]

def read_input(filename = "input") -> Devices:
    adj = {}
    with open(filename, 'r') as file:
        for line in file:
            devices = line.split()
            in_device = devices[0][:-1]
            adj[in_device] = set(devices[1:])
    return adj
