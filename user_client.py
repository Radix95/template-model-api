import argparse
import os
import requests
from dotenv import load_dotenv

load_dotenv()


def create_user(name_, email_, password_):

    key = os.environ["CREATE_USER_KEY"]

    my_headers = {'MDIuser' : key}

    response = requests.post('http://localhost:8000/user', json = {'name': name_, 'email': email_, 'password': password_}, headers=my_headers)

    print(response.status_code)


def show_user():
    key = os.environ["CREATE_USER_KEY"]

    my_headers = {'MDIuser' : key}

    response = requests.get('http://localhost:8000/user', headers=my_headers)

    print(response.content)


def delete_user(id):
    key = os.environ["CREATE_USER_KEY"]

    my_headers = {'MDIuser' : key}

    response = requests.delete(f'http://localhost:8000/user/{id}', headers=my_headers)

    print(response.content)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    # group = parser.add_mutually_exclusive_group()

    # group.add_argument("-c", "--create", action="store_true")
    # group.add_argument("-s", "--show", action="store_true")
    # group.add_argument("-d", "--delete", action="store_true")

    subparser = parser.add_subparsers(dest='command')
    create_u = subparser.add_parser('create')
    show_u = subparser.add_parser('show')
    delete_u = subparser.add_parser('delete')

    create_u.add_argument('--name', type=str, required=True)
    create_u.add_argument('--email', type=str, required=True)
    create_u.add_argument('--password', type=str, required=True)

    delete_u.add_argument('--id', type=str, required=True)


    args = parser.parse_args()

    if args.command == "create":
        name_ = args.name
        email_ = args.email
        password_ = args.password

        create_user(name_, email_, password_)

    elif args.command == "show":

        show_user()

    elif args.command == "delete":
        id = args.id

        delete_user(id)