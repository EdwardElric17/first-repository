from xml.etree import ElementTree

worth_red = 0
worth_green = 0
worth_blue = 0
value = 1
level = 0
tree = ElementTree.parse("cube_pyramid.xml")
root = tree.getroot()

def func(module):
    global worth_red, worth_green, worth_blue, value
    value += 1
    for elem in module:
        for i in elem.attrib.values():
            if i == 'red':
                worth_red += value
            if i == 'green':
                worth_green += value
            if i == 'blue':
                worth_blue += value
    for elem in module:
        if len(elem) > 0:
            func(elem)

for i in root.attrib.values():
    if i == 'red':
        worth_red += value
    if i == 'green':
        worth_green += value
    if i == 'blue':
        worth_blue += value
func(root)
print(worth_red, worth_green, worth_blue)