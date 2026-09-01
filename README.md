![banner](https://raw.githubusercontent.com/ramyasp64/ramyasp64/main/banner.svg)

### Hi, I'm Ramya 👋

I'm an M.S. student in Web and Data Science at Universität Koblenz. I work on **sustainable healthcare robotics**: autonomous robots for patient monitoring in low-resource clinics.

A model that detects a patient deteriorating is only useful if someone is there to act on it. In a ward with one nurse and forty beds, that is often not the case. So I build both parts: the model that detects the problem, and the robot that responds to it.

**[MediSense](https://github.com/ramyasp64/MediSense)** is the detection side. It tests whether a model trained on industrial sensor degradation can transfer to clinical vital signs monitoring. **[MediSense-Rover](https://github.com/ramyasp64/MediSense-Rover)** is the response side. It is a ROS 2 robot that maps a ward, tracks its own position, and drives to the bedside on its own when an alert is raised.

My path into this started with my university's R&D research internship, where I worked on 3D point cloud anomaly detection for manufacturing quality control. That project is what made the connection clear: the way industrial sensors degrade and the way vital signs deteriorate follow surprisingly similar patterns. That observation became MediSense.

Before the Master's, I spent two years at Kumaran Systems as an ETL Developer, building and owning pipelines for CIBC's Wholesale Credit Data Warehouse (one of Canada's Big Five banks). 300+ tables, billions of records, 7 pipelines built from scratch, 75+ requirements delivered with zero escalations. I'm grateful for that experience. It taught me what it really means to own something.

I'm looking for a **paid research or thesis position** in robotics, physical AI, healthcare robotics, or applied ML.

---

### 🔬 What I'm working on

**[MediSense-Rover](https://github.com/ramyasp64/MediSense-Rover)**: an autonomous monitoring and response robot for clinical wards, built in ROS 2 Jazzy with SLAM and Nav2. A recorded ICU waveform at 163 BPM raises a clinical alert, and the robot drives itself to that bed, arriving within 0.17 m.

**[MediSense](https://github.com/ramyasp64/MediSense)**: research on transfer learning from industrial sensors to clinical vital signs monitoring. This is the model the rover carries.

---

### 🛠 Skills

**Robotics and Physical AI**  
![ROS 2](https://img.shields.io/badge/ROS%202%20Jazzy-22314E?style=flat-square&logo=ros&logoColor=white)
![Gazebo](https://img.shields.io/badge/Gazebo%20Harmonic-FF6C37?style=flat-square)
![Nav2](https://img.shields.io/badge/Nav2-Navigation%20Stack-2E7D32?style=flat-square)
![SLAM](https://img.shields.io/badge/SLAM-slam__toolbox-1565C0?style=flat-square)
![URDF](https://img.shields.io/badge/URDF%20%2F%20SDF-Robot%20Description-546E7A?style=flat-square)
![TF2](https://img.shields.io/badge/TF2-Transforms-455A64?style=flat-square)
![rclpy](https://img.shields.io/badge/rclpy-3776AB?style=flat-square&logo=python&logoColor=white)
![micro-ROS](https://img.shields.io/badge/micro--ROS-Embedded-8E24AA?style=flat-square)

**AI and Machine Learning**  
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)

**Signal Processing and Computer Vision**  
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=flat-square&logo=scipy&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Open3D](https://img.shields.io/badge/Open3D-3D%20Vision-darkgreen?style=flat-square)

**MLOps and Deployment**  
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)

**Data Engineering**  
![Oracle](https://img.shields.io/badge/Oracle-F80000?style=flat-square&logo=oracle&logoColor=white)
![SQL](https://img.shields.io/badge/PL%2FSQL-4479A1?style=flat-square&logo=postgresql&logoColor=white)
![Informatica](https://img.shields.io/badge/Informatica-FF6D00?style=flat-square)

**Cloud and Analytics**  
![Azure](https://img.shields.io/badge/Azure-0078D4?style=flat-square&logo=microsoft-azure&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazon-aws&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)
![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=flat-square&logo=databricks&logoColor=white)

---

### 📂 Projects

**🤖 [MediSense-Rover: An Autonomous Monitoring and Response Robot](https://github.com/ramyasp64/MediSense-Rover)**  
*Independent research · ROS 2 Jazzy · 2026*

This robot maps a four-bed ward using SLAM, tracks its own position with AMCL, and plans its own route with Nav2. When a patient's waveform produces a sustained red alert, it drives to that bedside without anyone controlling it.

Built entirely in simulation with no hardware purchased, which is the same budget constraint the intended deployment has. It carries the MediSense model unmodified, mounted read-only, and adds the perception, decision and action loop around it.

All figures are measured against the simulator's ground truth rather than the robot's own reports: **0.17 m** arrival accuracy, **16 s** from alert to bedside, and **zero** recovery behaviours. SLAM closes a full ward lap to within **1 mm and 25 mm**. Inference runs at **p99 61 to 70 ms** against a 100 ms budget, on **16,530 parameters and 64.6 KiB of weights**, using **0.05% of one CPU core**.

Two independent detectors run side by side and the more severe result wins. One is a learned autoencoder for equipment faults, the other is a set of clinical vital-sign rules that cannot miss a heart rate of 163. Every alert records which detector fired, so the decision can be audited. The README also states which of the two is currently weak, and why.

`ROS 2 Jazzy` · `Gazebo Harmonic` · `Nav2` · `slam_toolbox` · `TF2` · `URDF/SDF` · `rclpy` · `PyTorch` · `Docker`

---

**🩺 [MediSense: Vital Signs Monitoring via Transfer Learning](https://github.com/ramyasp64/MediSense)**  
*Independent research · 2025 onwards*

Can anomaly representations learned from industrial sensor data transfer to clinical vital signs monitoring? That's the question MediSense is built around. The practical case: in low-resource settings, continuous vital signs monitoring fails not because of hardware but because of the lack of labelled medical training data. Industrial run-to-failure datasets are large, public, and fully annotated. Medical waveforms are not.

- Dual-model pipeline: 1D-CNN Autoencoder on raw 1250-sample windows and a Feature-Based Autoencoder on 17 hand-crafted statistical, frequency, and peak features
- Signal pipeline: Butterworth bandpass, baseline wander removal, Kalman smoothing
- Dual-level alert engine: Level 1 isolates sensor malfunction before Level 2 flags patient deterioration, preventing false alarms from a disconnected probe triggering a cardiac alert
- Performance targets: 90% patient anomaly detection, 95% sensor malfunction detection, under 100ms inference per window
- Validation: McNemar's test (p < 0.05) and a data efficiency experiment to quantify how much less labelled medical data is needed
- Datasets: BIDMC Waveform, CapnoBase, MIMIC-III (medical); NASA Bearing, CMAPSS, SKAB (industrial pre-training)

`PyTorch` `SciPy` `Transfer Learning` `1D-CNN` `Autoencoders` `Clinical AI`

---

**🔧 [3D Point Cloud Anomaly Detection and Registration](https://github.com/ramyasp64/pointcloud-anomaly-detection)**  
*R&D Research Internship · Universität Koblenz · Completed Mar 2026*

Built a fully automated pipeline for aligning 3D scan data against CAD reference models and classifying surface defects, with no manual steps after setup. The cluster-first detection approach evaluates spatially coherent point groups against physical criteria rather than classifying noisy individual points, which is what kept false positives low.

- RANSAC global registration followed by Point-to-Plane ICP refinement: RMSE as low as 0.38 mm
- DBSCAN clustering evaluated against size, deviation, spatial extent, and consistency
- **93-95% classification accuracy** across 6 independent industrial datasets
- JSON-based metadata caching for deterministic, near-instant re-runs

`Python` `Open3D` `RANSAC` `ICP` `DBSCAN` `NumPy` `SciPy`

---

**🗑 [Waste Classifier API](https://github.com/ramyasp64/waste-classifier-api)**  
*Production ML API · Completed Jun 2025*

End-to-end ML project from data to a deployed Kubernetes service. I wanted to take one model the whole distance, training through to serving, instead of stopping at a notebook.

- 6-class CNN (3 Conv2D + MaxPooling layers), trained on Kaggle Garbage Classification dataset with 80/20 split, 30 epochs, batch size 32
- ~90% validation accuracy with Adam optimizer and categorical cross-entropy loss
- FastAPI REST API served with Uvicorn, Dockerised (2.47 GB image), deployed on Kubernetes NodePort (port 30080)
- Confidence scores per class (e.g. `plastic: 0.75`), Swagger testing, full inference pipeline

`TensorFlow` `FastAPI` `Docker` `Kubernetes` `CNNs`

---

**📊 [REWE Retail Intelligence](https://github.com/ramyasp64/rewe-retail-intelligence)**  
*Business Intelligence · Completed Jun 2025*

Retail analytics for REWE Group covering loyalty programs, regional organic sales, competitor pricing, and seasonal trends, built in Power BI with dynamic dashboards.

- Loyalty members average 1,953 EUR vs. 1,809 EUR for non-members: 8% higher spend
- Organic sales peak March to June; Munich and Berlin lead nationally across 5+ German regions
- Lidl holds the lowest prices across all categories: benchmarking opportunity identified for REWE
- 3 product categories analysed; interactive slicers, filled maps, combo charts, and drilldowns

`Power BI` `DAX` `Microsoft Excel` `Data Modeling`

---

**🌀 [Storm Prediction Dashboard](https://github.com/ramyasp64/storm-prediction-dashboard)**  
*Solartis Hackathon · Dec 2020 to Jan 2021*

Real-time geospatial storm risk tool built for insurance underwriting decisions during a hackathon.

- Interactive storm trajectory maps with Folium (Leaflet.js)
- Automated state-wise PDF risk reports generated with FPDF, dispatched via SMTP with StartTLS
- JSON/CSV ingestion with modular SQL filtering for regional analysis

`Python` `Folium` `MySQL` `FPDF` `SMTP`

---

**🤝 [Contactless Donation and Tax Receipt Tracker](https://github.com/ramyasp64/contactless-donation-tracker)**  
*Opportunity Hack 2020 · 3rd Place · Organised by PayPal*

Our nonprofit partner was Dress for Success San Jose, an organisation that helps women re-enter the workforce. Their problem: donors had to fill out paper tax receipts on-site. Enough friction that some turned around at the door.

We built a WordPress plugin over a weekend. Donors submit a request online before drop-off, get a tracking tag, and download their approved PDF receipt from their account. Staff handle approvals from the backend. No paper, no wait.

> *"Having an online tax receipt will enable donors to drop off faster and increase our community support."*

Delivered 100% of the nonprofit's stated requirements, plus tracking and approval capabilities they had not asked for.

`PHP` `WordPress` `TCPDF` `MySQL` `HTML/CSS`

---

**🚕 [Fiddle Tour: Fraudulent Taxi Detection (AdaBoost and XGBoost)](https://github.com/ramyasp64/fiddle-tour-adaboost-xgboost)**  
*B.Tech Thesis · Completed Jun 2022*

Full fraud detection system for real-world metered and unmetered taxi trips, predicting overcharging from distance and price features. Compared AdaBoost vs. XGBoost across accuracy, precision, recall, F1-score, Cohen's Kappa, and execution time. Includes a real-time Tkinter GUI for trip input and fraud verdict.

`Python` `Scikit-learn` `XGBoost` `AdaBoost` `Pandas` `NumPy`

---

**📄 [Fiddle Tour: Fraudulent Taxi Detection (KNN)](https://github.com/ramyasp64/fiddle-tour-knn)**  
*Mini Project · National Engineering College · Feb 2022 · Published · Conference Presented*

KNN-based classifier replacing a map-matching baseline for unmetered taxi fraud detection. Published in the International Journal of Novel Research and Development (Jan 2024) and presented at the ICADSIS International Virtual Conference (May 2022). Repository includes the full project report, published paper, and presentation slides.

`Python` `KNN` `Scikit-learn` `NLTK` `Pickle` `Tkinter`

---

### 🎓 Education

**M.S. Web and Data Science** · Universität Koblenz, Germany · 2024 to present  
Machine Learning, Data Engineering, AI Methods, Computer Vision, Web Technologies

**B.Tech. Information Technology** · National Engineering College, India · 2018 to 2022  
First-Class Distinction · CGPA 8.65/10 · Published research · Presented at ICADSIS International Conference

---

### 📜 Certifications and Recognition

| | |
|--|--|
| 🏅 | Microsoft Certified: Fabric Analytics Engineer Associate (Jun 2024) |
| ☁️ | Microsoft Certified: Azure AI Fundamentals AI-900 (Aug 2023) |
| ☁️ | Microsoft Certified: Azure Fundamentals AZ-900 (Jan 2023) |
| 📦 | Databricks Accredited Lakehouse Fundamentals (May 2023) |
| 🗄️ | Oracle SQL Certification, Udemy (Feb 2023) |
| 🏆 | Go Extra Mile Award, Kumaran Systems Q2 2023: 90% query improvement, zero escalations across 2+ years |
| 🎤 | Certificate of Appreciation, Speaker, ETL Development Webinar Series, NEC Alumni Association (Apr 2024) |
| 📝 | Published: "Fiddle Tour: Detection of Fraudulent Taxi Trips using KNN", IJDRD, Jan 2024 |
| 🎤 | Presented: ICADSIS International Virtual Conference on Advances in Digital Transformation, May 2022 |

---

*Vital signs monitoring for low-resource settings is not just possible. It is achievable.*

*Exploring the intersection of AI, robotics, and accessible healthcare.*

![footer](https://raw.githubusercontent.com/ramyasp64/ramyasp64/main/footer.svg)
