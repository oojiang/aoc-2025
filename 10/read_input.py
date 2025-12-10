import re

type Indicators = tuple[bool, ...]
type Button = set[int]
type Machine = tuple[Indicators, list[Button]]

def read_input(filename = "input") -> list[Machine]:
    machines = []
    with open(filename, 'r') as file:
        for line in file:
            machines.append(machine(line))
    return machines

def machine(s: str) -> Machine:
    pattern = r"\[(.*)\] (.*) {(.*)}"
    indicator_s, buttons_s, _ = re.match(pattern, s).groups()
    return (indicator(indicator_s), buttons(buttons_s))

def indicator(s: str) -> Indicators:
    return tuple(c == '#' for c in s)

def buttons(s: str) -> list[Button]:
    pattern = r"\(([^)]*)\)"
    return [button(ss) for ss in re.findall(pattern, s)]

def button(s: str) -> Button:
    return set(int(ss) for ss in s.split(','))
