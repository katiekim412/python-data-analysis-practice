# 🏠 서울시 아파트 실거래가 데이터 분석 및 시각화 프로젝트

## 📌 프로젝트 소개
이 프로젝트는 공공데이터포털 API를 활용하여 **서울시 아파트 실거래가 데이터를 수집하고, 데이터 정제 및 분석을 통해 유의미한 인사이트를 도출**하는 것을 목표로 합니다.  
Python과 `pandas`, `seaborn` 등의 라이브러리를 사용하여 데이터 분석의 전 과정을 수행했습니다.  

---

## ✨ 주요 분석 과정 및 특징
- **데이터 수집**
  - 국토교통부 실거래가 정보 API를 활용하여 특정 기간(예: 2020-2024년)의 서울시 아파트 매매 데이터 수집 자동화
- **데이터 전처리 및 정제**
  - 여러 기간에 걸쳐 수집된 데이터를 `pandas`를 사용해 단일 데이터프레임으로 병합
  - 결측치 처리, 데이터 타입 변환 등 데이터 클리닝 수행
- **특성 공학 (Feature Engineering)**
  - '평당 금액', '건축 경과 년수' 등 분석에 필요한 파생 변수 생성
  - 주소 데이터를 기반으로 '구' 단위 지역 정보 추출
- **탐색적 데이터 분석 (EDA) 및 시각화**
  - `matplotlib`와 `seaborn`을 활용하여 데이터 분포 및 변수 간 관계 시각화
  - 거래 가격 분포, 지역별 평균 평당 가격, 건축 년도와 가격의 관계 등 분석

---

## 🛠 기술 스택
- **Python**
- **Libraries**:
  - **Data Handling**: `pandas`, `numpy`
  - **Web Scraping**: `requests`, `xmltodict`, `beautifulsoup4`
  - **Data Visualization**: `matplotlib`, `seaborn`
- **Environment**: Jupyter Notebook

---

## 📂 프로젝트 구조
```

📦 seoul-apt-analysis  
┣ 📂 code               \# Jupyter Notebook 소스 코드  
┃ ┣ 📜 Day1\_Python\_Basics.ipynb  
┃ ┣ 📜 Day3\_Data\_Crawling.ipynb  
┃ ┣ 📜 Day6\_Data\_Preprocessing.ipynb  
┃ ┗ 📜 Day7\_Visualization.ipynb  
┣ 📂 data                \# 수집한 원본 및 가공 데이터 (CSV, Excel)  
┃ ┣ 📜 APT\_Price\_Seoul\_2024.csv  
┃ ┗ 📜 APT\_Detail\_Seoul\_2024.csv  
┗ 📜 README.md          \# 프로젝트 설명 문서  

```

---

## 📸 분석 결과 시각화 예시

- **서울시 자치구별 평당 평균 가격** (막대 그래프)
- **전용 면적과 거래 가격의 관계** (산점도)
- **월별 거래량 추이** (선 그래프)
- **거래 가격 분포** (히스토그램/KDE 플롯)

---

## 💡 학습 포인트
- 공공데이터 API를 활용한 **대용량 데이터 수집 및 자동화 파이프라인 구축 경험**
- `pandas`를 이용한 **데이터 정제 및 가공 능력** 심화
- **시각화 라이브러리(`seaborn`, `matplotlib`)를 활용**하여 데이터의 특징을 효과적으로 전달하는 능력 배양
- 데이터 분석 프로젝트의 **전체 프로세스를 처음부터 끝까지 주도적으로 수행**한 경험

---

## 📌 향후 개선 아이디어
- 📈 **예측 모델링**: 수집한 데이터를 기반으로 선형 회귀, 트리 기반 모델 등을 사용하여 아파트 가격 예측 모델 개발
- 🌐 **인터랙티브 대시보드**: `Streamlit`이나 `Dash`를 활용하여 사용자가 직접 조건을 설정하며 분석 결과를 살펴볼 수 있는 웹 대시보드 구축
- 🗺️ **지리 정보 시각화**: `folium` 라이브러리를 활용하여 지도 위에 아파트 가격 정보를 시각화
### 👤 Author
- **이름**: 김태영
- **역할**: 클라우드 엔지니어 & 데이터 분석 학습자
- **Contact**: katiekim412@gmail.com | [LinkedIn](http.www.linkedin.com/in/katiekim412)
---
```
