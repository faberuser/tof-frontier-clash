import pyautogui, time, random

pyautogui.FAILSAFE = False

adventure = "./images/adventure.png"
approve = "./images/approve.png"
assist = "./images/assist.png"
assist_check = "./images/assist-check.png"
auto = "./images/auto.png"
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
bygone = "./images/bygone.png"
training = "./images/training.png"


def is_on_screen(img, cutoff=0.7):
    return pyautogui.locateOnScreen(img, confidence=cutoff)


def get_center(coords):
    return (coords[0] + int(coords[2] / 2), coords[1] + int(coords[3] / 2))


def press_mouse(pos, right=False):
    pyautogui.moveTo(pos)
    time.sleep(random.uniform(0.05, 0.1))
    if right == True:
        pyautogui.mouseDown(button="right")
    else:
        pyautogui.mouseDown()
    time.sleep(random.uniform(0.05, 0.1))
    if right == True:
        pyautogui.mouseUp(button="right")
    else:
        pyautogui.mouseUp()


def run():
    runs = 0
    while True:
        try:
            if is_on_screen(skip):
                press_mouse(is_on_screen(skip))
                time.sleep(random.uniform(0.5, 1))
                pyautogui.moveTo(0, 0)

            elif is_on_screen(close):
                cec = get_center(is_on_screen(close))
                press_mouse((cec[0], cec[1] - 50))
                time.sleep(random.uniform(0.5, 1))
                pyautogui.moveTo(0, 0)

            elif is_on_screen(close_2):
                cec = get_center(is_on_screen(close_2))
                press_mouse((cec[0], cec[1] - 50))
                time.sleep(random.randint(2, 3))

                count = 0
                while True:
                    if count >= 30:
                        break
                    if is_on_screen(_quit):
                        pyautogui.keyDown("alt")
                        time.sleep(random.uniform(0.5, 1))
                        press_mouse(is_on_screen(_quit))
                        time.sleep(random.uniform(0.5, 1))
                        pyautogui.keyUp("alt")
                        time.sleep(random.randint(1, 2))

                    if is_on_screen(ok):
                        press_mouse(is_on_screen(ok))
                        time.sleep(random.randint(10, 15))
                        runs += 1
                        break
                    count += 1

            elif is_on_screen(clock) is None:
                pyautogui.keyDown("alt")
                time.sleep(random.uniform(0.5, 1))
                pyautogui.keyDown("3")
                time.sleep(random.uniform(0.5, 1))
                pyautogui.keyUp("alt")
                time.sleep(random.uniform(0.5, 1))
                pyautogui.keyUp("3")
                time.sleep(random.randint(1, 2))
                if is_on_screen(adventure):
                    print("Entered Adventure")
                    time.sleep(random.randint(2, 3))
                else:
                    continue

                while True:
                    if is_on_screen(challenge):
                        press_mouse(is_on_screen(challenge))
                        print("Clicked Challenge")
                        time.sleep(random.randint(1, 2))

                        not_fc_count = 0
                        while True:
                            if not_fc_count >= 10:
                                pyautogui.moveTo(is_on_screen(bygone))
                                pyautogui.mouseDown(button="left")
                                pyautogui.moveTo(is_on_screen(training), duration=1)
                                pyautogui.mouseUp(button="left")
                                not_fc_count = 0

                            elif is_on_screen(frontier_clash):
                                while True:
                                    if is_on_screen(frontier_clash):
                                        fc = get_center(is_on_screen(frontier_clash))
                                        press_mouse((fc[0], fc[1] + 379))
                                        print("Clicked Frontier Clash")
                                        time.sleep(random.randint(2, 3))

                                    # elif is_on_screen(frontier_clash_completed):
                                    #     fc = get_center(is_on_screen(frontier_clash_completed))
                                    #     press_mouse((fc[0], fc[1] + 379))
                                    #     print("Clicked Frontier Clash (Completed)")
                                    #     time.sleep(random.randint(2, 3))

                                    elif is_on_screen(go):
                                        press_mouse(is_on_screen(go))
                                        print("Clicked Go")
                                        time.sleep(random.randint(1, 2))

                                    elif is_on_screen(match):
                                        press_mouse(is_on_screen(match))
                                        print("Clicked Match")
                                        print("Waiting for matching")
                                        time.sleep(random.randint(2, 3))

                                        while True:
                                            if is_on_screen(approve):
                                                if is_on_screen(assist):
                                                    press_mouse(is_on_screen(assist))
                                                    print("Clicked Assist")
                                                    time.sleep(random.randint(1, 2))
                                                    press_mouse(is_on_screen(approve))
                                                    print("Clicked Approve")
                                                    time.sleep(random.randint(1, 2))
                                                    pyautogui.moveTo(0, 0)
                                                elif is_on_screen(assist_check):
                                                    print(
                                                        "No Attempt left, Assists automatically on"
                                                    )
                                                    press_mouse(is_on_screen(approve))
                                                    print("Clicked Approve")
                                                    time.sleep(random.randint(1, 2))
                                                    pyautogui.moveTo(0, 0)

                                            elif is_on_screen(clock):
                                                wait_count = 0
                                                count = 0
                                                while True:
                                                    if is_on_screen(clock) is None:
                                                        if wait_count == 0:
                                                            wait_count += 1
                                                            time.sleep(7.5)
                                                            print(
                                                                "Waiting to activate the battle"
                                                            )
                                                            continue
                                                        elif wait_count == 1:
                                                            time.sleep(11)
                                                            break
                                                    else:
                                                        count += 1
                                                        time.sleep(2)
                                                        if count >= 30:
                                                            break
                                                while True:
                                                    if is_on_screen(
                                                        auto, 0.6
                                                    ) and is_on_screen(clock):
                                                        pyautogui.keyDown("alt")
                                                        time.sleep(
                                                            random.uniform(0.5, 1)
                                                        )
                                                        press_mouse(
                                                            is_on_screen(auto, 0.6)
                                                        )
                                                        time.sleep(
                                                            random.uniform(0.5, 1)
                                                        )
                                                        pyautogui.keyUp("alt")
                                                        print(
                                                            "Clicked Auto, entered the battle"
                                                        )
                                                        print(
                                                            "End this loop, waiting to finish for next one"
                                                        )
                                                        print(
                                                            "Currently did "
                                                            + str(runs + 1)
                                                            + " runs including this."
                                                        )
                                                        time.sleep(
                                                            random.randint(420, 450)
                                                        )
                                                        break
                                                break
                                        break
                                break

                            elif not is_on_screen(frontier_clash):
                                not_fc_count += 1
                        break

        except KeyboardInterrupt:
            print("--------------------------")
            text = (
                "["
                + time.strftime("%m/%d/%Y-%H:%M:%S", time.gmtime())
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
    time.sleep(10)
    run()
