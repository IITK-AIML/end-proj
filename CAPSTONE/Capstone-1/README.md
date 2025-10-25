# Capstone-1: Autonomous Driving

This capstone project focuses on autonomous vehicles and intelligent transport systems, addressing two key aspects of autonomous driving technology: vehicle detection through computer vision and the analysis of autopilot safety incidents using data analytics.

## Project Overview

Tesla launched its Full Self-Driving (FSD) beta program in October 2020, with over 100,000 participants. The project aims to:
1. **Part 1**: Develop an AI model for real-time vehicle detection, classification, and localization in images to support vehicle tracking, counting, and incident response.
2. **Part 2**: Analyze Tesla autopilot usage and its impact on road safety through exploratory data analysis of accident data.

## Project Structure

```
Capstone-1/
├── Part-1/
│   ├── capston-1.ipynb                       # Object detection implementation
│   ├── Images.zip                            # Dataset archive
│   ├── Images/                               # Extracted images (100 images)
│   └── labels.csv                            # Bounding box labels
├── Part-2/
│   ├── capstone-1.ipynb                      # Data analysis implementation
│   └── Tesla-Deaths.csv                      # Tesla accident dataset
└── README.md                                 # This file
```

## Part 1: Vehicle Object Detection

### Objective
Develop a deep learning model that can:
- Predict the type of vehicle in an image (classification)
- Localize vehicles using rectangular bounding boxes (detection)

### Dataset
- **Source**: `Images.zip` - Collection of autonomous vehicle images
- **Labels**: `labels.csv` containing:
  - `image_id`: Image identifier
  - `class`: Vehicle type/category
  - `xmin`, `ymin`, `xmax`, `ymax`: Bounding box coordinates
- **Size**: 100 images total (loaded from labels, prioritized first 1000 but limited by availability)

### Implementation
The solution uses TensorFlow/Keras to build a convolutional neural network:

- **Data Preprocessing**:
  - Unzip `Images.zip`
  - Load images (handles different resolutions: 228px height and 480px height images)
  - Resize all images to 224x224 pixels
  - Encode vehicle classes to numerical labels

- **Model Architecture**:
  - Input layer: 224x224x3 images
  - Convolutional layers: 32 filters (3x3), 64 filters (3x3), 64 filters (3x3)
  - MaxPooling layers (2x2)
  - Dense layers: 64 units + output layers
  - Multi-output model: classification (softmax) + bounding box regression (4 values)

- **Training**:
  - Loss functions: Sparse Categorical Crossentropy (classification), MSE (bounding box)
  - Optimization: Adam
  - Epochs: 100
  - Train/validation split: 80/20

### Evaluation and Inference
- Model evaluation on test set
- Inference on sample images to verify vehicle detection accuracy

### Key Dependencies
- TensorFlow
- Keras
- OpenCV (cv2)
- Pandas, NumPy
- Scikit-learn (train_test_split)

### How to Run
1. Extract `Images.zip` into the `Images/` directory
2. Open `capston-1.ipynb` in Jupyter Notebook
3. Run all cells sequentially
4. Note: Training may take significant time depending on compute resources

## Part 2: Tesla Autopilot Deaths Analysis

### Objective
Analyze the usage of Tesla's autopilot feature and its effects on road safety by exploring patterns in fatal accidents.

### Dataset
- **Source**: `Tesla-Deaths.csv` - Historical Tesla accident data
- **Key Variables**:
  - Date, Country, State: Temporal and geographical information
  - Deaths: Number of fatalities
  - Tesla driver's death status
  - Other vehicles, cyclists/pedestrians involved
  - Vehicle Model, Autopilot claims
  - Verified autopilot deaths

### Implementation
Comprehensive data science workflow:

- **Data Cleaning**:
  - Drop irrelevant columns (Case#, Year, Deceased names, Source, Notes)
  - Handle missing values (fill numeric columns with 0, drop rows with NA)
  - Rename and standardize column names
  - Filter data to years with sufficient incidents (2015-2022 excluding 2023)

- **Exploratory Data Analysis**:
  - Temporal analysis: Accidents by year, month, day
  - Geographical analysis: Accidents by country and state
  - Vehicle model distribution
  - Verified autopilot deaths distribution

- **Key Analytical Questions Answered**:
  - Total fatalities: 341
  - Tesla driver deaths: 113
  - Proportion of incidents involving occupant/cyclist/pedestrian deaths
  - Frequency of collisions with other vehicles
  - Accident distribution across Tesla models
  - Verified autopilot death patterns

### Visualizations
- Count plots for accidents over time
- Bar charts by location and model
- Pie chart for verified autopilot deaths distribution

### Key Dependencies
- Pandas, NumPy
- Seaborn, Matplotlib
- NLTK (imported for potential text analysis, minimally used)

### How to Run
1. Ensure `Tesla-Deaths.csv` is in the directory
2. Open `capstone-1.ipynb` in Jupyter Notebook
3. Execute cells step-by-step to see data cleaning, analysis, and visualizations

## General Requirements

### Environment Setup
```bash
pip install tensorflow keras pandas numpy opencv-python scikit-learn seaborn matplotlib nltk
```

### Prerequisites
- Python 3.x
- Jupyter Notebook
- Sufficient compute resources for Part 1 model training

## Results and Insights

### Part 1 Findings
- Custom CNN architecture successfully trained for simultaneous vehicle classification and localization
- Model evaluates on test set (specific metrics depend on training results)
- Inference demonstrates bounding box prediction capabilities

### Part 2 Insights
- **Temporal Patterns**: Accident frequency shows specific trends across years/months/days
- **Geographical Distribution**: Accidents concentrated in certain countries/states (primarily USA)
- **Model Vulnerabilities**: Specific Tesla models exhibit varying accident rates
- **Safety Impact**: Analysis reveals patterns in verified autopilot-related incidents
- **Human Factors**: 113 Tesla driver fatalities identified across the dataset

## Next Steps and Future Work

- **Model Enhancement**: Implement more advanced architectures (YOLO, SSD, Faster R-CNN) for improved object detection accuracy
- **Data Expansion**: Incorporate larger image datasets for better model generalization
- **Advanced Analytics**: Apply machine learning techniques to predict accident likelihood based on environmental factors
- **Real-time Integration**: Deploy models for actual autonomous vehicle systems
- **Policy Recommendations**: Use insights to inform autonomous vehicle safety regulations

## References

- Tesla Full Self-Driving Beta Program
- Public Tesla safety data sources
- Computer vision techniques for object detection
- Data analysis methodologies for incident investigation