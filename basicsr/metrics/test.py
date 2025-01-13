from basicsr.metrics import calculate_psnr
import cv2 as cv

img1 = cv.imread("demo/blurry.jpg")

# height, width = img1.shape[:2]
# kernel_size = int(0.02*min(width, height))
# if kernel_size % 2 == 0:
#     kernel_size += 1

# img1 = cv.GaussianBlur(img1, (kernel_size,kernel_size), 0)

# cv.imwrite("demo/images/train/35008_2.jpg", img1)

img2 = cv.imread("demo/deblur_img.png")

print(calculate_psnr(img1, img2, crop_border=0, input_order='HWC', test_y_channel=False))