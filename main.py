import pyautogui   #  firrst we pyautogui laibrary
import time
import pyperclip


pyautogui.click(963,767) # go on the whatsapp and click it to opened
pyautogui.click()
time.sleep(1)


def is_last_message_from_meta_ai(message: str) -> bool:
    lines = [line for line in message.strip().split('\n') if '] ' in line]
    if not lines: return False
    last_sender = lines[-1].split('] ')[-1].split(':')[0].strip()
    return last_sender == "Meta AI"


while True:
    pyautogui.moveTo(1354,174)
    pyautogui.dragTo(1328,690,duration=1.0,button='left')

    pyautogui.hotkey('ctrl','c')
    pyautogui.click(1320,586)
    time.sleep(1)

    text=pyperclip.paste()
    if(is_last_message_from_meta_ai(text)):

        print(text)

        a=""
        try: 
            from openai import OpenAI
            client=OpenAI(
                api_key="",
            )

            completion=client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role":"system","content":"You are a person named Om who speaks hindi as well as english. You are from India and you are a coder. Please analyze chat history and make next response and respond like Om"},
                    {"role":"user","content":text}
                ]
            )

            response=completion.choices[0].message.content
            a=pyperclip.copy(response)

        except Exception as e:
            print("Open AI can not be worked now..... Try after some time")


        message="I am Om's Chatbot...Sorry Om is not available now"
        if(a==""):
            pyperclip.copy(message)

        pyautogui.click(980,725)
        time.sleep(1)

        pyautogui.hotkey('ctrl','v')
        time.sleep(0.5)

        pyautogui.hotkey('enter')

        time.sleep(5)
