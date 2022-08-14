import cv2
from PIL import Image
main_img = cv2.imread("canada.jpg")
back_img = cv2.imread("tree.jpg")

main_img =cv2.resize(main_img, (512,512))
back_img = cv2.resize(back_img, (512,512))
final_img = cv2.add(main_img, back_img)

cv2.imshow("Final Image", final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


img1 = Image.open('canada.jpg')
img2 = Image.open('tree.jpg')

image_new = Image.new('RGB',(img1.width+img2.width,img1.height))
image_new.paste(img1,(0,0))
image_new.paste(img2,(img1.width,0))

image_new.save('merged.jpg')



path = r'merged.jpg'


image = cv2.imread(path)
image = cv2.resize(image, (512,512))
window_name = 'image'
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()

