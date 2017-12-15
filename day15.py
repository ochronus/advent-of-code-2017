def solve(generator_a, generator_b, iter_count, part2):
    count = 0
    for i in range(iter_count):
        while True:
            generator_a = (generator_a * 16807) % 2147483647
            if not part2 or generator_a % 4 == 0:
                break
        while True:
            generator_b = (generator_b * 48271) % 2147483647
            if not part2 or generator_b % 8 == 0:
                break
        if (generator_a & 65535 == generator_b & 65535):
            count += 1
    return count


print(solve(289, 629, 40000000, False))
print(solve(289, 629, 5000000, True))
