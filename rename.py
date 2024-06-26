from subprocess import run

proc = run(['ls', 'images'], capture_output=True)
filenames = sorted(proc.stdout.decode().split())
for i, name in enumerate(filenames):
    if i < 10:
        run(['mv', "images/" + name,  "0" + str(i) + ".jpg"])
    else:
        run(['mv', "images/" + name,  str(i) + ".jpg"])
 