import re

type Joltage = tuple[int, ...]
type Indicators = tuple[bool, ...]
type Button = set[int]
type Machine = tuple[Indicators, list[Button], Joltages]

def read_input(filename = "input") -> list[Machine]:
    machines = []
    with open(filename, 'r') as file:
        for line in file:
            machines.append(machine(line))
    return machines

def machine(s: str) -> Machine:
    pattern = r"\[(.*)\] (.*) {(.*)}"
    indicator_s, buttons_s, joltage_s = re.match(pattern, s).groups()
    return (indicator(indicator_s), buttons(buttons_s), joltage(joltage_s))

def indicator(s: str) -> Indicators:
    return tuple(c == '#' for c in s)

def buttons(s: str) -> list[Button]:
    pattern = r"\(([^)]*)\)"
    return [button(ss) for ss in re.findall(pattern, s)]

def button(s: str) -> Button:
    return set(int(ss) for ss in s.split(','))

def joltage(s: str) -> Joltage:
    return tuple(int(ss) for ss in s.split(','))
