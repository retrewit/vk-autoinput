try:
    import vk_api
    import argparse
    import requests
    from time import sleep
except ModuleNotFoundError:
    print("ENTER: pip3 install -r requirements.txt")
    exit()

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--token", type=str, default="",
                    help="VK Token", dest="token")
parser.add_argument("-n", "--type", type=int, choices=[1, 2], default=1,
                    help="1 - typing, 2 - audiomessage", dest="types")
parser.add_argument("user", type=str, default="",
                    help="VK User")
args = parser.parse_args()

try:
    if args.token != "":
        token = args.token
        with open("token.txt", "w") as file:
            file.write(token)
    else:
        with open("token.txt", "r") as file:
            token = file.read()
    user = args.user
    types = "typing" if args.types == 1 else "audiomessage"
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    if not user.isdigit():
        user = vk.users.get(user_ids=user)[0]["id"]
        print("Digital ID:", user)
    while True:
        vk.messages.setActivity(type=types, peer_id=user)
        sleep(3)
except FileNotFoundError:
    print("ENTER THE TOKEN: python3 main.py [--token TOKEN] user")
except requests.exceptions.ConnectionError:
    print("NO INTERNET")
except vk_api.exceptions.ApiError:
    print("INVALID TOKEN")
except KeyboardInterrupt:
    print("END")
