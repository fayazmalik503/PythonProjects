from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title="*** take Rest",
            message="Rest is best fo health, body also need rest",
            # app_icon = r"C:\Users\92334\PycharmProjects\PythonProjects\example.png",
            timeout = 5)
        time.sleep(5)