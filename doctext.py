import argparse
from enum import Enum
import io
import json
import os, os.path
from google.cloud import vision_v1
from google.cloud.vision_v1 import types
from PIL import Image, ImageDraw

class FeatureType(Enum):
    PAGE = 1
    BLOCK = 2
    PARA = 3
    WORD = 4
    SYMBOL = 5

def get_document_bounds(image_file, feature):

    client = vision_v1.ImageAnnotatorClient()

    bounds = []

    with io.open(image_file, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.document_text_detection(image=image)
    document = response.full_text_annotation

    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    for symbol in word.symbols:
                        if (feature == FeatureType.SYMBOL):
                            bounds.append(symbol.bounding_box)

                    if (feature == FeatureType.WORD):
                        bounds.append(word.bounding_box)

                if (feature == FeatureType.PARA):
                    bounds.append(paragraph.bounding_box)

            if (feature == FeatureType.BLOCK):
                bounds.append(block.bounding_box)

        if (feature == FeatureType.PAGE):
            bounds.append(block.bounding_box)

    return bounds


def render_doc_text(opn,filein):
    image = Image.open(os.path.join(opn,filein))
    bounds = get_document_bounds(os.path.join(opn,filein), FeatureType.PARA)
    result = {'vertices':[]}

    for bound in bounds:
        item = [
        {'x': bound.vertices[0].x, 'y': bound.vertices[0].y},
        {'x': bound.vertices[1].x, 'y': bound.vertices[1].y},
        {'x': bound.vertices[2].x, 'y': bound.vertices[2].y},
        {'x': bound.vertices[3].x, 'y': bound.vertices[3].y},
        ]
        result['vertices'].append(item)

    return result
