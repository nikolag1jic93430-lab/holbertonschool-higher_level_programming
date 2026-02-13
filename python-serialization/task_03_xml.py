#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    try:
        with open(filename, "wb") as file:
            tree.write(file, encoding="utf-8", xml_declaration=True)
        return True
    except Exception:
        return False

def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}
        for child in root:
            result[child.tag] = child.text
        return result
    except Exception:
        return None

if __name__ == "__main__":
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    if serialize_to_xml(sample_dict, xml_file):
        print(f"Dictionary serialized to {xml_file}")
        deserialized = deserialize_from_xml(xml_file)
        print("Deserialized data:")
        print(deserialized)
    else:
        print("Serialization failed.")
