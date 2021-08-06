import re


def is_bot(user):
    """Checks if user is likely a spambot"""

    # Will eventually be a score based on similarities to other spambots
    isbot = True

    # Matches the auto-generated names of spambots we get
    spambot_re = re.compile(r"^[A-Z]{1}.*[0-9]{1}$")
    if not spambot_re.match(user.name):
        isbot = False

    # Spambots don't change their avatars
    if user.avatar_url != user.default_avatar_url:
        isbot = False

    # Spambots don't change their nicknames
    if user.nick != user.name:
        isbot = False

    return isbot
