from rembg import remove
import easygui
from PIL import Image

inputPath = easygui.fileopenbox(title='Select image file')
outputPath = easygui.filesavebox(title='Save file to..')

# mengambil gambar dan menghapus background
input = Image.open(inputPath)
output = remove(input)
output.save(outputPath)