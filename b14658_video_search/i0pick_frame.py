import cv2
 
# Opens the Video file
movie_name = 'Blue_Planet_II'
cap= cv2.VideoCapture('video/'+movie_name+'.mp4')
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    print('i=', i)
    if ret == False:
        break
    if i % 40 == 0:
    	cv2.imwrite('static/img/source/'+movie_name+'_'+str(i)+'.jpg',frame)
    i+=1
 
cap.release()
cv2.destroyAllWindows()