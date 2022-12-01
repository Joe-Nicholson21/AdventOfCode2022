def Day_One(data):
    elves = [i for i in data.strip().split("\n\n")]
    elf_calories = [sum([int(cals)for cals in elf.split()]) for elf in elves]
    sorted_elves = sorted(elf_calories)
    return max(elf_calories),sum(sorted_elves[-3:])
    
    


if __name__ == '__main__':
    data = open("day1.txt").read()
    part1,part2=Day_One(data)
    print("Part1: ", part1, "\nPart2:", part2)
    data.close()