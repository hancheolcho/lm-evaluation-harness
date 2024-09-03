




def doc_to_text(doc: dict) -> str:
    """MMLU format doc_to_text function for ARC task.

    The following is an example:

    Given the following question and four candidate answers (A, B, C and D), choose the best answer.
    An astronomer observes that a planet rotates faster after a meteorite impact. Which is the most likely effect of this increase in rotation?
    A. Planetary density will decrease.
    B. Planetary years will become longer.
    C. Planetary days will become shorter.
    D. Planetary gravity will become stronger.
    Your response should end with "The best answer is [the_answer_letter]" where the [the_answer_letter] is one of A, B, C or D.
    """
    text = "Given the following question and four candidate answers ("
    text += ", ".join(doc["choices"]["label"][:-1]) + " and " + doc["choices"]["label"][-1]
    text += "), choose the best answer.\n"
    text += doc["question"].strip() + "\n"

    for i in range(len(doc["choices"]["text"])):
        text += doc["choices"]["label"][i] + ". " + doc["choices"]["text"][i] + "\n"
    text += "\n"

    text += "Your response should end with \"The best answer is [the_answer_letter]\" where the [the_answer_letter] is one of "
    text += ", ".join(doc["choices"]["label"][:-1]) + " or " + doc["choices"]["label"][-1] + "."

    return text
