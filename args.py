import argparse

def setup_args():
    parser = argparse.ArgumentParser(description='anger zip brute force decode.')

    parser.add_argument('-a', action='store_true', help='add lower case(a-z) letter to password.')
    parser.add_argument('-A', action='store_true', help='add upper case(A-Z) letter to password..')
    parser.add_argument('-n', action='store_true', help='add numeric(0-9) to password..')
    parser.add_argument('-N', action='store', required=True, help='total word nums of the password. ')
    parser.add_argument('--spec', action='store', help='add special words to password..')
    parser.add_argument('--filepath', action='store', required=True, help='zip file path. ')

    return parser.parse_args()

if __name__ == "__main__":
    print(setup_args())
