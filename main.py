from cvzone.HandTrackingModule import HandDetector
import cv2
import socket

#init webcam; width; height
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
success, img = cap.read()
h, w, _ = img.shape
detector = HandDetector(detectionCon=0.8, maxHands=2)

#Using UDP (SOCK_DGRAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 5052)

while True:
    # Get image frame from webcam
    success, img = cap.read()
    # Find the hand and its landmarks
    hands, img = detector.findHands(img)  # with draw
    # hands = detector.findHands(img, draw=False)  # without draw
    data = []
    # data1 = []
    # data2 = []

    if hands:
        # Hand 1
        # hand = hands[0]
        # lmList = hand["lmList"]  # Get list of 21 Landmark points
        # bbox = hand["bbox"]
        # centerPoint = hand["center"]
        # handType = hand["type"]
        # pointIndex = lmList[8][0:2] #Switch to 0:3 for 3d
        # #Starburst
        # fingers = detector.fingersUp(hand)
        #
        #
        # if handType == "Left":
        #     for lm in lmList:
        #         data.extend([lm[0], h - lm[1], lm[2]])
        #     sock.sendto(str.encode(str(data)), serverAddressPort)

        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # Get list of 21 Landmark points
        bbox1 = hand1["bbox"]
        centerPoint1 = hand1["center"]
        handType1 = hand1["type"]
        pointIndex1 = lmList1[8][0:2] #Switch to 0:3 for 3d
        #Starburst
        fingers1 = detector.fingersUp(hand1)
        print(handType1)


        if handType1 == "Left":
            for lm1 in lmList1:
                data.extend([lm1[0], h - lm1[1], lm1[2]])
            sock.sendto(str.encode(str(data)), serverAddressPort)

    # if len(hands==2):
    #     # Hand 2
    #     hand2 = hands[1]
    #     lmList2 = hand2["lmList"]  # Get list of 21 Landmark points
    #     bbox2 = hand2["bbox"]
    #     centerPoint2 = hand2["center"]
    #     handType2 = hand2["type"]
    #     pointIndex2 = lmList2[8][0:2] #Switch to 0:3 for 3d
    #     fingers2 = detector.fingersUp(hand2)
    #
    #     for lm2 in lmList2:
    #         data2.extend([lm2[0], h - lm2[1], lm2[2]])
    #
    #     sock2.sendto(str.encode(str(data2)), serverAddressPort)

    # Display
    cv2.imshow("Image", cv2.flip(img, 1))
    # cv2.waitKey(1)
    if cv2.waitKey(5) & 0xFF == 27:
        break