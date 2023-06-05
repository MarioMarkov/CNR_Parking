import xml.etree.ElementTree as ET
import math
import cv2
import numpy as np

def extract_bndbox_values(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    bndbox_values = {}

    for obj in root.findall('object'):
        bndbox = obj.find('bndbox')
        name = obj.find('name').text

        xmin = float(bndbox.find('xmin').text)
        ymin = float(bndbox.find('ymin').text)
        xmax = float(bndbox.find('xmax').text)
        ymax = float(bndbox.find('ymax').text)
        bndbox_values[name] = {'xmin': xmin, 'ymin': ymin, 'xmax': xmax, 'ymax': ymax}

    return bndbox_values

def extract_rotated_box_values(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    bndbox_values = {}

    for obj in root.findall('object'):
        #bndbox = obj.find('bndbox')
        name = obj.find('name').text
        #print(name)
        rotated_box = obj.find('rotated_box')
        cx = float(rotated_box.find('cx').text)
        cy = float(rotated_box.find('cy').text)
        width = float(rotated_box.find('width').text)
        height = float(rotated_box.find('height').text)
        rot = float(rotated_box.find('rot').text)

        bndbox_values[name] = {'cx': cx, 'cy': cy, 'width': width,
                               'height': height, 'rot':rot}

    return bndbox_values

def extract_polygon_box_values(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    bndbox_values = {}

    for obj in root.findall('object'):
        bndbox = obj.find('bndbox')
        name = obj.find('name').text

        x1 = float(bndbox.find('x1').text)
        y1 = float(bndbox.find('y1').text)
        x2 = float(bndbox.find('x2').text)
        y2 = float(bndbox.find('y2').text)
        x3 = float(bndbox.find('x3').text)
        y3 = float(bndbox.find('y3').text)
        x4 = float(bndbox.find('x4').text)
        y4 = float(bndbox.find('y4').text)

        bndbox_values[name] = {'x1': x1, 'y1': y1, 
                               'x2': x2,'y2': y2,
                               'x3':x3, 'y3':y3,
                               'x4':x4,'y4':y4,}

    return bndbox_values


def name_to_id(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    for idx, obj in enumerate(root.findall('object')):
        obj.find('name').text =  obj.find('name').text + str(idx)
    
    tree.write("parking2_id.xml")

#name_to_id("parking2.xml")

def rotate_point(x, y, cx, cy, angle):
    """Rotate a point around another point."""
    angle_rad = math.radians(angle)
    cos_theta = math.cos(angle_rad)
    sin_theta = math.sin(angle_rad)
    nx = (cos_theta * (x - cx)) + (sin_theta * (y - cy)) + cx
    ny = (cos_theta * (y - cy)) - (sin_theta * (x - cx)) + cy
    return nx, ny

def cut_patch_from_rotated_box(rotated_box, patch):
    # Extract the rotated box coordinates
    x1, y1, x2, y2, x3, y3, x4, y4 = rotated_box

    # Calculate the center of the rotated box
    cx = (x1 + x2 + x3 + x4) / 4
    cy = (y1 + y2 + y3 + y4) / 4

    # Calculate the angle of rotation
    angle = math.degrees(math.atan2(y2 - y1, x2 - x1))

    # Rotate the patch's top-left and bottom-right coordinates
    patch_x1, patch_y1 = rotate_point(patch[0], patch[1], cx, cy, -angle)
    patch_x2, patch_y2 = rotate_point(patch[2], patch[3], cx, cy, -angle)

    # Calculate the axis-aligned bounding box coordinates
    bbox_x1 = min(patch_x1, patch_x2)
    bbox_y1 = min(patch_y1, patch_y2)
    bbox_x2 = max(patch_x1, patch_x2)
    bbox_y2 = max(patch_y1, patch_y2)

    # Calculate the intersection between the patch and the bounding box
    intersection_x1 = max(x1, bbox_x1)
    intersection_y1 = max(y1, bbox_y1)
    intersection_x2 = min(x3, bbox_x2)
    intersection_y2 = min(y3, bbox_y2)

    # Transform the intersection coordinates back to rotated box coordinates
    intersection = [
        rotate_point(intersection_x1, intersection_y1, cx, cy, angle),
        rotate_point(intersection_x2, intersection_y2, cx, cy, angle)
    ]

    return intersection


def extract_intersection_values(file_path):
    # Example usage
    # rotated_box = [100, 100, 200, 100, 200, 200, 100, 200]  # Example rotated box coordinates
    # patch = [150, 150, 250, 250]  # Example patch coordinates

    # intersection = cut_patch_from_rotated_box(rotated_box, patch)
    # print(intersection)
    
    tree = ET.parse(file_path)
    root = tree.getroot()
    bndbox_values = {}

    for obj in root.findall('object'):
        bndbox = obj.find('bndbox')
        name = obj.find('name').text

        x1 = float(bndbox.find('x1').text)
        y1 = float(bndbox.find('y1').text)
        x2 = float(bndbox.find('x2').text)
        y2 = float(bndbox.find('y2').text)
        x3 = float(bndbox.find('x3').text)
        y3 = float(bndbox.find('y3').text)
        x4 = float(bndbox.find('x4').text)
        y4 = float(bndbox.find('y4').text)
        xmin = float(bndbox.find('xmin').text)
        ymin = float(bndbox.find('ymin').text)
        xmax = float(bndbox.find('xmax').text)
        ymax = float(bndbox.find('ymax').text)
        rotated_box = [x1, y1, x2, y2, x3, y3, y4, x4]
        patch = [xmin, ymin, xmax, ymax]
        #bndbox_values[name] = {'xmin': xmin, 'ymin': ymin, 'xmax': xmax, 'ymax': ymax}

    return bndbox_values

def crop_rotated_box(image, cx, cy, width, height, angle):
    # Convert angle from degrees to radians
    angle_rad = angle * (3.14159 / 180.0)

    # Calculate the corner points of the rotated box
    corner_points = [
        [cx - width / 2, cy - height / 2],
        [cx + width / 2, cy - height / 2],
        [cx + width / 2, cy + height / 2],
        [cx - width / 2, cy + height / 2]
    ]

    # Create a rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D((cx, cy), angle, 1.0)

    # Rotate the corner points
    rotated_points = [cv2.transform(np.array([point]), rotation_matrix)[0] for point in corner_points]

    # Find the minimum and maximum x, y coordinates of the rotated box
    min_x = min(rotated_points[0][0], rotated_points[1][0], rotated_points[2][0], rotated_points[3][0])
    max_x = max(rotated_points[0][0], rotated_points[1][0], rotated_points[2][0], rotated_points[3][0])
    min_y = min(rotated_points[0][1], rotated_points[1][1], rotated_points[2][1], rotated_points[3][1])
    max_y = max(rotated_points[0][1], rotated_points[1][1], rotated_points[2][1], rotated_points[3][1])

    # Convert the coordinates to integers
    min_x = int(min_x)
    max_x = int(max_x)
    min_y = int(min_y)
    max_y = int(max_y)

    # Crop the image
    cropped_image = image[min_y:max_y, min_x:max_x]

    return cropped_image
