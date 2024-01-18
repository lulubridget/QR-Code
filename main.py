import pyqrcode 
import png 
from pyqrcode import QRCode 
  

# Generate QR code 
url = pyqrcode.create('https://lulubridget.github.io/ImLuWang.github.io/') 
  
# Create and save the png file naming "myqr.png" 
url.png('Lu Website.png', scale = 6) 
