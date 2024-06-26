"""
Goal is to figure out which images have both dogs, one dog, the other, or none.
Put all the ones with no dogs in the test, then divide up the others across
train, validation and test.

Categories: 0=No dogs, 1=Savanna only, 2=Glacier only, 3=Both dogs
"""
from subprocess import run
import random

train_prop = 0.7
valid_prop = 0.2
test_prop = 0.1

# Get image filenames
proc = run(['ls', 'images'], capture_output=True)
filenames = sorted(proc.stdout.decode().split())
print(len(filenames))

class_0 = []
class_1 = []
class_2 = []
class_3 = []

for filename in filenames:
    # Find the associated labels filename, if it exists
    try:
        with open('labels/' + filename[:-3] + 'txt', 'r') as fin:
            lines = fin.readlines()
    except FileNotFoundError:
            lines = []
    # Count how many records, and if there is one, which dog is it
    if len(lines) == 0:
        class_0.append(filename)
    elif len(lines) == 2:
        class_3.append(filename)
    else:
        if lines[0][0] == '1':
            class_1.append(filename)
        else:
            class_2.append(filename)

# Start to split the images up.
test = class_0
class_0 = []
valid = []
train = []

# Put the image into lists
for i in range(int(test_prop * len(class_1)) + 1):
    img = random.choice(class_1)
    test.append(img)
    class_1.pop(class_1.index(img))
for i in range(int(test_prop * len(class_2)) + 1):
    img = random.choice(class_2)
    test.append(img)
    class_2.pop(class_2.index(img))
for i in range(int(test_prop * len(class_3)) + 1):
    img = random.choice(class_3)
    test.append(img)
    class_3.pop(class_3.index(img))
for i in range(int(valid_prop * len(class_1)) + 1):
    img = random.choice(class_1)
    valid.append(img)
    class_1.pop(class_1.index(img))
for i in range(int(valid_prop * len(class_2)) + 1):
    img = random.choice(class_2)
    valid.append(img)
    class_2.pop(class_2.index(img))
for i in range(int(valid_prop * len(class_3)) + 1):
    img = random.choice(class_3)
    valid.append(img)
    class_3.pop(class_3.index(img))
for img in class_1:
    train.append(img)
class_1 = []
for img in class_2:
    train.append(img)
class_2 = []
for img in class_3:
    train.append(img)
class_3 = []

# Double-check every img is only in one category
for img in train:
    if img in test: print(f"{img} in test and train")
    if img in valid: print(f"{img} in valid and train")
for img in valid:
    if img in test: print(f"{img} in valid and test")
# Should add up to the number of filenames from above
print(len(train), len(valid), len(test), len(train) + len(valid) + len(test))

# Copy images and labels into the appropriate folders
for img in train:
    run(['cp', f'images/{img}', 'train/images'])
    run(['cp', f'labels/{img[:-3]}txt', 'train/labels'])
for img in valid:
    run(['cp', f'images/{img}', 'valid/images'])
    run(['cp', f'labels/{img[:-3]}txt', 'valid/labels'])
for img in test:
    run(['cp', f'images/{img}', 'test/images'])
    # This line will throw an error at command-line for each file from class 0
    #   but it doesn't crash the program so just throw the errors and it's ok.
    run(['cp', f'labels/{img[:-3]}txt', 'test/labels'])
