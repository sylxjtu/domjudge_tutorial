import utility

def main():
    SESSION_ID = open('session.txt').read()
    l, r = [int(x) for x in input("Delete team range: ").split()]
    input("Confirm?")
    for team_id in range(l, r + 1):
        utility.do(utility.deleteTeam, SESSION_ID, team_id)

if __name__ == '__main__':
    main()