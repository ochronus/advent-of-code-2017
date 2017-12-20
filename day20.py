import re
import math


def solve(part2):
    particles = []
    for i, line in enumerate(open("day20-input.txt")):
        particle = list(map(int, re.findall(r'[\-\d]+', line)))
        particle.append(i)                                      # let's simply store the particle's ID as the last item in the list
        particles.append(particle)

    for i in range(500):
        positions = {}
        for particle in particles:
            # update the velocity based on the acceleration
            particle[3] += particle[6]
            particle[4] += particle[7]
            particle[5] += particle[8]
            # update the position based on the velocity
            particle[0] += particle[3]
            particle[1] += particle[4]
            particle[2] += particle[5]
            if part2:                                           # let's keep track of all particles per position triplet
                p = (particle[0], particle[1], particle[2])
                if p not in positions:
                    positions[p] = []
                positions[p].append(particle)
        if part2:                                               # time to remove collided particles
            for particles_in_pos in positions.values():
                if len(particles_in_pos) > 1:
                    for particle in particles_in_pos:
                        particles.remove(particle)

    if part2:
        print(len(particles))
    else:
        distances = [(math.sqrt(particle[0]**2 + particle[1]**2 + particle[2]**2), particle[9]) for particle in particles]
        print(list(sorted(distances))[0][1])


solve(False)
solve(True)
