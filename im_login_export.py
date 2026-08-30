# im_login_export.py — logs in via the fork's own login(), then exports the
# resulting session as JSON (stdout or --out), matching the format
# publisher/cookies.py and publisher/push_session.py expect.
import argparse, json, sys
from tiktok_uploader.tiktok import login
from tiktok_uploader.cookies import load_cookies_from_file

parser = argparse.ArgumentParser()
parser.add_argument("--account", required=True)
parser.add_argument("--out", default=None)
args = parser.parse_args()

login(args.account)  # opens a real Chrome window; a human completes login/2FA/captcha
cookies = load_cookies_from_file(f"tiktok_session-{args.account}")
if not cookies:
    sys.exit("login did not produce a session — check the Chrome window for what happened")

payload = json.dumps(cookies, default=str)
if args.out:
    open(args.out, "w").write(payload)
else:
    print(payload)
