import cv2
import sys

cap1 = cv2.VideoCapture('woman.mp4')

if not cap1.isOpened():
    print('동영상을 열 수 없습니다')
    sys.exit()

cap2 = cv2.VideoCapture('raining.mp4')

if not cap2.isOpened():
    print('동영상을 열 수 없습니다')
    sys.exit()

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = round(cap1.get(cv2.CAP_PROP_FPS))

delay = int(1000 / fps)

do_composit = False

while True:
    ret1, frame1 = cap1.read()

    if not ret1:
        break

    if do_composit :
        ret2, frame2 = cap2.read()

        if not ret2:
            break

        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (50, 150, 0), (70, 255, 255))

        cv2.copyTo(frame2, mask, frame1)

    cv2.imshow('frame', frame1)
    key = cv2.waitKey(delay)

    if key == ord(' '):
        do_composit = not do_composit
    elif key == 27 :
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()