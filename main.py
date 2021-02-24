import minimisation


def main():

    epsilon = 2.0

    parameters = minimisation.perform_minimise(epsilon)
    with open(f"../parameters_{int(epsilon)}.txt", "w") as file:
        file.write(f"solvent = {int(epsilon)}")
        file.write(f"parameterised radial shift = {parameters}")


if __name__ == "__main__":
    main()

