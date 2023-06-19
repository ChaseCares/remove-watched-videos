import time
import pyautogui


def mouseClick():
    pyautogui.mouseDown()
    pyautogui.mouseUp()


def locRegion(image, left, top, width, height):
    return pyautogui.locateCenterOnScreen(image, grayscale=True, confidence=0.9, region=(left, top, width, height))


def loc(image):
    return pyautogui.locateCenterOnScreen(image, grayscale=True, confidence=0.9)


def locateAndMove(image):
    pyautogui.moveTo(pyautogui.locateCenterOnScreen(image))


def locateAndClickRegion(image, left, top, width, height):
    x, y = locRegion(image, left, top, width, height)
    pyautogui.moveTo(x, y)
    time.sleep(0.1)
    mouseClick()
    time.sleep(0.2)


def locateAndClick(image):
    x, y = loc(image)
    pyautogui.moveTo(x, y)
    time.sleep(0.1)
    mouseClick()
    time.sleep(0.2)

# 370x 260y


def removeWatchedVideos():
    try:
        left, top, width, height = pyautogui.locateOnScreen('./img/watched_bar1.png', region=(0, 0, 2560, 1300))
    except Exception as e:
        print(e)
        return False

    # search for everything within this box
    left = left
    top = top-200
    width = width + 350
    height = height + 260

    pyautogui.moveTo(left+100, top+250)
    time.sleep(1)
    locateAndClickRegion('./img/triple_dots.png', left, top, width, height)
    locateAndClick('./img/not_interested.png')
    locateAndClickRegion('./img/tell_us_why.png', left, top, width, height)
    locateAndClick('./img/ive_already.png')
    locateAndClick('./img/submit.png')
    return True


def removeMix():
    try:
        left, top, width, height = pyautogui.locateOnScreen('./img/mix.png', region=(0, 0, 2560, 1300))
    except Exception as e:
        print(e)
        return False

    # search for everything within this box
    left = left
    top = top-200
    width = width + 350
    height = height + 260

    pyautogui.moveTo(left+100, top+100)
    time.sleep(1)
    locateAndClickRegion('./img/triple_dots.png', left, top, width, height)
    locateAndClick('./img/not_interested.png')
    return True


def main():
    time.sleep(1)

    # image = pyautogui.screenshot(region=(0, 0, 2560, 1300))
    # image.save('./screenshot.png')

    timeout = 20
    while timeout > 0:
        # removeMix()
        # removeMix()
        time.sleep(0.4)
        print('Searching for watched videos')
        if not removeWatchedVideos():
            print('No watched videos found')
            pyautogui.scroll(-1500)
            timeout -= 1


if __name__ == "__main__":
    main()
