#load packages
from xml.etree import cElementTree as ET
import uuid
import os
import json
import sys


'''
get relevant xml attributes and convert to dictonary

:param root: xml root for image
:return: obs: dictionary for one annotation from the image
'''
def get_attributes(root, labels):
    for object in root.findall('object'):

        #get image size for scaling
        size = root.find('size')
        image_width = size.find('width').text
        image_height = size.find('height').text


        #get_attributes
        label = object.find('name').text
        labels.add(label)
        bndbox = object.find('bndbox')
        xmin = bndbox.find('xmin').text
        ymin = bndbox.find('ymin').text
        xmax = bndbox.find('xmax').text
        ymax = bndbox.find('ymax').text

        #TODO: bulid in check and error handling for missing data

        obs = [{'x': float(xmin) / float(image_width),
                'x2': float(xmax) / float(image_width),
                'y': float(ymin) / float(image_height),
                'y2': float(ymax) / float(image_height),
                'id': str(uuid.uuid1()),
                'label': label}]
        return obs



'''
This funtion converts annotations information from many xml files to one json
'''
def main():
    # initialize variable
    labels = set()
    annotation = {}

    # configure
    version = '1.0'
    type = "localization"
    rootdir = sys.argv[1]
    foldername = sys.argv[2]


    #get annotation attrinutes for ech xml file
    for _, _, files in os.walk(rootdir):
        for file in files:
            if file.endswith('.xml'):
                path = '/'.join([rootdir, file])
                root = ET.parse(path).getroot()
                annotation['/'.join([foldername, root.find('filename').text])] = get_attributes(root, labels)

    # only write/overwrite when there was some information from xmls found
    if annotation:
        #write results in json
        annotations = {'version': version, 'type': type, 'labels': list(labels), 'annotations': annotation}
        with open('/'.join([rootdir, '_annotations.json']), 'w') as outfile:
            json.dump(annotations, outfile)

if __name__ == "__main__":
    main()


