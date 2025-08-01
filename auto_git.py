import os
import datetime

def auto_push():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_msg = f"Auto commit at {now}"
    os.system("git add .")
    os.system(f'git commit -m "{commit_msg}"')
    os.system("git push origin main")

if __name__ == "__main__":
    auto_push()
