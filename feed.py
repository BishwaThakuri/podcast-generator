import yaml
import xml.etree.ElementTree as xml_tree

with open('feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

# Create the root <rss> element with attributes
rss_element = xml_tree.Element(
    'rss',
    {
        'version': '2.0',
        'xmlns:itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
        'xmlns:content': 'http://purl.org/rss/1.0/modules/content/'
    }
)

    

channel_element = xml_tree.SubElement(rss_element, 'channel')

link_prefix = yaml_data['link']

xml_tree.SubElement(channel_element, 'title').text = yaml_data['title']
xml_tree.SubElement(channel_element, 'format').text = yaml_data['format']
xml_tree.SubElement(channel_element, 'subtitle').text = yaml_data['subtitle']
xml_tree.SubElement(channel_element, 'itunes:author').text = yaml_data['title']
xml_tree.SubElement(channel_element, 'description').text = yaml_data['description']
# itunes:image is an empty element with href attribute
xml_tree.SubElement(channel_element, 'itunes:image', {'href': link_prefix + yaml_data['image']})
xml_tree.SubElement(channel_element, 'language').text = yaml_data['language']
xml_tree.SubElement(channel_element, 'link').text = link_prefix

# itunes:category is an empty element with text attribute
xml_tree.SubElement(channel_element, 'itunes:category', {'text': yaml_data['category']})


for item in yaml_data['item']:
    item_element = xml_tree.SubElement(channel_element, 'item')
    xml_tree.SubElement(item_element, 'title').text = item['title']
    xml_tree.SubElement(item_element, 'itunes:author').text = yaml_data['author'] if 'author' in yaml_data else ''
    xml_tree.SubElement(item_element, 'description').text = item['description']
    # enclosure: url, length, type
    xml_tree.SubElement(item_element, 'enclosure', {
        'url': link_prefix + item['file'],
        'length': str(item['length']).replace(',', ''),
        'type': yaml_data['format'] if 'format' in yaml_data else 'audio/mpeg'
    })
    xml_tree.SubElement(item_element, 'guid').text = link_prefix + item['file']
    xml_tree.SubElement(item_element, 'pubDate').text = item['published']
    if 'duration' in item:
        xml_tree.SubElement(item_element, 'itunes:duration').text = item['duration']


# Write the XML tree to file
output_tree = xml_tree.ElementTree(rss_element)
output_tree.write('podcast.xml', encoding='utf-8', xml_declaration=True)

