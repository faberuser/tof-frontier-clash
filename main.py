import pyautogui
from time import sleep, strftime, gmtime
from random import randint, uniform
from win32gui import FindWindow, GetWindowText, GetForegroundWindow, ShowWindow, SetActiveWindow, SetForegroundWindow

pyautogui.FAILSAFE = False

solo = True

activate = "./images/activate.png"
approve = "./images/approve.png"
assist = "./images/assist.png"
assist_check = "./images/assist-check.png"
auto = "./images/auto.png"
enter = "./images/enter.png"
challenge = "./images/challenge.png"
clock = "./images/clock.png"
close = "./images/close.png"
close_2 = "./images/close_2.png"
frontier_clash = "./images/frontier-clash.png"
frontier_clash_completed = "./images/frontier-clash-completed.png"
go = "./images/go.png"
match = "./images/match.png"
ok = "./images/ok.png"
_quit = "./images/quit.png"
skip = "./images/skip.png"
overworld = "./images/overworld.png"


def is_on_screen(img, cutoff=0.7):
    return pyautogui.locateOnScreen(img, confidence=cutoff)


def get_center(coords):
    return (coords[0] + int(coords[2] / 2), coords[1] + int(coords[3] / 2))


def press_mouse(pos, right=False, wait=[0.05, 0.1]):
    pyautogui.moveTo(pos)
    sleep(uniform(wait[0], wait[1]))
    if right == True:
        pyautogui.mouseDown(button="right")
    else:
        pyautogui.mouseDown()
    sleep(uniform(wait[0], wait[1]))
    if right == True:
        pyautogui.mouseUp(button="right")
    else:
        pyautogui.mouseUp()


