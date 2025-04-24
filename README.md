# KHU 금학기 성적 조회 프로그램

이 프로젝트는 **경희대학교 포털 사이트(info21.khu.ac.kr)**에 로그인하여 사용자의 **성적/과목 정보를 자동으로 가져와 GUI로 시각화**해주는 프로그램입니다.  
`Selenium`, `BeautifulSoup`, `Tkinter`를 사용하여 구현되었습니다.

## 기술 스택

- Python 3.x
- Selenium
- BeautifulSoup
- Tkinter (GUI)
- ChromeDriver

---

## 파일 구조

```
📁 NoMoreInfo/
└── main.py        # 메인 실행 파일 (tkinter 기반 GUI 포함)
```

---

## 실행 방법

1. **크롬 드라이버 설치**

    ChromeDriver에서 현재 사용하는 크롬 버전에 맞는 드라이버를 받아 설치하세요.  
    받은 드라이버 경로를 `main.py`의 `driver_path` 변수에 지정해야 합니다.

2. **필수 패키지 설치**

    ```bash
    pip install selenium beautifulsoup4
    ```

3. **프로그램 실행**

    ```bash
    python main.py
    ```

## 주요 기능

- **GUI 기반 로그인**: Tkinter로 구성된 UI에서 경희대학교 포털 ID/PW 입력
- **자동 로그인 및 크롤링**: Selenium을 이용한 자동화된 로그인 및 성적 데이터 추출
- **성적 데이터 테이블화**: BeautifulSoup으로 파싱 후 Tkinter TreeView에 표시
- **Headless 모드 지원**: 백그라운드에서 크롬 실행 가능 (시각적 창 없음)

---

## 주의사항

- 경희대학교 포털 시스템 구조나 로그인 방식이 변경되면 작동하지 않을 수 있습니다.
- Chrome 브라우저와 ChromeDriver 버전은 일치해야 합니다.

---

- 로그인 실패 시 사용자에게 GUI 팝업으로 에러 안내
- 수집된 성적 데이터를 CSV 또는 Excel로 저장
- 교과목 필터링 및 정렬 기능 추가
- 로그인 세션 유지 기능# NoMoreInfo
