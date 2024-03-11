import random


def roll_d6():
    return random.randint(1, 6)


def roll_d8():
    return random.randint(1, 8)


damage_types = {1: "Acid", 2: "Cold", 3: "Fire", 4: "Force",
                5: "Lightning", 6: "Poison", 7: "Psychic", 8: "Thunder"}


def chaos_bolt():
    damage = []

    # Initial damage roll
    damage.append(roll_d6())

    # Determine the type of damage using one of the d8 rolls
    damage_die = roll_d8()
    damage_type = damage_types[damage_die]
    damage.append(damage_die)
    # print(damage_type)

    # Add the second damage roll (2d8) to the total damage
    damage.append(roll_d8())

    energy_leaps = False
    # If the two damage rolls are the same, roll additional damage
    if damage[1] == damage[2]:
        energy_leaps = True

    # Display the results
    # print(f"Initial damage: {initial_damage}")
    print(f"Damage type: {damage_type}")
    print(f"Total damage: {sum(damage)}")
    print(f"Individual damage rolls: {damage}")

    if energy_leaps:
        print("Your energy leaped! Roll again.")


if __name__ == "__main__":
    print("Simulating Chaos Bolt damage...")
    chaos_bolt()
