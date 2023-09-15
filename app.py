import os
import sys

from DogSegmentation.pipeline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()
print("Training Done!!!")