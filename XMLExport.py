import Card as card
import xml.etree.ElementTree as ET
import random
import string
def Export(adrCost,desc,name):
# Create an instance of the class
    obj = card.Card(adrCost, desc,name)
# Create an XML element representing the class
    root = ET.Element("Card")
    name_elem = ET.SubElement(root, "adrenaline_cost")
    name_elem.text = str(obj.adrenaline_cost)
    value_elem = ET.SubElement(root, "description")
    value_elem.text = str(obj.description)
    value_elem = ET.SubElement(root, "name")
    value_elem.text = str(obj.name)

    # Write the XML to a file
    tree = ET.ElementTree(root)
    characters = string.ascii_letters + string.digits
    random_text = ''.join(random.choice(characters) for i in range(10))
    tree.write(f"xml/{random_text}.xml")
