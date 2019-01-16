import utility

def main():
    SESSION_ID = open('session.txt').read()
    l, r = [int(x) for x in input("Add user range: ").split()]
    contests = input("Add to contest: ").split()
    name_list_path = input("Name list file path: ").strip()

    name_list = []
    if name_list_path != '':
        print("Name List is: ")
        name_list = [name.strip() for name in open(name_list_path, encoding="utf-8")]
        print(', '.join(name_list))

    input("Confirm?")

    for i in range(l, r + 1):
        username = "team%03d" % i
        teamname = name_list[i - l] if len(name_list) > i - l else username
        utility.do(utility.addUser, SESSION_ID, teamname, username, contests)

if __name__ == '__main__':
    main()