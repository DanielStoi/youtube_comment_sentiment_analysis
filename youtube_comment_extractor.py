#!/usr/bin/env python3


"""
credit goes to github user nickjj for writing essentially essentially all of the
code within this file.

The code was adapted to provide the comments instead of just the username of the users


'textDisplay' is the response
'totalReplyCount' returns integer
"""
import argparse
import json
import os
import random
import sys
import textwrap

from itertools import chain
from urllib.request import urlopen
from urllib.parse import urlencode



def extract_youtube_id(url):
    if len(url) == 11:
        return url

    location = url.find("?v=")
    if location == -1:
        print("CANNOT EXTRACT VIDEO")
        return False
    
    url = url[location+3:]
    if len(url)<11:
        print("INVALID ID")
        return False
    url = url[:11]
    return url


def get_api_key():
    try:
        return os.environ['YOUTUBE_API_KEY']
            
    except KeyError:
        return input("enter an API key for google: ")
        msg = '''You must create and export a YOUTUBE_API_KEY, instructions:

    1. Go-to https://console.developers.google.com/apis/credentials
    2. Create credentials with an "API Key" type
    3. export YOUTUBE_API_KEY=<your key goes here>'''
        print(msg)
        sys.exit(1)


def check_youtube_video_id(str):
    str = str.strip()

    # This is a bit naive but it should be good enough to protect against
    # accidentally pasting in the wrong value.
    if len(str) == 11:
        return str
    else:
        msg = f'not a valid YouTube video id: "{str}"'
        raise argparse.ArgumentTypeError(msg)


def check_positive_int(val):
    int_val = int(val)

    if int_val >= 0:
        return int_val
    else:
        msg = f'must be a positive integer: "{val}"'
        raise argparse.ArgumentTypeError(msg)


def check_omit_authors(omit_authors):
    if omit_authors == '':
        return []

    return list(map(str.strip, omit_authors.split(',')))


def display_names(results, is_verbose):
    authors = []

    for item in results['items']:
        comment = item['snippet']['topLevelComment']['snippet']
        author = comment['authorDisplayName']
        text = comment['textDisplay']
        authors.append([author,text])

        if is_verbose:
            print(f'  {author}')

    return authors


def progress(page_count):
    if page_count > 1:
        print('')

    print(f'Getting comments for page {page_count}...')

    return page_count + 1


def get_comments(api_params):
    api_endpoint = 'https://www.googleapis.com/youtube/v3/commentThreads'
    encoded_params = urlencode(api_params)

    with urlopen(f'{api_endpoint}?{encoded_params}') as response:
        return json.load(response)


def get_all_comments(api_token, video_id, is_verbose):
    authors = []
    page_count = 1

    api_params = {
        'key': api_token,
        'part': 'snippet',
        'videoId': video_id,
        'maxResults': 100,
    }

    results = get_comments(api_params)
    page_count = progress(page_count)
    authors.append(display_names(results, is_verbose))

    next_page_token = results.get('nextPageToken')

    while next_page_token:
        page_count = progress(page_count)

        api_params['pageToken'] = next_page_token
        results = get_comments(api_params)
        authors.append(display_names(results, is_verbose))

        next_page_token = results.get('nextPageToken')

    return authors


def flatten_list(items):
    return list(chain.from_iterable(items))


def sorted_unique_list(items):
    return sorted(list(set(items)))


def remove_authors(items, skip_items):
    #  This could be rewritten as a list comprehension such as:
    #   return [item.strip() for item in items if item not in skip_items]
    #
    # But IMO this approach is much more readable.
    for item in skip_items:
        if item.strip() in items:
            items.remove(item)

    return items


def pick_winners(authors, authors_count, winner_count):
    # We can't pick more winners than we have in total.
    if winner_count > authors_count:
        winner_count = authors_count

    return (random.sample(authors, winner_count), winner_count)


def parseargs():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
        Get a list of top level comments from a YouTube video and then
        pick N amount of unique comment authors by choosing them randomly.
        '''))

    parser.add_argument('video_id', default=None,
                        metavar='VIDEO_ID', type=check_youtube_video_id,
                        help='the 11 characters after ?v= in a YouTube URL')

    parser.add_argument('--winners', default=10, type=check_positive_int,
                        metavar='WINNERS',
                        help='number of winners to pick (defaults to 10)')

    parser.add_argument('--omit-authors', default='', type=check_omit_authors,
                        metavar='OMIT_AUTHORS',
                        help='comma separated list of author names to omit')

    parser.add_argument('--verbose', default=False, type=bool, nargs='?',
                        const=True, metavar='BOOL',
                        help='output author display names during the progress')

    return parser.parse_args()


def generate_report(winners, winner_count, authors_count,
                    duplicate_authors_count, omit_authors_count,
                    authors_final_count):
    winners = '\n  '.join(winners)

    print(f'''
{authors_count} top level comments were returned
- {duplicate_authors_count} comment(s) had duplicate authors
- {omit_authors_count} comment authors were explicitly omit
= {authors_final_count} comment authors have a chance to win

Winners ({winner_count}):
  {winners}''')

    return None


def cmd_request_everything():
    v = input("Video Id")
    comments = get_all_comments(get_api_key(), vid_id, is_verbose=False)
    return comments
    
    

if __name__ == '__main__':
    #args = parseargs()
    
    #omit_authors_count = len(args.omit_authors)
    
    #comments = get_comments(get_api_key(), args.video_id, args.verbose)
    vid_id = "QzxmWzHtimA"
    comments = get_all_comments(get_api_key(), vid_id, is_verbose=False)
    comments = flatten_list(comments)
    authors_count = len(comments)
    

    for i in comments:
        print(i)



