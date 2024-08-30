import requests
import hashlib
import sys

def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching data: {res.status_code}')
    return res

def get_pass_leak_count(hashes, hash_to_test):
    hashes = (line.split(':') for line in hashes.splitlines())
    for h, count in hashes:
        if h == hash_to_test:
            return count
    return 0  # Move this outside the loop to only return 0 if no match is found

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)

    # Extract the text content from the response
    response_text = response.text

    return get_pass_leak_count(response_text, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'Password was found {count} times! You should consider changing it.')
        else:
            print(f'Password was not found: {password}')
    return 'done'

main(sys.argv[1:])
print(main(sys.argv[1:]))
