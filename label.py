from subprocess import run
import cv2

coords = []
all_vals = []

def on_click(*event):
    if event[0] == 1:
        coords.append(str(event[1]))
        coords.append(str(event[2]))

proc = run(['ls', 'images'], capture_output=True)
filenames = sorted(proc.stdout.decode().split())

with open('data.txt', 'r') as fin:
    lines = fin.readlines()

for name in filenames:
    for line in lines:
        if name in line:
            print(line)    
    img = cv2.imread("images/" + name)
    coords.append(name)
    cv2.imshow(f"{name}", img)
    cv2.setMouseCallback(f"{name}", on_click)
    # key will be 48+digit for digit characters 1-9
    key = cv2.waitKey(0)
    if key == 49:
        coords.append('1')
    elif key == 50:
        coords.append('2')
    if len(coords) == 6:
        all_vals.append(coords)
    elif len(coords) > 1:
        print(name, key - 48)
    coords = []
    break

with open('test.txt', 'a') as fout:
    for val in all_vals:
        print(" ".join(val), file=fout)