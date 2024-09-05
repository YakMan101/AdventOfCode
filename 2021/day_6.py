"""Functions to solve Day-6"""


def load_input() -> list[int]:
    """Return input data"""

    with open("input.txt", "r", encoding="utf-8") as f:
        return [int(x) for x in f.readline().strip().split(',')]


def spawn_fish(fishes: list[int]) -> list[int]:
    """
    Spawn new fish with internal clock of 8 for every -1 in fishes list
    and reset clock of any fish on -1
    """
    ...

    fishes_to_add = [8 for x in fishes if x == -1]
    fishes = [6 if x == -1 else x for x in fishes]
    fishes.extend(fishes_to_add)
    return fishes


def go_next_day(fishes: list[int]) -> list[int]:
    """
    Reduce internal clock of all fish by 1
    """

    return [x - 1 for x in fishes]


def print_fishes(day: int, fishes: list[int]) -> None:
    """Format list and print all fishes to console"""

    day_str = 'day' if day == 1 else 'days'
    print(
        f"After {day} {day_str}: Total={len(fishes)}")


def simulate_fish_life(fishes: list[int], days: int) -> int:
    """
    Go through full simulation of 'days' (spawn children, reset internal clocks)
    """

    print(f"Initial state: Total={len(fishes)}")
    for i in range(days):
        fishes = go_next_day(fishes)
        fishes = spawn_fish(fishes)
        print_fishes(i+1, fishes)
    print(f"Final state: Total={len(fishes)}")
    return len(fishes)


def simulate_fish_life_efficiently(fishes: list[int], days: int) -> int:
    """Simulate fish life more efficiently"""

    fish_count = [0] * 9

    for timer in fishes:
        fish_count[timer] += 1

    for _ in range(days):
        new_fish_count = [0] * 9
        new_fish_count[6] += fish_count[0]
        new_fish_count[8] += fish_count[0]
        for i in range(1, 9):
            new_fish_count[i - 1] += fish_count[i]
        fish_count = new_fish_count

    return sum(fish_count)


if __name__ == '__main__':

    data = load_input()
    total_days = 80

    total_fish = simulate_fish_life(data, total_days)
    print(f'1) {total_fish}')

    data = load_input()
    total_days = 256

    total_fish = simulate_fish_life_efficiently(data, total_days)
    print(f'2) {total_fish}')
