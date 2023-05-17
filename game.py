from email.mime import image
import cv2
import numpy as np
import keyboard
import random, math
import streamlit as st

img = np.zeros((500, 500, 3), np.uint8)

# cv2.rectangle(img,(0,0),(500,500),(0,0,255),thickness=3)

cv2.rectangle(img, (40, 30), (300, 50), (0, 255, 0), thickness=-1)
cv2.rectangle(img, (100, 200), (120, 300), (0, 255, 0), thickness=-1)

a = 0

game_name = "ORGANISM"
start_pos_i = 480
start_pos_j = 480
i = start_pos_i
j = start_pos_j

step = 2
defeat = 0

f = open("score.txt", "r")
present_score = 0
best_score = int(f.read())
f.close()

radius = 5
flag = 2
target_j = random.randint(40, 490)
target_i = random.randint(40, 490)
target_radius = radius

# organism1
loc1 = (100, 100)
min_radius1 = 5
max_radius1 = 50
# wait_time1=100
radius1 = min_radius1
org_flag1 = 0

# organism2
loc2 = (400, 300)
min_radius2 = 10
max_radius2 = 100
# wait_time1=100
radius2 = min_radius2
org_flag2 = 0

play_again = 1

rules = """\n
Press `e` begin \n
Press `r` to rerun \n
Don't touch the `green dots` to survive! \n
Eat `white dots` to gain points!\n
Enjoy!"""

# st.write(game_name)
st.markdown(f"<h1 style='text-align: center;'>{game_name}</h1>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center;'>{rules}</h1>", unsafe_allow_html=True)
image_placeholder = st.empty()
while True:
    
    cv2.rectangle(img, (0, 0), (500, 500), (0, 0, 0), thickness=-1)
    cv2.rectangle(img, (0, 0), (500, 500), (0, 0, 255), thickness=10)
    cv2.line(img, (0, 30), (499, 30), (0, 0, 255), thickness=5)

    

    # cv2.putText(img, game_name, (175, 23), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255), thickness=1)

    cv2.rectangle(img, (7, 6), (130, 25), (255, 255, 255), thickness=-1)
    cv2.putText(img, "BEST SCORE: ", (7, 20), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0, 0, 0), thickness=1)
    cv2.putText(img, str(best_score), (90, 20), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0, 0, 255), thickness=1)

    cv2.rectangle(img, (400, 6), (493, 25), (255, 255, 255), thickness=-1)
    cv2.putText(img, "SCORE: ", (400, 20), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0, 0, 0), thickness=1)
    cv2.putText(img, str(present_score), (450, 20), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0, 0, 255), thickness=1)

    #     cv2.rectangle(img,(100,200),(120,300),(0,255,0),thickness=-1)
    #     cv2.rectangle(img,(60,60),(450,450),(0,255,0),thickness=-1)

    # organism1
    cv2.circle(img, loc1, radius1, (0, 255, 0), thickness=-1)

    # organism2
    cv2.circle(img, loc2, radius2, (0, 255, 0), thickness=-1)

    #     cv2.rectangle(img,(),())
    cv2.rectangle(img, (290, 270), (200, 210), (255, 255, 255), thickness=-1)
    cv2.putText(img, "START", (200, 250), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), thickness=2)

    # cv2.imshow("img", img)
    image_placeholder.image(img, channels="RGB")
    k = cv2.waitKey(0)
    if (keyboard.is_pressed("e")):
        break

