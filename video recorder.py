import cv2 as cv

video_file = 0
video = cv.VideoCapture(video_file)

codec = cv.VideoWriter_fourcc(*'XVID')

if video.isOpened():
    preview_mode = True
    record_mode = False

    result = cv.VideoWriter('result.avi', codec, video.get(cv.CAP_PROP_FPS), (int(video.get(cv.CAP_PROP_FRAME_WIDTH)), int(video.get(cv.CAP_PROP_FRAME_HEIGHT))))

    while True:
        valid, img = video.read()
        img = cv.flip(img, 1)

        # 후지필름 스타일 필터 적용
        alpha = 0.7  # 블렌딩 가중치
        beta = 1 - alpha

        # 필터 적용
        filter_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        filter_img = cv.cvtColor(filter_img, cv.COLOR_GRAY2BGR)

        img = cv.addWeighted(img, alpha, filter_img, beta, 0)
        if not valid:
            print("카메라에서 프레임을 읽을 수 없습니다.")
            break

        if preview_mode:
            cv.imshow('VideoRecorder_likeFujifilm', img)

        if record_mode:
            
            
            radius = 10
            center = (img.shape[1] - radius - 10, radius + 10)
            color = (0, 0, 255)  # 빨간색 (BGR)
            thickness = cv.FILLED
            cv.circle(img, center, radius, color, thickness)
            cv.imshow('VideoRecorder_likeFujifilm', img)
            result.write(img)

        key = cv.waitKey(1)

        # 스페이스 키를 눌러 모드 전환
        if key == ord(' '):
            preview_mode = not preview_mode
            record_mode = not record_mode

        # esc 키를 눌러 프로그램 종료
        elif key == 27:
            break

    result.release()
else:
    print("비디오 파일 열기 실패")

video.release()
cv.destroyAllWindows()
