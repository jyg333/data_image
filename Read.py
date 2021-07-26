"""Read image and videos """

import cv2 as cv
from rescale import rescaleFrame

capture = cv.VideoCapture('videos/dog.mp4') # VideoCapture(0) means web cams
while True:
    isTure, frame = capture.read() #capture returns by frame

    frame_resize = rescaleFrame(frame)

    cv.imshow('video',frame)
    cv.imshow('video_resized', frame_resize)

    if cv.waitKey(20) & 0xFF ==ord('d'): # if press 'd' key stop play videos
        break

def changeRes(width, height):
    '''Live videos'''
    capture.set(3, width)
    capture.set(4, height)
capture.release()
cv.destroyAllWindows()
# 비디오 윈도우에서 일정 시간이 지마녀 -215: Assertion failed,
# error가 발생한다 -> opencv가 지정한 위치에 미디어 파일을 찾지 못할때 발생
# Video run out of frame -> resize video frame
# 위의 에러를 해결하기위해 opencv02 에서 만든 rescaleFrame 함수 사용
