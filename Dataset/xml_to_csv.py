import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        print(xml_file)
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[5][0].text),
                     int(member[5][1].text),
                     int(member[5][2].text),
                     int(member[5][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    #print(xml_list)
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
     for directory in [r"pascal_voc_out_folder"]:
         image_path = os.path.join(os.getcwd(), directory)
         xml_df = xml_to_csv(image_path)
         xml_df.to_csv("NAME_OF_CSV_FILE.csv", index=None)
         print('Successfully converted xml to csv.')


main() 