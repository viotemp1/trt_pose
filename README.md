# TensorRT Pose Estimation

This project features multi-instance pose estimation accelerated by NVIDIA TensorRT.  It is ideal for use in applications where low latency is necessary.  It includes

- Training scripts to train on any keypoint task data in MSCOCO format

- Evaluation scripts to assess the accuracy of a trained model 
- A collection of models that may be easily optimized with TensorRT using [torch2trt](https://github.com/NVIDIA-AI-IOT/torch2trt)

This project can be used easily for the task of human pose estimation, or extended for something new.

If you run into any issues please [let us know](../../issues).

## Human pose

To try out these pre-trained models, please follow the human pose [notebooks](notebooks/human_pose).

| Name | Accuracy | Jetson Nano | Jetson Xavier | Pre-trained Weights |
|-------|------------|-------------|---------------|---------------------|
| [densenet121_baseline_att_256x256_A](experiments/densenet121_baseline_att_256x256_A) |  |  |  | [download (84MB)](https://drive.google.com/open?id=199JXyPHxGh3uTy2Eezef9CFqgC8v76Od) |
| [densenet169_baseline_att_256x256_A](experiments/densenet169_baseline_att_256x256_A) |  |  |  | [download (127MB)](https://drive.google.com/open?id=1BboOiLor9aRxegVOU35ml5r2--YCvhaU) |

For more information on how to train or evaluate a human pose model, please read the human pose [documentation](docs/human_pose.md).
