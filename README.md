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
    !kaggle datasets download -d muki2003/yolo-drone-detection-dataset
    ```

## Results

### Detected Drones in dataset

![Detected Drones](images/detected_drones.jpg)

### Evaluation Metrics



#### Precision-Recall Curve

![Precision-Recall Curve](evaluation_metrics/pr_curve.png)

#### Confusion Matrix

![Confusion Matrix](evaluation_metrics/confusion_matrix.png)


## Acknowledgments

- This project is inspired by the YOLOv8 model implementation by Ultralytics.

