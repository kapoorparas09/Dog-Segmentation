ARTIFACTS_DIR: str = "artifacts"

DATA_INGESTION_DIR_NAME: str = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

DATA_DOWNLOAD_URL: str ="https://drive.google.com/file/d/19d6_-HjE6PTXDtdnXbc4TtPnQqeJDHx3/view?usp=drive_link"



DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE = 'status.txt'

DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "valid", "test", "data.yaml"]



MODEL_TRAINER_DIR_NAME: str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov8s-seg.pt"

MODEL_TRAINER_NO_EPOCHS: int = 10

# MODEL_TRAINER_BATCH_SIZE: int = 16  # Yolov8 has predefined batch size.