""" JUMBLE
    BY: ADG
    Solves jumbles using brute force.  This solution is >O(n!), so long
    jumbles will take ages.
    """
import enchant
from itertools import permutations
import click


@click.command()
@click.argument('jumbles', nargs=-1)
def jumble(jumbles):
    click.echo("\n--JUMBLE V0.1 by ADG--")
    if len(jumbles) > 0:
        for jumble in jumbles:
            if not jumble.isalpha():
                click.echo("E - Jumbles should only have alphabetic characters!")
                return

        # Solves jumbles
        solutions = [_solve_jumble(puzzle) for puzzle in jumbles]
        for i, sol in enumerate(solutions):
            click.echo("  {} ----> {}".format(jumbles[i], solutions[i]))

    else:
        click.echo("E - Please provide some jumbles for me to solve")


def _solve_jumble(jumble):
    ''' Brute force some jumbles
    '''
    pmuts = [''.join(combo) for combo in permutations(jumble)]
    dictionary = enchant.Dict("en_us")
    words = [word for word in pmuts if dictionary.check(word)]
    if len(words):
        return(words[0])
    else:
        return("No Matches Found")


if __name__ == "__main__":
    jumble()