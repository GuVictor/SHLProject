def max_energy(reac_capacity, critical_mass, volumes, masses, energies):
    """Return the maximum energy using a 2-constraint 0/1 knapsack.

    dp[m][v] holds the best energy achievable with total mass at most m
    and total volume at most v, considering the liquids processed so far.
    """
    dp = [[0] * (reac_capacity + 1) for _ in range(critical_mass + 1)]

    for volume, mass, energy in zip(volumes, masses, energies):
        for m in range(critical_mass, mass - 1, -1):
            dp_m = dp[m]
            prev_row = dp[m - mass]
            for v in range(reac_capacity, volume - 1, -1):
                candidate = prev_row[v - volume] + energy
                if candidate > dp_m[v]:
                    dp_m[v] = candidate

    return dp[critical_mass][reac_capacity]


def main():
    import sys

    data = sys.stdin.read().splitlines()
    reac_capacity = int(data[0])
    critical_mass = int(data[1])
    num_volumes = int(data[2])
    volumes = list(map(int, data[3].split()))
    num_masses = int(data[4])
    masses = list(map(int, data[5].split()))
    num_energy = int(data[6])
    energies = list(map(int, data[7].split()))

    print(max_energy(reac_capacity, critical_mass, volumes, masses, energies))


if __name__ == "__main__":
    main()
