import sys

from pass_lib import passme_hash, passme_password, passme_file, passme_list

full_cmd_arguments = sys.argv
argument_list = full_cmd_arguments[1:]


def main():
    engine = check_engine(argument_list)
    api_key = check_api(argument_list)
    if len(argument_list) >= 2 or "--help" in argument_list:
        if argument_list[0] == "-h" or argument_list[0] == "--hash":
            passme_hash(argument_list[1], engine=engine, api_key=api_key)
        elif argument_list[0] == "-p" or argument_list[0] == "--password":
            passme_password(argument_list[1], engine=engine, api_key=api_key)
        elif argument_list[0] == "-f" or argument_list[0] == "--file":
            passme_file(argument_list[1], engine=engine, api_key=api_key)
        elif argument_list[0] == "-l" or argument_list[0] == "--list":
            passme_list(argument_list[1], engine=engine, api_key=api_key)
        elif argument_list[0] == "--help":
            print_help()
        else:
            print("Seems that the arguments are malformed, check --help for a hint")
    else:
        print("ERROR")


def check_engine(arlist):
    if "-engine" in arlist:
        try:
            return arlist[3]
        except IndexError:
            print("Seems that the arguments are malformed, defaulting engine to HIBP")
            return "HIBP"
    else:
        return "HIBP"


def check_api(arlist):
    if "-api_key" in arlist:
        try:
            return arlist[5]
        except IndexError:
            print("Seems that the arguments are malformed, defaulting api_key to 0")
            return "0"
    else:
        return "0"


def print_help():
    print("""
    NAME
        passme -- Check if your data has been leaked online

    USAGE
        passme [FUNC] [ELEMENT] -engine [ENGINE] -api_key [API_KEY]

    DESCRIPTION
        FUNC:       The kind of element tha you want to check, it can be -h/--hash or -p/--password
                    or -f/--file or -l/--list or --help.

        ELEMENT:    The "Hash", "Password" or the name of the file that contains a list of
                    hashes or password separeted by a new line.

        ENGINE:     The leaks engine that you want to be used, by default it uses HIBP (Have I been PWN).

        API_KEY:    The API_KEY necessary for some functions of some engines.
    """)


if __name__ == "__main__":
    main()
