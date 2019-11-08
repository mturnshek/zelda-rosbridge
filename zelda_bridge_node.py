import keyboard
import numpy as np
import rospy
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import Twist
from mss import mss
from rospy import Publisher, Subscriber
from sensor_msgs.msg import Image
from std_msgs.msg import Bool

import cv2


class ZeldaBridgeNode(object):
    def __init__(self):
        rospy.init_node("zelda_bridge_node")
        self.arrows = Subscriber("/cmd_vel", Twist, self.arrows_callback)
        self.interact = Subscriber(
            "/interact", Bool, self.create_button_callback("r"))
        self.swing = Subscriber(
            "/swing", Bool, self.create_button_callback("d"))
        self.item = Subscriber("/item", Bool, self.create_button_callback("s"))
        self.map = Subscriber("/map", Bool, self.create_button_callback("e"))
        self.menu = Subscriber("/menu", Bool, self.create_button_callback("q"))

        self.camera = Publisher("/camera/rgb/image_raw", Image, queue_size=10)

        self.keyboard_state = {
            "left": False,
            "right": False,
            "up": False,
            "down": False
        }

        self.bridge = CvBridge()
        self.screenshotter = mss()
        self.monitor = {"top": 1000, "left": 800, "width": 500, "height": 500}

        self.rate = rospy.Rate(30)
        while not rospy.is_shutdown():
            self.read_image()

            if self.keyboard_state["left"]:
                keyboard.press("left")
            else:
                keyboard.release("left")
            if self.keyboard_state["right"]:
                keyboard.press("right")
            else:
                keyboard.release("right")
            if self.keyboard_state["up"]:
                keyboard.press("up")
            else:
                keyboard.release("up")
            if self.keyboard_state["down"]:
                keyboard.press("down")
            else:
                keyboard.release("down")
            self.rate.sleep()

    def read_image(self):
        img = np.array(self.screenshotter.grab(self.monitor))
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)

        # resize image
        width = int(img.shape[1] * 0.5)
        height = int(img.shape[0] * 0.5)
        dim = (width, height)
        resized = cv2.resize(img, dim)
        try:
            ros_image = self.bridge.cv2_to_imgmsg(resized, "bgr8")
            self.camera.publish(ros_image)
        except CvBridgeError as e:
            print(e)

    def arrows_callback(self, twist):
        self.keyboard_state["right"] = twist.angular.z < -0.25
        self.keyboard_state["left"] = twist.angular.z > 0.25
        self.keyboard_state["up"] = twist.linear.x > 0.25
        self.keyboard_state["down"] = twist.linear.x < -0.25

    def create_button_callback(self, key):
        def callback(bool):
            if bool.data:
                keyboard.press(key)
                for _ in range(3):
                    self.rate.sleep()
                keyboard.release(key)
        return callback


if __name__ == "__main__":
    ZeldaBridgeNode()