def run():
    runs = 0
    while True:
        if (GetWindowText(GetForegroundWindow()) != "Tower of Fantasy  "):
            window = FindWindow(0, "Tower of Fantasy  ")
            pyautogui.press("alt")
            try:
                SetForegroundWindow(window)
            except:
                print("Error when setting game to active window, has the game launched?")
                break

        failed = False
        try:
            if is_on_screen(skip):
                # press_mouse(is_on_screen(skip))
                # sleep(uniform(0.5, 1))
                # pyautogui.moveTo(0, 0)
                # sleep(uniform(0.5, 1))
                pass

            elif is_on_screen(close):
                cec = get_center(is_on_screen(close))
                press_mouse((cec[0], cec[1] - 50))
                sleep(uniform(0.5, 1))
                pyautogui.moveTo(0, 0)

            elif is_on_screen(close_2):
                cec = get_center(is_on_screen(close_2))
                press_mouse((cec[0], cec[1] - 50))
                sleep(randint(1, 2))

                count = 0
                while True:
                    if count >= 30:
                        break
                    if is_on_screen(_quit):
                        pyautogui.keyDown("alt")
                        sleep(uniform(0.5, 1))
                        press_mouse(is_on_screen(_quit))
                        sleep(uniform(0.5, 1))
                        pyautogui.keyUp("alt")
                        sleep(randint(1, 2))

                    if is_on_screen(ok, cutoff=0.6):
                        press_mouse(is_on_screen(ok, cutoff=0.6))
                        sleep(randint(10, 15))
                        runs += 1
                        break
                    count += 1

            elif is_on_screen(overworld):
                while True:
                    pyautogui.keyDown("alt")
                    sleep(uniform(0.5, 1))
                    pyautogui.keyDown("3")
                    sleep(uniform(0.5, 1))
                    pyautogui.keyUp("alt")
                    sleep(uniform(0.5, 1))
                    pyautogui.keyUp("3")
                    sleep(randint(1, 2))

                    if is_on_screen(challenge):
                        break

                while True:
                    if is_on_screen(challenge):
                        press_mouse(is_on_screen(challenge))
                        print("Clicked Challenge")
                        sleep(randint(1, 2))
                        break

                while True:
                    if is_on_screen(frontier_clash):
                        press_mouse(is_on_screen(frontier_clash))
                        print("Clicked Frontier Clash")
                        sleep(randint(1, 2))

                    elif is_on_screen(frontier_clash_completed):
                        press_mouse(is_on_screen(
                            frontier_clash_completed))
                        print("Clicked Frontier Clash (Completed)")
                        sleep(randint(1, 2))

                    elif is_on_screen(go):
                        press_mouse(is_on_screen(go))
                        print("Clicked Go")
                        sleep(randint(1, 2))
                        break

                if solo:
                    while True:
                        if is_on_screen(enter):
                            press_mouse(is_on_screen(enter))
                            print("Clicked Enter")
                            break

                    while True:
                        if is_on_screen(clock):
                            print("Waiting 10-15s for loading animation")
                            sleep(randint(8, 10))

                            activated = False
                            pyautogui.keyDown("w")
                            sleep(2.4)
                            pyautogui.keyUp("w")

                            sleep(uniform(0.5, 1))

                            pyautogui.keyDown("a")
                            sleep(2.4)
                            pyautogui.keyUp("a")

                            sleep(uniform(0.5, 1))
                            break

                    while True:
                        if is_on_screen(activate):
                            activated = True
                            pyautogui.keyDown("f")
                            sleep(2)
                            pyautogui.keyUp("f")
                            print("Activated")
                            sleep(randint(5, 10))
                            break

                        if is_on_screen(overworld) or is_on_screen(close):
                            failed = True
                            break

                        pyautogui.keyDown("w")
                        sleep(0.25)
                        pyautogui.keyUp("w")
                        sleep(uniform(0.5, 1))

                else:
                    while True:
                        if is_on_screen(match):
                            press_mouse(is_on_screen(match))
                            print("Clicked Match")
                            print("Waiting for matching")
                            sleep(randint(1, 2))
                            break

                    while True:
                        if is_on_screen(approve):
                            if is_on_screen(assist):
                                press_mouse(
                                    is_on_screen(assist))
                                print("Clicked Assist")
                                sleep(
                                    randint(1, 2))
                                press_mouse(
                                    is_on_screen(approve))
                                print("Clicked Approve")
                                sleep(
                                    randint(1, 2))
                                pyautogui.moveTo(0, 0)
                            elif is_on_screen(assist_check):
                                print(
                                    "No Attempt left, Assists automatically on"
                                )
                                press_mouse(
                                    is_on_screen(approve))
                                print("Clicked Approve")
                                sleep(
                                    randint(1, 2))
                                pyautogui.moveTo(0, 0)

                        elif is_on_screen(clock):
                            wait_count = 0
                            count = 0
                            while True:
                                if is_on_screen(clock) is None:
                                    if wait_count == 0:
                                        wait_count += 1
                                        sleep(7.5)
                                        print(
                                            "Waiting to activate the battle")
                                        continue
                                    elif wait_count == 1:
                                        sleep(11)
                                        break
                                else:
                                    count += 1
                                    sleep(2)
                                    if count >= 30:
                                        break

                while True:
                    if failed:
                        break

                    if is_on_screen(auto, 0.6) and is_on_screen(clock):
                        pyautogui.keyDown("alt")
                        sleep(uniform(0.5, 1))
                        press_mouse(is_on_screen(auto, 0.6))
                        sleep(uniform(0.5, 1))
                        pyautogui.keyUp("alt")
                        print("Clicked Auto, entered the battle")
                        print("End this loop, waiting to finish for next one")
                        print("Currently did " + str(runs + 1) +
                              " runs including this.")
                        sleep(randint(240, 270))
                        break

        except KeyboardInterrupt:
            print("--------------------------")
            text = (
                "["
                + strftime("%m/%d/%Y-%H:%M:%S", gmtime())
                + "] Cancelled, did a total of ["
                + str(runs)
                + "] Frontier Clash runs.\n"
            )
            print(text)
            with open("./results.txt", "a") as f:
                f.write(text)
            break


if __name__ == "__main__":
    print("Script is running, please focus on Game window in 10 seconds.")
    sleep(10)
    run()
