# Make dictionary with spot: id , coordinates and predicted
from utils.image_utils import extract_bndbox_values
import cv2 
file_path = 'predictions.txt'  # Replace with the path to your text file
image_data = {}
xml_file = "parking.xml"
image_cv = cv2.imread("parking.jpg")
bndbox_values = extract_bndbox_values(xml_file)
with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            image_path, value = line.split()
            image_name = image_path.split('/')[-1]
            image_data[image_name] = { "is_busy" :int(value), "coordinates": bndbox_values[image_name.replace(".jpg", "")] }
print(len(image_data))
# Loop over image data and draw boxes 
for spot_name , values in image_data.items():
    print(spot_name)
    is_busy = values["is_busy"]
    coordinates = values["coordinates"]
    xmin, ymin, xmax, ymax, = coordinates["xmin"], coordinates["ymin"], coordinates["xmax"], coordinates["ymax"]
    id = spot_name.replace("jpg", "").replace("spot", "")
    if(is_busy == 1):
        cv2.rectangle(image_cv, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 255, 0), 2)
        cv2.putText(img = image_cv, 
                    text =id,
                    org=(int(xmin), int(ymin)-5),
                    fontFace =cv2.FONT_HERSHEY_SIMPLEX, 
                    fontScale =0.2, 
                    color = (36,255,12), 
                    thickness = 1)

    else:
        cv2.rectangle(image_cv, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 0, 255), 2)

cv2.imwrite("image_with_boxes.jpg", image_cv)
    


