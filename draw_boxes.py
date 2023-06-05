
# Make dictionary with spot: id , coordinates and predicted


file_path = 'predictions.txt'  # Replace with the path to your text file

with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            image_path, value = line.split()
            image_name = image_path.split('/')[-1]
            print('Image Name:', image_name)
            print('Value:', value)