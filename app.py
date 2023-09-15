import os
import sys

from DogSegmentation.pipeline.training_pipeline import Trainpipeline

obj = Trainpipeline()
obj.run_pipeline()
print("Training Done!!!")
