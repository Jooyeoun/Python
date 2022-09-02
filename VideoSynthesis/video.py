import cv2
import numpy as np
import sys

# 합성시킬 두 개의 영상 열기
cap1 = cv2.VideoCapture('110877.mp4')
cap2 = cv2.VideoCapture('128504.mp4')

if not cap1.isOpened() or not cap2.isOpened():
    print('비디오를 열 수 없습니다')
    sys.exit()

frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))

print('frame_cnt1 : ', frame_cnt1)
print('frame_cnt2 : ', frame_cnt2)
fps = cap1.get(cv2.CAP_PROP_FPS)
print(fps)

delay = int(1000/fps)

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(w)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

# 1번 동영상 마지막 2초전까지 복사
for i in range(frame_cnt1 - int(fps*2)): # 237 - 60
    ret1, frame1 = cap1.read()
    out.write(frame1)
    cv2.imshow('output', frame1)
    cv2.waitKey(delay)

for i in range(int(fps*2)):
    ret1, frame1 = cap1.read() # 남은 60프레임
    ret2, frame2 = cap2.read() # 처음 60프레임

    dx = int(w / int(fps*2)) * i # (1280 / 60) * i

    frame = np.zeros((h, w, 3), dtype=np.uint8) # 검은색
    frame[:, 0:dx, :] = frame2[:, 0:dx, :]
    frame[:, dx:w, :] = frame1[:, dx:w, :]

    out.write(frame)
    cv2.imshow('output', frame)
    cv2.waitKey(delay)

for i in range(int(fps*2), frame_cnt2):
    ret2, frame2 = cap2.read()
    out.write(frame2)
    cv2.imshow('output', frame2)
    cv2.waitKey(delay)

cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()