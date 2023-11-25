from func import *
from time import sleep

for action in actions:
    for sequence in range(m):
        try:
            os.makedirs(os.path.join(Dataset_Path, action, str(sequence)))
        except:
            pass


with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    # 
    
    for action in actions:
        try:
            print("ACTION",action)
            for sequence in range(m):
                print("sequence",sequence)
                # looping through video squence
                for frame_num in range(n):
                    try:
                        print("Action",action,'seq',sequence,"frame_num",frame_num)
                        action_folder = os.path.join('Sign-Language-Digits-Dataset', 'Dataset', action)
                        files = os.listdir(action_folder)


                        # ret, frame = cap.read()
                        frame=cv2.imread('Sign-Language-Digits-Dataset\Dataset/{}/{}'.format(action,files[frame_num]))
                        # frame=cv2.imread('{}{}.png'.format(action,sequence))
                        # frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

                        image, results = medp_det_l(frame, hands)
        #                 print("results>>>>>",results)

                        drw_keypoints(image, results)

                        if frame_num == 0:
                            cv2.putText(image, 'STARTING COLLECTION', (120,200),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255, 0), 4, cv2.LINE_AA)
                            cv2.putText(image, 'Collecting frames for {} Video Number {}'.format(action, sequence), (15,12),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                            cv2.imshow('OpenCV Feed', image)
                            cv2.waitKey(200)
                        else:
                            cv2.putText(image, 'Collecting frames for {} Video Number {}'.format(action, sequence), (15,12),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                            cv2.imshow('OpenCV Feed', image)

                        k_points = extcrt_kpoints(results)
                        npy_path = os.path.join(Dataset_Path, action, str(sequence), str(frame_num))
                        np.save(npy_path, k_points)

                        
                    except Exception as e:
                        continue
        except Exception as e:
            print('Exception',e)
            continue
    
    cv2.destroyAllWindows()