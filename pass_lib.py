import requests
import hashlib


def passme_password(password, engine="HIBP", api_key="0"):
    encoded_password = hashlib.sha1(str.encode(password)).hexdigest()
    passme_hash(encoded_password, engine, api_key)


def passme_hash(hashed_password, engine="HIBP", api_key="0"):
    if engine == "HIBP":
        engine_HIBP(hashed_password, engine, api_key)
    elif engine == "BD":
        print("DataBreach")
    else:
        print("Engine not implemented, defaulting to HIBP.")
        passme_hash(hashed_password, engine="HIBP", api_key=api_key)


def passme_file(filename, engine="HIBP", api_key="0"):
    with open(filename) as file_in:
        for line in file_in:
            line = line.rstrip("\n")
            print("Password: " + line)
            passme_password(line, engine, api_key)
            print("")


def passme_list(filename, engine="HIBP", api_key="0"):
    with open(filename) as file_in:
        for line in file_in:
            passme_hash(line, engine, api_key)
            print("Hash: " + line)


def engine_HIBP(hashed_password, engine, api_key):
    word_count = len(hashed_password)
    if word_count >= 5:
        hashed = hashed_password[5:35].upper()
        response = requests.get("https://api.pwnedpasswords.com/range/"
                                + hashed_password[0:5],
                                headers={'Add-Padding': 'true', 'hibp-api-key': api_key})
        if hashed in response.text:
            print("It is possible that your password has been filtered.")
        else:
            print("Your password has not been filtered yet.")
    else:
        print("Invalid Hash, please use a prefix of at least 5 characters.")
