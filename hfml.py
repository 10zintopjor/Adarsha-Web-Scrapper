import os
from pathlib import Path
from openpecha import serializers
from openpecha.formatters import HFMLFormatter
from openpecha.serializers import HFMLSerializer, EpubSerializer
from openpecha.core.pecha import OpenPechaFS




if __name__ == "__main__":
    hfml_path = "./hfml"
    opf_path = "./opfs/Tengyur/degetengyur/degetengyur.opf"
   
    serializer = HFMLSerializer(opf_path)
    serializer.serialize(output_path=hfml_path)
    