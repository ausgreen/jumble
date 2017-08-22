import enchant
from itertools import permutations
import click


@click.command()
@click.argument('jumbles', nargs=-1)
def jumble(jumbles):
    # Solves
    click.echo([_solve_jumble(puzzle) for puzzle in jumbles])


def _solve_jumble(jumble):
    pmuts = [''.join(combo) for combo in permutations(jumble)]
    dictionary = enchant.Dict("en_us")
    words = [word for word in pmuts if dictionary.check(word)]
    return(words)


if __name__ == "__main__":
    jumble()