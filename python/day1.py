def process_input(num: int, command: str) -> tuple[int, int]:
    direction = command[0]
    value = int(command[1:])

    full_cycles, leftover = divmod(value, 100)
    print(full_cycles, leftover)
    zero_hits = full_cycles

    if num != 0:
        if direction == 'R' and leftover >= 100 - num:
            zero_hits += 1
        elif direction == 'L' and leftover >= num:
            zero_hits += 1

    if direction == 'R':
        num = (num + value) % 100
    elif direction == 'L':
        num = (num - value) % 100
    else:
        raise ValueError("Command must start with 'L' or 'R'")
    return zero_hits, num


def process_sequence(start_num: int, commands: list[str]) -> int:
    num = start_num
    zero_count = 0
    for command in commands:
        hits, num = process_input(num, command)
        zero_count += hits
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
