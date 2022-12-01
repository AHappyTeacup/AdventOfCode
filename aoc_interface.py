import re
import sys
import requests
from bs4 import BeautifulSoup as soup


SESSION_COOKIE = "[REDACTED]"
RIGHT_ANSWER = "CORRECT"
WRONG_ANSWER = "INCORRECT"
ALREADY_ANSWERED = "ALREADY ANSWERED"
WAIT_TO_ANSWER = "PLEASE WAIT TO SUBMIT ANOTHER ATTEMPT"


def get_year_and_day():
    """"""
    invoking_script = sys.modules["__main__"]

    invoking_script_path = invoking_script.__file__
    file_path_regex = re.compile(r"/(?P<year>\d+)/day_(?P<day>\d+).py$")
    script_path_match = file_path_regex.search(invoking_script_path)
    year = int(script_path_match.group("year"))
    day = int(script_path_match.group("day"))

    return year, day


def get_input():
    """HTTP GET the problem input.

    :return:
    """
    year, day = get_year_and_day()
    input_request = requests.get(
        "https://adventofcode.com/{}/day/{}/input".format(year, day),
        cookies={
            "session": SESSION_COOKIE
        },
    )
    return input_request.text


def post_answer(level, answer):
    """HTTP POST the problem output.
    Once the right answer is submitted, the URL becomes invalid

    :param level:
    :param answer:
    :return:
    """
    year, day = get_year_and_day()

    problem_url = "https://adventofcode.com/{}/day/{}".format(year, day)

    answer_request = requests.post(
        problem_url + "/answer",
        cookies={
            "session": SESSION_COOKIE
        },
        data={
            "answer": answer,
            "level": level,
        }
    )
    answer_soup = soup(answer_request.text, "html.parser")
    answer_text = answer_soup.body.article.p.text

    if "not the right answer" in answer_text:
        return answer_text
    elif "already complete it?" in answer_text:
        # The base page should display the answers.
        problem_request = requests.get(problem_url, cookies={"session": SESSION_COOKIE})
        problem_soup = soup(problem_request.text, "html.parser")
        answers = [p.code.text for p in problem_soup.main.find_all("p") if "Your puzzle answer was" in p.text]
        if str(answer) != answers[level-1]:
            return WRONG_ANSWER
        else:
            return RIGHT_ANSWER
    elif "answer too recently" in answer_text:
        return WAIT_TO_ANSWER
    else:
        return RIGHT_ANSWER
