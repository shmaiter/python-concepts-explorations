import random

"""_summary_
Write a program that generates poetry using lists and the random module.
Whith the following structure inspired by Clifford Pickover:

{A/An} {adj1} {noun1}
{A/An} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
{adverb1}, the {noun1} {verb2}
the {noun2} {verb3} {prep2} a {adj3} {noun3}
"""

nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]
vocals = "aeiou"


def make_poem():
    # s1 = set(random.choice(lst))
    # while len(s1) < num:
    #     temp = random.choice(lst)
    #     while temp in s1:
    #         print(f"repeated: {temp}")
    #         temp = random.choice(lst)
    #     s1.add(temp)

    # return s1
    
    adj1 = random.choice(adjectives)
    adjectives.remove(adj1)
    adj2 = random.choice(adjectives)
    adjectives.remove(adj2)
    adj3 = random.choice(adjectives)
    adjectives.remove(adj3)

    noun1 = random.choice(nouns)
    nouns.remove(noun1)
    noun2 = random.choice(nouns)
    nouns.remove(noun2)
    noun3 = random.choice(nouns)
    nouns.remove(noun3)
    verb1 = random.choice(verbs)
    verbs.remove(verb1)
    verb2 = random.choice(verbs)
    verbs.remove(verb2)
    verb3 = random.choice(verbs)
    verbs.remove(verb3)
    prep1 = random.choice(prepositions)
    prepositions.remove(prep1)
    prep2 = random.choice(prepositions)
    prepositions.remove(prep2)
    adverb1 = random.choice(adverbs)

    article = "An" if adj1[0] in vocals else "A"

    print(
        f"""
        {article} {adj1} {noun1}
        {article} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
        {adverb1}, the {noun1} {verb2}
        the {noun2} {verb3} {prep2} a {adj3} {noun3}
        """
    )


if __name__ == "__main__":
    make_poem()
