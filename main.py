import cv2
import os

# 图像文件夹路径和输出视频文件名
image_folder = '/Users/liaohanlin/training/python/frame by frame turn to video/2023-05-28'
video_name = 'output_video.mp4'


# 获取所有图像文件名
images = [img for img in os.listdir(image_folder) if img.endswith("-2605658000.png")]

# 排序檔名
s_images = sorted(images)


# 图像尺寸
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

# 创建视频编码器
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(video_name, fourcc, 30, (width, height))

# 将每个图像写入视频
for image in s_images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

# 释放资源
cv2.destroyAllWindows()
video.release()
