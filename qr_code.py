import qrcode

website_link = 'https://www.youtube.com/watch?v=L4rOBdjcwLc&list=RDL4rOBdjcwLc&start_radio=1'

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
# The version parameter is an integer from 1 to 40 that controls the size of the QR code.
# The box_size parameter controls how many pixels each “box” of the QR code is.
# The border parameter controls how many boxes thick the border should be.

qr.add_data(website_link)
qr.make() # .make() generate the QR code

img = qr.make_image(fill_color = 'black', back_color = 'white') # save this created QR code in an img pillow object
# using qr.make_image()
img.save('youtube_qr.png') # store and save the file. We can do this using pillow's save() command. We specify the file
# name inside the brackets, which is youtube_qr.png
