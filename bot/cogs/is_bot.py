import re


def is_bot(user):
    """Checks if user is likely a spambot"""

    # Will eventually be a score based on similarities to other spambots
    isbot = False

    spambot_re = re.compile(r"^[A-Z]{1}.*[0-9]{1}$")
    if spambot_re.match(user.name):
        isbot = True

    # For now, assume that all users being tested are bots
    return isbot
