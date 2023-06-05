import xml.etree.ElementTree as ET

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
        bndbox = obj.find('bndbox')
        name = obj.find('name').text

        cx = float(bndbox.find('cx').text)
        cy = float(bndbox.find('cy').text)
        width = float(bndbox.find('width').text)
        height = float(bndbox.find('height').text)
        rot = float(bndbox.find('rot').text)

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