while (True):
    cv2.rectangle(img, (0, 0), (500, 500), (0, 0, 0), thickness=-1)
    cv2.rectangle(img, (0, 0), (500, 500), (0, 0, 255), thickness=10)
    cv2.line(img, (0, 30), (499, 30), (0, 0, 255), thickness=5)

    # st.write(game_name)
    # cv2.putText(img, game_name, (175, 23), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255), thickness=1)

    cv2.rectangle(img, (7, 6), (130, 25), (255, 255, 255), thickness=-1)
    cv2.putText(img, "BEST SCORE: ", (7, 20), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0, 0, 0), thickness=1)
    cv2.putText(img, str(best_score), (90, 20), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0, 0, 255), thickness=1)

    cv2.rectangle(img, (400, 6), (493, 25), (255, 255, 255), thickness=-1)
    cv2.putText(img, "SCORE: ", (400, 20), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0, 0, 0), thickness=1)
    cv2.putText(img, str(present_score), (450, 20), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0, 0, 255), thickness=1)

    #     organism(loc,min_radius,max_radius)
    #     cv2.rectangle(img,(100,200),(120,300),(0,255,0),thickness=-1)
    #     cv2.rectangle(img,(60,60),(450,450),(0,255,0),thickness=-1)

    # organism1
    if (radius1 < max_radius1 and org_flag1 == 0):
        radius1 += 1
        cv2.circle(img, loc1, radius1, (0, 255, 0), thickness=-1)
    elif (radius1 > min_radius1):
        radius1 -= 1
        cv2.circle(img, loc1, radius1, (0, 255, 0), thickness=-1)
        org_flag1 = 1
    else:
        org_flag1 = 0

    # organism2
    if (radius2 < max_radius2 and org_flag2 == 0):
        radius2 += 1
        cv2.circle(img, loc2, radius2, (0, 255, 0), thickness=-1)
    elif (radius2 > min_radius2):
        radius2 -= 1
        cv2.circle(img, loc2, radius2, (0, 255, 0), thickness=-1)
        org_flag2 = 1
    else:
        org_flag2 = 0

    # Eating Mechanism
    if (img[target_j, target_i][1] != 255):
        if (pow(target_i - i, 2) + pow(target_j - j, 2) < pow(target_radius + radius, 2)):
            present_score += 10
            cv2.circle(img, (target_i, target_j), target_radius, (0, 0, 0), thickness=-1)
            target_j = random.randint(40, 490)
            target_i = random.randint(40, 490)
            radius += 3
        cv2.circle(img, (target_i, target_j), target_radius, (255, 254, 254), thickness=-1)
    else:
        target_j = random.randint(40, 490)
        target_i = random.randint(40, 490)

    if (keyboard.is_pressed("d")):
        flag = 1
    elif (keyboard.is_pressed("a")):
        flag = -1
    elif (keyboard.is_pressed("w")):
        flag = 2
    elif (keyboard.is_pressed("s")):
        flag = -2

    if (flag == 1):
        cv2.circle(img, ((i - step) % 500, j % 500), radius, (0, 0, 0), thickness=-1)
        cv2.circle(img, ((i) % 500, j), radius, (255, 0, 0), thickness=-1)
        i += step
        # st.write(f"Flag: {flag}")
    elif (flag == -1):
        cv2.circle(img, ((i + step) % 500, j % 500), radius, (0, 0, 0), thickness=-1)
        cv2.circle(img, ((i) % 500, j), radius, (255, 0, 0), thickness=-1)
        i -= step
        # st.write(f"Flag: {flag}")
    elif (flag == -2):
        cv2.circle(img, (i % 500, (j - step) % 500), radius, (0, 0, 0), thickness=-1)
        cv2.circle(img, (i % 500, j % 500), radius, (255, 0, 0), thickness=-1)
        j += step
        # st.write(f"Flag: {flag}")
    elif (flag == 2):
        cv2.circle(img, (i % 500, (j + step) % 500), radius, (0, 0, 0), thickness=-1)
        cv2.circle(img, (i % 500, j % 500), radius, (255, 0, 0), thickness=-1)
        j -= step
        # st.write(f"Flag: {flag}")

    # DEFEAT
    if (flag == 1):
        if (img[j, i + radius][2] == 255):
            defeat = 1
            break
    if (flag == -1):
        if (img[j, i - radius][2] == 255):
            defeat = 1
            break
    if (flag == -2):
        if (img[j + radius, i][2] == 255):
            defeat = 1
            break
    if (flag == 2):
        if (img[j - radius, i][2] == 255):
            defeat = 1
            break
    if (pow(loc1[0] - i, 2) + pow(loc1[1] - j, 2) < pow(radius + radius1, 2)):
        defeat = 1
        break
    if (pow(loc2[0] - i, 2) + pow(loc2[1] - j, 2) < pow(radius + radius2, 2)):
        defeat = 1
        break

    # cv2.imshow("img", img)
    image_placeholder.image(img, channels="RGB")
    # Quit
    if (keyboard.is_pressed("q")):
        cv2.rectangle(img, (300, 270), (200, 210), (255, 255, 255), thickness=-1)
        cv2.putText(img, f"Quit?", (200, 250), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), thickness=2)
        # cv2.imshow("img", img)
        image_placeholder.image(img, channels="RGB")
        m = cv2.waitKey(0)
        while (not (keyboard.is_pressed("y") or keyboard.is_pressed("n"))):
            cv2.rectangle(img, (300, 270), (200, 210), (255, 255, 255), thickness=-1)
            cv2.putText(img, "Quit?", (200, 250), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), thickness=2)
            # cv2.imshow("img", img)
            image_placeholder.image(img, channels="RGB")
            m = cv2.waitKey(0)
        if (keyboard.is_pressed("y")):
            defeat = 0
            #             play_again=0
            keyboard.is_pressed("r")
            cv2.destroyAllWindows()
            break
        elif (keyboard.is_pressed("n")):
            #             cv2.putText(img,"Quit? y/n",(150,250),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,0),thickness=2)
            continue

if (defeat == 1):
    cv2.rectangle(img, (310, 270), (200, 210), (255, 255, 255), thickness=-1)
    cv2.putText(img, "DEFEAT", (200, 250), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), thickness=2)
    # cv2.imshow("img", img)
    image_placeholder.image(img, channels="RGB")
    k = cv2.waitKey(0)

# print(int(f.read()))
if (best_score < present_score):
    f = open("score.txt", "w+")
    f.write(str(present_score))
    f.close()
cv2.destroyAllWindows()
# print(loc1[0],loc1[1])