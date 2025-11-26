#!/usr/bin/python3

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)

        # Manual formatting instead of ET.indent()
        xml_str = ET.tostring(root, encoding='utf-8').decode('utf-8')

        # Pretty format manually
        import re
        xml_str = re.sub(r'><', '>\n<', xml_str)
        xml_str = re.sub(r'(<[^/][^>]*>)', r'    \1', xml_str)
        xml_str = xml_str.replace('    <data>', '<data>')

        # Write without XML declaration
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(xml_str + '\n')

    except Exception as e:
        print(f"Error serializing to XML: {e}")


def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result_dict = {}
        for child in root:
            result_dict[child.tag] = child.text

        return result_dict

    except Exception as e:
        print(f"Error deserializing from XML: {e}")
        return {}
