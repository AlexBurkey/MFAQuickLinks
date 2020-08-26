USER_AGENT = 'MFAQuickLinks'
BATSIGNAL = '!MFAQuickLink'

DB_FILE = 'mfaql.db'
SUBREDDIT_NAME = "malefashionadvice"

TODO_TEXT = "Sorry, this function has not been implemented yet.\n\n"
HELP_TEXT = (f"Usage: I respond to comments starting with `{BATSIGNAL}` (case insensitive).  \n"
             f"`{BATSIGNAL} help`: Print this help message.  \n"
             f"`{BATSIGNAL} faq`: links to the MFA FAQ  \n"
             f"`{BATSIGNAL} bb`: links to The Basic Bastard guides  \n"
             f"`{BATSIGNAL} acronyms`: links to the glossary/acronym list  \n"
             )
FAQ_TEXT = ("The /r/malefashionadvice FAQ:  \n"
            "https://www.reddit.com/r/malefashionadvice/wiki/faq"
        )
BB_TEXT = TODO_TEXT

COMMANDS_MAP = {
        'help': HELP_TEXT,
        'faq': FAQ_TEXT,
        'bb': BB_TEXT
}

TAIL = ("\n\n---\nI am a bot! If you've found a bug you can open an issue "
        "[here.](https://github.com/AlexBurkey/MFAImageBot/issues/new?template=bug_report.md)  \n"
        "If you have an idea for a feature, you can submit the idea "
        "[here](https://github.com/AlexBurkey/MFAImageBot/issues/new?template=feature_request.md)  \n"
        "Version 1.2")