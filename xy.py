import numpy as np
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def call_xy(prompt: str):
    url = 'https://xiaoyi.huawei.com/chat/'
    driver = webdriver.Edge()
    driver.get(url)
    # search by class=input-area
    input_area = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'input-area'))
    )

    try:
        # 更换为 "快捷问答模式"
        check = driver.find_element(By.CLASS_NAME, 'selected-action__wrapper')
        check.click()
        time.sleep(0.2)
        quick_answer = driver.find_elements(By.CLASS_NAME, "action-item")
        quick_answer[-1].click()
        time.sleep(0.2)
    except:
        pass

    # 输入内容
    # <textarea data-v-56cf706d="" type="text" rows="1" placeholder="搜索、提问或发个文档给我吧， 支持shift+enter换行" style="height: inherit;"></textarea>
    textarea = input_area.find_element(By.TAG_NAME, 'textarea')
    textarea.send_keys(prompt)
    time.sleep(1)

    # 点击发送按钮 
    buttons = driver.find_elements(By.CLASS_NAME, 'xy-popover-trigger')
    buttons[-1].click()

    # 等待响应并获取响应内容
    time.sleep(30)
    try:
        answer = driver.find_element(By.CLASS_NAME, 'answer-cont').text
    except:
        answer = "ERROR"
    driver.close()
    return answer
    

if __name__ == '__main__':
    # dir = "wildjailbreak.npz"
    # dir = "wildguard_test.npz"
    # dir = "JBV_hate_speech.npz"
    dir = "JBV_bias.npz"
    prompts = np.load(dir, allow_pickle=True)["data"]
    for prompt in prompts:
        try:
            print(f"Prompt: {prompt}")
            response = call_xy(prompt)
            print(f"Response: {response}\n")
            result = {
                "prompt": prompt,
                "response": response
            }
            with open(f"{dir.split('.')[0]}_results.jsonl", "a", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False)
                f.write("\n")
        except KeyboardInterrupt:
            print("Interrupted by user.")
            break
        except Exception as e:
            # rerun
            print(f"Error: {e}")
            continue