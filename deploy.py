import os

os.system("gitbook build")
os.system("git add -A")
os.system("git commit -m \"update\"")
os.system("git push")