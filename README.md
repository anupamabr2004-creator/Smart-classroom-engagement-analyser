#  Smart Classroom Attention & Engagement Analyzer

A real-time **Computer Vision-based system** that analyzes student attention levels in a classroom using webcam video feed.  
This project goes beyond traditional attendance systems by introducing **behavior-based engagement analysis**.

---

##  Overview

In modern classrooms, especially large or hybrid environments, it is difficult for instructors to continuously monitor student engagement.

This project addresses that challenge by using **Computer Vision techniques** to:

- Detect faces in real-time
- Estimate attention levels based on head orientation
- Identify distracted behavior
- Compute overall class engagement score
- Log attention data for analysis

---

##  Problem Statement

Traditional attendance systems only capture presence, not engagement.  
There is no automated way to measure whether students are attentive, distracted, or disengaged during lectures.

This project aims to provide a **real-time, automated attention monitoring system** using vision-based analysis.

---

##  Key Features

- Real-time webcam-based analysis
- Multi-face detection using MediaPipe
- Head direction-based attention estimation
- Dynamic attention scoring per student
- Overall classroom engagement score
- Automatic logging of attention data (CSV)

---
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/eb98b1eb-7317-46b6-999b-18e30a0907f4" />
## System Architecture
Video Input (Webcam)
↓
Frame Processing (OpenCV)
↓
Face Detection (MediaPipe)
↓
Head Direction Analysis
↓
Attention Scoring
↓
Class Engagement Calculation
↓
CSV Logging + Live Display

---

##  Tech Stack

| Component | Technology |
|----------|-----------|
| Programming Language | Python |
| Computer Vision | OpenCV |
| Face Detection | MediaPipe |
| Data Processing | NumPy, Pandas |
| Logging | CSV |

---

##  Project Structure
smart-classroom-engagement-analyzer/
│
├── src/
│ ├── main.py # Main execution file
│ ├── detector.py # Face + attention detection logic
│ ├── scorer.py # Attention score calculation
│ ├── logger.py # CSV logging system
│
├── attention_log.csv # Generated during execution
├── requirements.txt # Dependencies
├── README.md
└── .gitignore

---

##  Installation & Setup

### 1. Clone the Repository

```bash
git clone <your-repo-link>
cd smart-classroom-engagement-analyzer

2️⃣ Create Virtual Environment (Recommended)
```bash
python -m venv venv
Activate:

Windows
```bash
venv\Scripts\activate

Mac/Linux
```bash
source venv/bin/activate

3️⃣ Install Dependencies
```bash
pip install -r requirements.txt

▶️ Running the Project
```bash
cd src
python main.py

Press q to exit.

Output

The system displays:

Student-wise attention status:
Focused
Slightly Distracted
Distracted
Class-level attention score (average)
Real-time visual overlay on video feed
CSV file (attention_log.csv) containing:
timestamp
class attention score

Attention Scoring Logic

Attention is estimated based on head orientation:

Looking forward → High score (Focused)
Slight deviation → Medium score
Looking away → Low score (Distracted)

Class attention is computed as:

Average of all individual attention scores

Challenges Faced
Ensuring stable face detection in real-time
Handling multiple faces in a single frame
Variations in lighting conditions
Dependency issues (OpenCV, MediaPipe compatibility)

Future Scope
Eye gaze tracking for precise attention detection
Mobile phone usage detection (YOLO)
Interactive dashboard using Streamlit
Classroom engagement heatmaps
Integration with smart classroom systems

During development, dependency conflicts were encountered due to multiple pre-installed packages in the environment.

To ensure smooth execution on any system, a minimal and stable set of dependencies has been defined in `requirements.txt`.

If you face issues:

1. Create a fresh virtual environment
2. Install dependencies using:

```bash
pip install -r requirements.txt


