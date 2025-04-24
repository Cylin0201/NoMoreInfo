from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

# 크롬 드라이버 경로
driver_path = "/usr/local/bin/chromedriver/chromedriver" 

# tkinter로 UI 만들기
root = tk.Tk()
root.title("KHU 과목 목록")
root.geometry("1280x720")

# 폰트 설정 (크기를 14로 키움)
font = Font(family="맑은 고딕", size=14)

# 아이디와 비밀번호 입력을 위한 레이블 및 입력 필드 추가
label_id = tk.Label(root, text="아이디:", font=font)
label_id.pack(pady=10)
entry_id = tk.Entry(root, font=font)
entry_id.pack(pady=10)

label_pw = tk.Label(root, text="비밀번호:", font=font)
label_pw.pack(pady=10)
entry_pw = tk.Entry(root, font=font, show="*")
entry_pw.pack(pady=10)

# 로그인 버튼 클릭시 실행될 함수 정의
def login():
    user_id = entry_id.get()  # 사용자 아이디
    user_pw = entry_pw.get()  # 사용자 비밀번호
    
    # 크롬 드라이버 설정
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

    # 로그인 절차
    try:
        login_url = "https://info21.khu.ac.kr/com/LoginCtr/login.do?sso=ok"  # 로그인 페이지 URL
        driver.get(login_url)

        user_id_field = driver.find_element(By.ID, "userId")  
        user_id_field.send_keys(user_id)  # 아이디 입력

        password_field = driver.find_element(By.ID, "userPw") 
        password_field.send_keys(user_pw)  # 비밀번호 입력

        login_button = driver.find_element(By.CSS_SELECTOR, ".btn.loginbtn1")
        login_button.click()

        print("로그인 성공!")
        time.sleep(1)

        # 로그인 후 성적 페이지로 이동
        target_url = "https://portal.khu.ac.kr/haksa/clss/scre/tyScre/index.do"
        driver.get(target_url)

        close_button = driver.find_element(By.CLASS_NAME, "ui-dialog-titlebar-close")
        close_button.click()

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        xpath = '//*[@id="cont1"]/div[2]/table/tbody'
        tbody_element = driver.find_element(By.XPATH, xpath)
        rows = tbody_element.find_elements(By.TAG_NAME, 'tr')

        data = []

        for row in rows:
            cols = row.find_elements(By.TAG_NAME, 'td')

            course_name = cols[0].text.strip() 
            course_type = cols[1].text.strip()  
            credits = cols[2].text.strip()  
            grade = cols[5].text.strip()  

            data.append([course_name, course_type, credits, grade])

        # 로그인 창을 숨기고 성적 화면을 표시
        root.withdraw()  # 로그인 창 숨기기

        # 성적을 표시할 새로운 창 생성
        result_window = tk.Tk()
        result_window.title("성적 목록")
        result_window.geometry("1280x720")

        tree = ttk.Treeview(result_window, columns=("Course", "Type", "Credits", "Grade"), show="headings")
        tree.heading("Course", text="교과목")
        tree.heading("Type", text="이수구분")
        tree.heading("Credits", text="학점")
        tree.heading("Grade", text="등급")

        # 테이블의 폰트 크기 적용
        tree.tag_configure('big', font=font)
        tree.pack(expand=True, fill=tk.BOTH)

        # 성적 데이터 표시
        for row in data:
            tree.insert("", tk.END, values=row)

        # 성적 창이 닫힐 때 root.quit() 호출
        result_window.protocol("WM_DELETE_WINDOW", lambda: (result_window.quit(), root.quit()))

        result_window.mainloop()  # 성적 창 실행

    except Exception as e:
        print(f"오류 발생: {e}")

    finally:
        driver.quit()

# 로그인 버튼을 클릭했을 때 login 함수 호출
login_button = tk.Button(root, text="로그인", font=font, command=login)
login_button.pack(pady=20)

# 엔터 키로 로그인 호출
entry_pw.bind("<Return>", lambda event: login())  # 비밀번호 입력 후 엔터 키를 누르면 login 함수 실행
entry_id.bind("<Return>", lambda event: login())  # 아이디 입력 후 엔터 키를 누르면 login 함수 실행

root.protocol("WM_DELETE_WINDOW", root.quit)

root.mainloop()
