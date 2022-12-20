import random

# Tabla de apariencias del NPC
appearance_table = [
    "Distinctive jewelry: earrings, necklace, circlet, bracelets",
    "Piercings",
    "Flamboyant or outlandish clothes",
    "Formal, clean clothes",
    "Ragged, dirty clothes",
    "Pronounced scar",
    "Missing teeth",
    "Missing fingers",
    "Unusual eye color (or two different colors)",
    "Tattoos",
    "Birthmark",
    "Unusual skin color",
    "Bald",
    "Braided beard or hair",
    "Unusual hair color",
    "Nervous eye twitch",
    "Distinctive nose",
    "Distinctive posture (crooked or rigid)",
    "Exceptionally beautiful",
    "Exceptionally ugly"
]

# Tabla de habilidades del NPC
abilities_table = [
    ("Strength", "powerful, brawny, strong as an ox"),
    ("Strength", "feeble, scrawny"),
    ("Dexterity", "lithe, agile, graceful"),
    ("Dexterity", "clumsy, fumbling"),
    ("Constitution", "hardy, hale, healthy"),
    ("Constitution", "sickly, pale"),
    ("Intelligence", "studious, learned, inquisitive"),
    ("Intelligence", "dim-witted, slow"),
    ("Wisdom", "perceptive, spiritual, insightful"),
    ("Wisdom", "oblivious, absentminded"),
    ("Charisma", "persuasive, forceful, born leader"),
    ("Charisma", "dull, boring")
]

# Tabla de talentos del NPC
talents_table = [
    "Plays a musical instrument",
    "Speaks several languages fluently",
    "Unbelievably lucky",
    "Perfect memory",
    "Great with animals",
    "Great with children",
    "Great at solving puzzles",
    "Great at one game",
    "Great at impersonations",
    "Draws beautifully",
    "Paints beautifully",
    "Sings beautifully",
    "Expert cook",
    "Expert dancer",
    "Expert juggler",
    "Expert at sleight of hand",
    "Expert at disguise"
]

# Lista de manerismos del NPC
mannerisms_table = [
    "Prone to singing, whistling, or humming quietly",
    "Speaks in rhyme or some other peculiar way",
    "Particularly low or high voice",
    "Slurs words, lisps, or stutters",
    "Enunciates overly clearly",
    "Speaks loudly",
    "Whispers",
    "Uses flowery speech or long words",
    "Frequently uses the wrong word",
    "Uses colorful oaths and exclamations",
    "Makes constant jokes or puns",
    "Prone to predictions of doom",
    "Fidgets",
    "Squints",
    "Stares into the distance",
    "Chews something",
    "Paces",
    "Taps fingers",
    "Bites fingernails",
    "Twirls hair or tugs beard"
]

# Lista de rasgos de interacción del NPC
interaction_traits_table = [
    "Argumentative",
    "Arrogant",
    "Blustering",
    "Rude",
    "Curious",
    "Friendly",
    "Honest",
    "Hot tempered",
    "Irritable",
    "Ponderous",
    "Quiet",
    "Suspicious"
]

# NPC Bonds list
bonds_table = [
    "Dedicated to fulfilling a personal life goal",
    "Protective of close family members",
    "Protective of colleagues or compatriots",
    "Loyal to a benefactor, patron, or employer",
    "Captivated by a romantic interest",
    "Drawn to a special place",
    "Protective of a sentimental keepsake",
    "Protective of a valuable possession",
    "Out for revenge",
    "Roll twice, ignoring results of 10"
]

# NPC Flaws and Secrets list
flaws_and_secrets_table = [
    "Forbidden love or susceptibility to romance",
    "Enjoys decadent pleasures",
    "Arrogance",
    "Envies another creature's possessions or station",
    "Overpowering greed",
    "Prone to rage",
    "Has a powerful enemy",
    "Specific phobia",
    "Shameful or scandalous history",
    "Secret crime or misdeed",
    "Possession of forbidden lore",
    "Foolhardy bravery"
]


def get_npc_ideal():
    # Roll a random number between 1 and 6 to determine the type of ideal
    ideal_type = random.randint(1, 6)

    # Set the list of ideals based on the ideal type
    if ideal_type == 1:
        ideals = ["Beauty", "Charity", "Greater good",
                  "Life", "Respect", "Self-sacrifice"]
    elif ideal_type == 2:
        ideals = ["Domination", "Greed", "Might",
                  "Pain", "Retribution", "Slaughter"]
    elif ideal_type == 3:
        ideals = ["Community", "Fairness", "Honor",
                  "Logic", "Responsibility", "Tradition"]
    elif ideal_type == 4:
        ideals = ["Change", "Creativity", "Freedom",
                  "Independence", "No limits", "Whimsy"]
    elif ideal_type == 5:
        ideals = ["Balance", "Knowledge", "Live and let live",
                  "Moderation", "Neutrality", "People"]
    else:
        ideals = ["Aspiration", "Discovery", "Glory",
                  "Nation", "Redemption", "Self-knowledge"]

    # Roll a random number between 0 and 5 to determine the specific ideal
    ideal = ideals[random.randint(0, 5)]

    return ideal


class NPC:
    def __init__(self):
        self.appearance = random.choice(appearance_table)
        self.ability = random.choice(abilities_table)
        self.talent = random.choice(talents_table)
        self.mannerisms = random.choice(mannerisms_table)
        self.interaction_traits = random.choice(interaction_traits_table)
        self.bonds = random.choice(bonds_table)
        self.flaws_and_secrets = random.choice(flaws_and_secrets_table)
        self.ideal = get_npc_ideal()


# imprimimos el NPC


def main():
    npc = NPC()
    print(f"Appearance: {npc.appearance} \n Ability: {npc.ability} \n Talent: {npc.talent} \n Mannerisms: {npc.mannerisms} \n Interaction Traits: {npc.interaction_traits} \n Bonds: {npc.bonds} \n Flaws and Secrets: {npc.flaws_and_secrets} \n Ideal: {npc.ideal} \n")


# call the main function
if __name__ == "__main__":
    main()
