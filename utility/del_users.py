import utility

def main():
    SESSION_ID = open('session.txt').read()
    l, r = [int(x) for x in input("Delete user range: ").split()]
    input("Confirm?")
    for user_id in range(l, r + 1):
        utility.do(utility.deleteUser, SESSION_ID, user_id)

if __name__ == '__main__':
    main()