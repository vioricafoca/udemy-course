import requests
import hashlib


def check_pwd(query):
    url = 'https://api.pwnedpasswords.com/range/' + query
    res = requests.get(url)
    if res.status_code != 200:
        print('Wrong URL or request failed')
        return None
    return res.text


def check_api(password):
    # Create a new sha1 hash object (Pwned Passwords API requires SHA-1, not SHA-256)
    sha1_hash = hashlib.sha1()
    sha1_hash.update(password.encode('utf-8'))

    # Get the hexadecimal digest of the hash
    hashed_password = sha1_hash.hexdigest().upper()

    # Send only the first 5 characters of the hash to the API
    prefix = hashed_password[:5]
    suffix = hashed_password[5:]

    # Check the pwned passwords database
    response = check_pwd(prefix)
    if response:
        # Check if the hash suffix is in the returned result
        for line in response.splitlines():
            hash_suffix, count = line.split(':')
            if hash_suffix == suffix:
                print(f'Password {hash_suffix} found {count} times in pwned database!')
                return True
        print('Password not found in pwned database.')
    return False


# Example usage
check_api('123')
