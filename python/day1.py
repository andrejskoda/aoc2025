
def process_input(num: int, command: str) -> int:
    direction = command[0]
    value = int(command[1:])
    if direction == 'L':
        return (num - value) % 100
    elif direction == 'R':
        return (num + value) % 100
    else:
        raise ValueError("Command must start with 'L' or 'R'")

def process_sequence(start_num: int, commands: list[str]) -> int:
    num = start_num
    zero_count = 0
    for command in commands:
        num = process_input(num, command)
        if num == 0:
            zero_count += 1
    return zero_count


def read_commands_from_file(file_path: str) -> list[str]:
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]


def main() -> None:
    start_num = 50
    commands = read_commands_from_file('day1.txt')
    print(process_sequence(start_num, commands))

if __name__ == "__main__":
    main()