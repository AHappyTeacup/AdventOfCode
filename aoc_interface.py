import requests


def get_input(year, day_num):
    input_request = requests.get(
        "https://adventofcode.com/{}/day/{}/input".format(year, day_num),
        cookies={
            "session": "[REDACTED]"
        },
    )
    return input_request.text
