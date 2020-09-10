#!/usr/bin/env python3
import re
import os
import sys
import praw
import json
import sqlite3
import requests
import my_strings as ms
import helpers as h


def run():
    r = praw.Reddit(USER_AGENT)
    # Don't need to load dotenv since we don't use imgur
    # load_dotenv()  # Used for imgur auth

    # TODO: verify that the db path is valid.
    #   A single file is fine but dirs are not created if they don't exist
    print("Looking for comments...")
    for comment in r.subreddit(SUBREDDIT_NAME).stream.comments():
        if check_batsignal(comment.body) and not check_has_responded(comment):
            print("-------------------------------------------------")
            tokens = h.get_and_split_first_line(comment.body)

            # For now just taking the 2nd token. First should be the batsignal
            command = tokens[1]
            response = ms.COMMANDS_MAP.get(command, ms.HELP_TEXT)
            db_obj = h.reply_and_upvote(comment, response=response, respond=RESPOND)
            add_comment_to_db(db_obj)


def check_batsignal(comment_body):
    """
    Returns True if the comment body starts with the batsignal "!mfaimagebot". Otherwise False.
    Case insensitive.

    >>> check_batsignal("!QuickLink test")
    True
    >>> check_batsignal("!quicklink test")
    True
    >>> check_batsignal("!QuIcKlInK test")
    True
    >>> check_batsignal("!QuickLink")
    True
    >>> check_batsignal(" !QuickLink test")
    False
    >>> check_batsignal("!Test test")
    False
    >>> check_batsignal("?QuickLink test")
    False
    """
    text = comment_body.lower()
    return text.startswith(ms.BATSIGNAL)


def check_has_responded(comment):
    """
    Returns True if the comment hash is in the database and we've already responded to it. Otherwise False.

    fetchone() is not None --> a row exists
    a row exists iff hash is in DB AND we have responded to it.
    """
    # TODONE: Using 0 (false) for has_responded will probably be a better query
    #       since the DB should really only keep comments we have responded to
    # UPDATE: We keep all comments in the DB, but update the value if responded.
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("SELECT * FROM comments WHERE comment_hash=:hash AND has_responded=1", {"hash": comment.id})
    val = (cur.fetchone() is not None)
    conn.close()
    return val


def add_comment_to_db(db_dict):
    """
    Adds the comment and its info to the database
    """
    # print(f"Hash: {db_dict["hash"]}")
    print(f"Has responded: {db_dict["has_responded"]}")
    print(f"Response text: ")
    print(f"{db_dict["response_text"]}")
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    # https://stackoverflow.com/questions/19337029/insert-if-not-exists-statement-in-sqlite
    cur.execute("INSERT OR REPLACE INTO comments VALUES (:hash, :has_responded, :response_text)", db_dict)
    conn.commit()
    conn.close()


def db_setup(db_file):
    print("Setting up DB...")
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS comments (
        comment_hash  TEXT       NOT NULL  UNIQUE,
        has_responded INTEGER    DEFAULT 0,
        response_text TEXT       DEFAULT NULL,
        CHECK(has_responded = 0 OR has_responded = 1)
    )""")
    conn.commit()
    conn.close()
    print("Done!")


if __name__ == "__main__":
    env = sys.argv[1]
    USER_AGENT = ""
    DB_FILE = ""
    SUBREDDIT_NAME = ""
    RESPOND = False
    print(f"Running bot in env: {env}")

    if env == "test":
        USER_AGENT = "MFAQuickLinksTest"
        DB_FILE = "test.db"
        SUBREDDIT_NAME = "mybottestenvironment"
        RESPOND = False
    elif env == "prod":
        USER_AGENT = ms.USER_AGENT
        DB_FILE = ms.DB_FILE
        SUBREDDIT_NAME = ms.SUBREDDIT_NAME
        RESPOND = True
    else:
        print("Not a valid environment: test or prod.")
        print("Exiting...")
        sys.exit()
    # file-scope vars are set above
    print(f"User agent: {USER_AGENT}")
    print(f"DB file: {DB_FILE}")
    print(f"Subreddit name: {SUBREDDIT_NAME}")
    print(f"Respond: {RESPOND}")
    print("~~~~~~~~~~")
    db_setup(DB_FILE)  # TODO: set db file path as CLI parameter
    run()
