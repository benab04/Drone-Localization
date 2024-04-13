# YOLOv8 Drone Localization

This repository contains code for drone localization using the YOLOv8 object detection model. The model is trained to detect drones in images and videos in real-time. Additionally, it includes evaluation metrics such as precision-recall curves, F1 curve, and confusion matrix, providing insights into the model's performance.

## Features

- Detection of drones in images and videos using YOLOv8.
- Evaluation metrics for assessing model performance.
- Real-time tracking of drones in videos.
- Various visualization tools for analyzing model results.

## Applications

The YOLOv8 model for drone localization has several applications in different fields:

1. **Surveillance and Security**: Drones are increasingly being used for surveillance purposes. This model can help security personnel detect and track drones in restricted areas.

2. **Environmental Monitoring**: Drones equipped with sensors can monitor environmental parameters such as air quality, temperature, and pollution levels. This model can assist in identifying and tracking drones used for environmental monitoring tasks.

3. **Infrastructure Inspection**: Drones are used for inspecting infrastructure such as bridges, pipelines, and power lines. This model can aid in detecting drones during inspection activities, ensuring safety and security.

4. **Event Security**: At public events and gatherings, drones may pose security risks. This model can be deployed to monitor the airspace and detect unauthorized drones.

## Repository Contents

- **Images**: Contains sample images of detected drones using the YOLOv8 model. Add your detected drone images here.
- **Evaluation Metrics**: Includes plots of precision-recall curves, F1 curve, PR curve, P curve, R curve, and confusion matrix. Add your evaluation curves and metrics here.
- **Video**: Provides a real-time detection video demonstrating the model's performance.

## Getting Started

To use the YOLOv8 model for drone localization, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/benab04/Drone-Localization.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the model on your images or videos:
   The dataset used for training and testing is:
    ```bash
    kaggle datasets download -d muki2003/yolo-drone-detection-dataset
    ```

## Results

### Detected Drones in dataset
![Test results](https://github.com/benab04/Drone-Localization/assets/124769045/99bd1e1f-64fd-4671-aca7-5beafcb4adb2)

### Evaluation Metrics
![metrics](https://github.com/benab04/Drone-Localization/assets/124769045/afa94c45-9a61-4821-9fff-5f80e68c6ea7)

#### Precision-Recall Curve
![PR_curve](https://github.com/benab04/Drone-Localization/assets/124769045/d23e7f7c-1191-4e2d-ab90-82163a7feb8a)

#### Confusion Matrix
![Confusion Matrix](https://github.com/benab04/Drone-Localization/assets/124769045/430e7517-345f-4553-bb6c-b46cf22038b9)

## Acknowledgments

- This project is inspired by the YOLOv8 model implementation by Ultralytics.

