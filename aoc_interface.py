import requests
from bs4 import BeautifulSoup as soup


SESSION_COOKIE = "[REDACTED]"
RIGHT_ANSWER = "CORRECT"
WRONG_ANSWER = "INCORRECT"
ALREADY_ANSWERED = "ALREADY ANSWERED"
WAIT_TO_ANSWER = "PLEASE WAIT TO SUBMIT ANOTHER ATTEMPT"


def get_input(year, day_num):
    """HTTP GET the problem input.

    :param year:
    :param day_num:
    :return:
    """
    input_request = requests.get(
        "https://adventofcode.com/{}/day/{}/input".format(year, day_num),
        cookies={
            "session": SESSION_COOKIE
        },
    )
    return input_request.text


def post_answer(year, day_num, level, answer):
    """HTTP POST the problem output.
    Once the right answer is submitted, the URL becomes invalid

    :param year:
    :param day_num:
    :param level:
    :param answer:
    :return:
    """
    output_request = requests.post(
        "https://adventofcode.com/{}/day/{}/answer".format(year, day_num),
        cookies={
            "session": SESSION_COOKIE
        },
        data={
            "answer": answer,
            "level": level,
        }
    )
    output_soup = soup(output_request.text, "html.parser")
    output_text = output_soup.body.article.p.text
    if "not the right answer" in output_text:
        return WRONG_ANSWER
    elif "already complete it?" in output_text:
        return ALREADY_ANSWERED
    elif "answer too recently" in output_text:
        return WAIT_TO_ANSWER
    else:
        return RIGHT_ANSWER
