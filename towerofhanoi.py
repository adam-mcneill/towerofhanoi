"""Tower of Hanoi - A puzzle game where a tower made up of disks has to be
moved from place to place, one disk at a time."""

import sys

TOWER_SIZE = 5  # This can be changed to alter the difficulty level
COMPLETED_TOWER = list(range(TOWER_SIZE, 0, -1))
towers = {"A": COMPLETED_TOWER[:], "B": [], "C": []}

def main():
    """Main loop function. Runs a single game, then exits."""
    
    print("""Welcome to the Tower of Hanoi. Move a disk by entering the
tower to take it from and to. For example, AB to move from tower A
to tower B. Bigger disks may not be placed on top of smaller ones.""")
    print()

    while True:  # Main loop. Runs a single game, then exits.
        drawTowers(towers)
        
        fromTower, toTower = takeInput(towers)

        moveDisks(towers, fromTower, toTower)


def takeInput(towers):
    """Takes an input from the user, validates it and returns the
towers specified. Exits if QUIT is entered."""
    
    while True:  # Keep looping until a valid move is entered
        print("""Please enter a move, or QUIT to exit.""")
        response = input('> ').upper().strip()

        if response == 'QUIT':
            print('Thanks for playing.')
            sys.exit()
        elif response not in ("AB", "AC", "BA", "BC", "CA", "CB"):
            print("That isn't a valid move. Please try again.")
            continue

        fromTower = response[0]
        toTower = response[1]
        
        if len(towers[fromTower]) == 0:
            # Trying to take from an empty tower.
            print('The tower you are taking from is empty.')
            continue
        elif len(towers[toTower]) == 0:
            # Moving to an empty tower is always valid.
            return fromTower, toTower
        elif towers[fromTower][-1] > towers[toTower][-1]:
            # Trying to put a big disk on a small one.
            print("You can't put a larger disk on top of a smaller one")
            continue
        else:
            # All other moves are valid.
            return fromTower, toTower


def moveDisks(towers, fromTower, toTower):
    """Moves the top disk from a specified tower to another. Also
checks if the puzzle has been completed."""

    # Add the disk to the new tower and remove it from the old one
    towers[toTower].append(towers[fromTower][-1])
    towers[fromTower].pop()

    if COMPLETED_TOWER in (towers['B'], towers['C']):
        # Draw the completed puzzle:
        drawTowers(towers)
        print('You have solved the puzzle. Congratulations!')
        sys.exit()


def drawTowers(towers):
    """Draws the three towers on screen by calling drawLevel one
storey at a time."""

    # Draw each storey, starting at the top.
    # Start one level above a completed tower for clarity:
    for level in range(TOWER_SIZE + 1, 0, -1):
        drawLevel(towers, level)

    # Draw the tower labels:
    spaceBuffer = " " * TOWER_SIZE
    print(spaceBuffer, ' A', spaceBuffer,
          spaceBuffer, ' B', spaceBuffer,
          spaceBuffer, ' C', sep='')
    print()


def drawLevel(towers, levelToDraw):
    """Draws a single storey of each of the three towers."""
    
    for tower in ("A", "B", "C"):
        # Find the disk width. Use zero if there is no disk there:
        if len(towers[tower]) < levelToDraw:
            diskWidth = 0
        else:
            diskWidth = towers[tower][levelToDraw - 1]

        # Build a blank space string to display between towers:
        spaceBuffer = " " * (TOWER_SIZE - diskWidth)

        # Build the tower section string:
        if diskWidth == 0:
            towerSection = "||"
        else:
            towerSection = "@" * diskWidth + \
                           str(diskWidth).rjust(2, "_") + \
                           "@" * diskWidth

        # Draw the tower section with buffers on either side:
        print(spaceBuffer, towerSection, spaceBuffer, sep='', end='')
    print()

# Run main() if the program was run, as opposed to imported.
if __name__ == '__main__':
    main()
