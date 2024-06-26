with open('data.txt', 'r') as fin:
    lines = fin.readlines()

# For each line in the file, break it into its different parts
for i, line in enumerate(lines):
    lines[i] = line[:-1].split()

# The images off my cell phone are 3024 x 4032 pixels.  Convert pixel
#   values of location into proportion
for i, line in enumerate(lines):
    line[1] = float(line[1]) / 3024
    line[2] = float(line[2]) / 4032
    line[3] = float(line[3]) / 3024
    line[4] = float(line[4]) / 4032
    # Make sure all value are what they should be
    if (line[1] > 1 or line[2] > 1 or line[3] > 1 or line[4] > 1 or
        line[1] < 0 or line[2] < 0 or line[3] < 0 or line[4] < 0):
        raise ValueError(f"Line #{i} out of range: {line[1:5]}")

# Sort by filename so we can create a separate annotation file for each image
lines = sorted(lines, key=lambda x: x[0])

# Now, create a text file for each image that has a dog in it.
for i, line in enumerate(lines):
    # Make label filename same as image filename but replace .jpg with .txt
    #   Change folder from images to labels
    filename = "labels/" + line[0][:-3] + "txt"
    with open(filename, 'a')  as fout:
        print(f"{line[5]} {line[1]} {line[2]} {line[3]} {line[4]}", file = fout)
