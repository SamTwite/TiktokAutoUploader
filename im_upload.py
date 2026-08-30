# im_upload.py — entrypoint for InternetMoney's tiktok_private adapter.
# Bypasses cli.py (which needs SQLModel + SQLite) and prints a machine-readable
# post id, which upstream never does.
import argparse, sys
from tiktok_uploader import tiktok

parser = argparse.ArgumentParser()
parser.add_argument("--user", required=True)
parser.add_argument("--video", required=True)
parser.add_argument("--title", required=True)
args = parser.parse_args()

result = tiktok.upload_video(args.user, args.video, args.title)
# `upload_video` returns bool today. Return the API's video id instead if the
# response carries one — see "Open question" below.
if not result:
    sys.exit(1)
print(f"POST_ID={result if isinstance(result, str) else 'unknown'}")