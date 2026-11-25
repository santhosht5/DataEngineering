# Data Engineering for Computer Vision & Video Analytics

A hands-on learning repository focused on data engineering pipelines, data curation, temporal synchronization, and preprocessing for computer vision and video understanding models.

---

## 📁 Repository Structure

```text
DataEngineeringLearning/
├── Annotation_Videos/          # Sample annotated videos (tennis, cricket)
├── day01/                     # Annotation Manifests & Filtering
│   ├── runs/                  # Versioned manifest runs (v1, v2, v3)
│   ├── ai-log.md
│   ├── export_manifest.py
│   └── rows.txt
├── day02/                     # Temporal Alignment & Clock Synchronization
│   ├── align_clocks.py        # Timestamp-to-frame indexing with clock offsets
│   ├── make_video.py          # Synthetic test video generation
│   ├── contact_sheet.png      # Comparison of naive vs corrected frames
│   └── time_offset.csv        # Offset calibration logs
├── day03/                     # Spatial Matching & IoU Evaluation
│   ├── iou.py                 # Intersection over Union (IoU) implementation
│   ├── match_status.py        # Box matching against ground truth / player boxes
│   ├── reload_yolo.py         # YOLO annotation parsing & validation
│   └── labels/                # Sample YOLO bounding box labels
├── day04/                     # Leak-Free Dataset Splitting
│   ├── split_sources.py       # Group-level train/validation split by video source ID
│   ├── split_frames.py        # Frame-level validation to prevent temporal leakage
│   ├── split.json             # Source assignment metadata
│   └── leaky_frames.json      # Leak detection report
├── day05/                     # Multi-Channel Tensor Stacking & Auditing
│   ├── stack_channels.py      # 12-channel tensor construction (RGB + mask channels)
│   ├── exit_ticket.md         # Rally Cam project specifications & audit metrics
│   ├── audit.csv              # Quality audit checklist
│   └── sample12.tif           # Multi-page TIFF of stacked tensor channels
├── .gitignore
└── README.md
```

---

## 🚀 Daily Modules Overview

### **Day 01: Annotation Manifests & Filtering**
- Manifest schema design for video annotation events (`matched`, `no_positive`, `unmatched`, `no_box`, `outside_window`).
- Filtering logic to separate trainable vs rejected samples.
- Dataset versioning (`runs/v1`, `v2`, `v3`) with sample catalogs and YAML configuration.

### **Day 02: Temporal Clock Alignment**
- Solved annotation clock drift by calculating temporal offsets ($t_{frame} = (t_{ann} + \Delta t) \times \text{FPS}$).
- Extracted and compared naive vs. offset-corrected video frames.
- Automated generation of visual verification contact sheets using OpenCV.

### **Day 03: Spatial Matching & IoU**
- Implemented 2D Intersection over Union (IoU) calculation from bounding box coordinates.
- Set matching thresholds ($\text{IoU} \ge 0.5$) to correlate candidate detections with ground-truth player boxes.
- Parsing and reloading YOLO annotation format (`<class> <x_center> <y_center> <width> <height>`).

### **Day 04: Preventing Temporal Data Leakage**
- Engineered dataset split pipelines grouped strictly by video source ID instead of random frame shuffling.
- Guarded against spatial-temporal autocorrelation and data leakage between training and validation sets.
- Built verification routines to ensure zero source overlap.

### **Day 05: Multi-Channel Tensor Stacking (Rally Cam Project)**
- Constructed 12-channel input representations for deep learning models:
  - 3 temporal RGB frames ($t-2, t-1, t$) $\rightarrow$ 9 color channels.
  - 3 candidate attention/player mask channels $\rightarrow$ 3 binary mask channels.
- Exported and validated multi-page TIFF tensors (`sample12.tif`).
- Defined audit metrics (`correct`, `missed`, `wrong instance`, `false positive`).

---

## 🛠 Prerequisites & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/santhosht5/DataEngineering.git
   cd DataEngineering
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On Linux/macOS:
   source .venv/bin/activate
   ```

3. **Install common dependencies:**
   ```bash
   pip install opencv-python numpy pillow pyyaml
   ```

---

## 👤 Author

- **GitHub:** [@santhosht5](https://github.com/santhosht5)
- **Email:** santhosh.t@gradientascent.in
