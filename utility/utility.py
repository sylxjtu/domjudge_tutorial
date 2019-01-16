import requests

def addUser(session_id, teamname, username, contests = []):
    cookies = {
        'domjudge_session': session_id
    }

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Origin': 'http://oj.xjtuacm.com:12345',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'http://oj.xjtuacm.com:12345/jury/team.php?cmd=add',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    }

    data = [
        ('data[0][name]', teamname),
        ('data[0][categoryid]', '3'),
        ('data[0][members]', ''),
        ('data[0][affilid]', '2'),
        ('data[0][penalty]', '0'),
        ('data[0][room]', ''),
        ('data[0][comments]', ''),
        ('data[0][mapping][0][items]', ','.join(contests)),
        ('data[0][enabled]', '1'),
        ('data[0][adduser]', '1'),
        ('data[0][mapping][1][extra][username]', username),
        ('data[0][mapping][0][fk][0]', 'teamid'),
        ('data[0][mapping][0][fk][1]', 'cid'),
        ('data[0][mapping][0][table]', 'contestteam'),
        ('data[0][mapping][1][fk]', 'teamid'),
        ('data[0][mapping][1][table]', 'user'),
        ('cmd', 'add'),
        ('table', 'team'),
        ('referrer', ''),
    ]

    return requests.post('http://oj.xjtuacm.com:12345/jury/edit.php', headers=headers, cookies=cookies, data=data)

def deleteTeam(session_id, team_id):
    cookies = {
        'domjudge_session': session_id,
    }

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Origin': 'http://oj.xjtuacm.com:12345',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'http://oj.xjtuacm.com:12345/jury/delete.php?table=team&teamid=7&referrer=&desc=dddteam',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    }

    data = [
    ('table', 'team'),
    ('teamid', str(team_id)),
    ('confirm', ' Yes I\'m sure! '),
    ]

    return requests.post('http://oj.xjtuacm.com:12345/jury/delete.php', headers=headers, cookies=cookies, data=data)

def deleteUser(session_id, user_id):
    cookies = {
        'domjudge_session': session_id,
    }

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Origin': 'http://oj.xjtuacm.com:12345',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'http://oj.xjtuacm.com:12345/jury/delete.php?table=team&teamid=7&referrer=&desc=dddteam',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    }

    data = [
    ('table', 'user'),
    ('userid', str(user_id)),
    ('confirm', ' Yes I\'m sure! '),
    ]

    return requests.post('http://oj.xjtuacm.com:12345/jury/delete.php', headers=headers, cookies=cookies, data=data)

def do(func, *args, **kargs):
    print(func.__name__, *args, func(*args, **kargs))

def main():
    SESSION_ID = 'tc4oihnj0lehh0vh78jpkh90r4'

if __name__ == '__main__':
    main()