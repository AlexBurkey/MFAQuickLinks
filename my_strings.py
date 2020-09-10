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

BB_TEXT = ("The /r/malefashionadvide Basic Bastard Guides:  \n"
            "https://www.reddit.com/r/malefashionadvice/wiki/guides#wiki_basic_bastard")

ACRONYMS_TEXT = ("The /r/malefashionadvice acronyms guide:  \n"
                "https://www.reddit.com/r/malefashionadvice/wiki/glossary")

ITEMS_TEXT = ("The /r/malefashionadvice Your Favorite ___ for $___ mega threads:  \n"
            "https://www.reddit.com/r/malefashionadvice/wiki/itemguides#wiki_item_suggestions_at_each_price_point")

COMMANDS_MAP = {
        'help': HELP_TEXT,
        'faq': FAQ_TEXT,
        'bb': BB_TEXT,
        'acronyms': ACRONYMS_TEXT,
        'items': ITEMS_TEXT
}

TAIL = ("\n\n---\nI am a bot! If you've found a bug you can open an issue "
        "[here.](https://github.com/AlexBurkey/MFAImageBot/issues/new?template=bug_report.md)  \n"
        "If you have an idea for a feature, you can submit the idea "
        "[here](https://github.com/AlexBurkey/MFAImageBot/issues/new?template=feature_request.md)  \n"
        "Version 1.2")