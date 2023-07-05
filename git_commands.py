import subprocess

# subprocess.run("git status")
subprocess.run("git add --all")
subprocess.run('git commit -m "commit from mac"')
subprocess.run("git push cal_github main")