![Image](https://github.com/user-attachments/assets/a8eb4fc4-e734-4be4-a115-5a09e0228041)


# 🚲 서울시 공공자전거 재배치 경로 및 스케줄 최적화 시스템
서울시 공공자전거 따릉이의 자전거 재고 불균형 문제를 해결하기 위한 수요 기반 재배치 경로 최적화 서비스입니다. </br>
배송 인력에게 시간대별 권역 내 최적 동선을 안내하여 재배치 효율성과 따릉이 이용 품질 향상을 목표로 합니다.

## 📺 [서비스 데모 영상(v1)](https://drive.google.com/file/d/1N8SdPq4LX2NF92GhWPBNJ8Kl4aYglPzw/view?usp=sharing)
## 📋 [Notion 페이지](https://past-brazil-18f.notion.site/ebd/213ccc61484380119d1fc36d1c146cce)


## 🧠 핵심 기술 스택 및 기능 구성

* 백엔드 및 프론트엔드 담당자: [👾YUNA AN](https://github.com/pompom33) </br>

### ⛏ Backend _(개발중!)_
언어: Python [📁backend](https://github.com/pompom33/ddarawayo/tree/main/backend) </br>
주요 기능:  </br>
* **데이터 파이프라인 구축** : 정적 데이터 로딩 파이프라인 구축 및 서비스 통합
* **외부  API 자동화** : 외부 API 연동 및 응답 파싱 자동화
* **수요 예측 모델 제작** : 대여소 단위 수요 예측 모델 구현 및 입력데이터 생성 자동화
* **재배치 경로 최적화 로직 구현** : ILP 기반 최적화 알고리즘으로 대여소 간 재배치 경로 및 스케줄 자동 계산
* **테스트** : 단위/통합/시스템 테스트 작성

### 🌐 Frontend
_(준비중!)_</br>
주요 기능:</br>
* 사용자로부터 권역, 날짜, 시간대 입력값을 수집하고 서버에 전달
