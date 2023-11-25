
import cv2, numpy as np
import os, string
import mediapipe as mp

med_dr = mp.solutions.drawing_utils
med_dr_st = mp.solutions.drawing_styles
med_hnds = mp.solutions.hands

def medp_det_l(image, model):

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = model.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image, results

def drw_keypoints(image, results):
    if results.mul_hand_points:
      for hand_points in results.mul_hand_points:
        med_dr.draw_landmarks(
            image,
            hand_points,
            med_hnds.HAND_CONNECTIONS,
            med_dr_st.get_default_hand_landmarks_style(),
            med_dr_st.get_default_hand_connections_style())


def extcrt_kpoints(results):
    if results.mul_hand_points:
      for hand_points in results.mul_hand_points:
        rh = np.array([[res.x, res.y, res.z] for res in hand_points.landmark]).flatten() if hand_points else np.zeros(21*3)
        return(np.concatenate([rh]))

Dataset_Path = os.path.join('MP_Data')

dig = list(np.arange(10))
alpha= list(string.ascii_uppercase)
# char = dig + alpha
# actions = np.array(list(string.ascii_uppercase))
actions = np.array(alpha)

m = 15

n = 15
