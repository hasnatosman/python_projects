# import qrcode as qr
# img = qr.make('Hasnat Osman')
# img.save('hasnat.png')

import qrcode
from PIL import Image
qr = qrcode.QRCode(version = 1,error_correction = qrcode.constants.ERROR_CORRECT_H,box_size = 10, border = 10)
qr.add_data('https://hasnatosman.wordpress.com/')
qr.make(fit = True)
img = qr.make_image(fill_color = 'blue',back_color = 'white')
img.save('hasnat.png')
