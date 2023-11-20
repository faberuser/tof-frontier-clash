import sys
from os import chdir, getcwd, path
from time import sleep, strftime, gmtime
from random import randint, uniform
from glob import glob
from shutil import rmtree

import pyautogui
from win32gui import FindWindow, GetWindowText, GetForegroundWindow, ShowWindow, SetActiveWindow, SetForegroundWindow

pyautogui.FAILSAFE = False
solo = True

chdir(getcwd())
assets_path = None

try:
    assets_path = sys._MEIPASS + "\\images\\"
    open(sys._MEIPASS + '\\is_tof_frontier_clash', 'a').close()

    base_path = (sys._MEIPASS).split("\\")
    base_path.pop(-1)
    temp_path = ""
    for item in base_path:
        temp_path = temp_path + item + "\\"

    mei_folders = [f for f in glob(temp_path + "**/", recursive=False)]
    for item in mei_folders:
        if item.find('_MEI') != -1 and item != sys._MEIPASS + "\\":
            if path.exists(item + '\\is_tof_frontier_clash'):
                rmtree(item)
except AttributeError:
    assets_path = ".\\images\\"

activate = assets_path + "activate.png"
approve = assets_path + "approve.png"
assist = assets_path + "assist.png"
assist_check = assets_path + "assist-check.png"
auto = assets_path + "auto.png"
enter = assets_path + "enter.png"
challenge = assets_path + "challenge.png"
clock = assets_path + "clock.png"
close = assets_path + "close.png"
close_2 = assets_path + "close_2.png"
frontier_clash = assets_path + "frontier-clash.png"
frontier_clash_completed = assets_path + "frontier-clash-completed.png"
go = assets_path + "go.png"
match = assets_path + "match.png"
ok = assets_path + "ok.png"
_quit = assets_path + "quit.png"
skip = assets_path + "skip.png"
overworld = assets_path + "overworld.png"


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


def run(stop_when_has_attemps):
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

                    elif is_on_screen(frontier_clash):
                        break

                    elif is_on_screen(frontier_clash_completed):
                        break

                while True:
                    if is_on_screen(frontier_clash):
                        if stop_when_has_attemps:
                            print("Detect attempt(s) available, script terminated.")
                            return
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

                    elif is_on_screen(enter):
                        break

                if solo:
                    while True:
                        if is_on_screen(enter):
                            press_mouse(is_on_screen(enter))
                            print("Clicked Enter")

                        elif not is_on_screen(enter):
                            break

                    while True:
                        if is_on_screen(clock):
                            print("Waiting 10-15s for loading animation")
                            sleep(randint(8, 10))

                            pyautogui.keyDown("w")
                            sleep(2.3)
                            pyautogui.keyUp("w")

                            sleep(uniform(0.5, 1))

                            pyautogui.keyDown("a")
                            sleep(2.4)
                            pyautogui.keyUp("a")

                            sleep(uniform(0.5, 1))
                            break

                    while True:
                        if is_on_screen(activate):
                            for i in range(1, 10):
                                pyautogui.keyDown("f")
                                sleep(randint(1, 2))
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
                        print("Clicked Auto")
                        print("End this loop, waiting to finish for next one")
                        print(
                            f"Currently did [{str(runs + 1)}] runs including this.\n")
                        sleep(randint(240, 270))
                        break

        except KeyboardInterrupt:
            print("--------------------------")
            end_time = strftime("%m/%d/%Y-%H:%M:%S", gmtime())
            text = f"[{end_time}] Cancelled, did a total of [{str(runs)}] Frontier Clash runs.\n"
            print(text)
            with open("./results.txt", "a") as f:
                f.write(text)
            break


def main(stop_when_has_attemps):
    print("\nIf the script doesn't do anything after 10 seconds, stop this and rerun as administrator.")
    print("Stop the script with CTRL-C while focusing on this window.\n")
    sleep(10)
    run(stop_when_has_attemps)


if __name__ == "__main__":
    _stop = input(
        "Do you want stop the script when Frontier Clash attempt(s) is available? (Y/N) > ")
    if _stop.lower() == "y":
        main(True)
    elif _stop.lower() == "n":
        main(False)
    else:
        print("Invalid answer, script terminated.")
    input("\nEnter any key to exit")
