from colorama import Fore, Style
from face_tally.ml_logic.data import *
from face_tally.ml_logic.preprocessing import *
from face_tally.ml_logic.train import *


def preprocess():
    """
    - Query the raw dataset from Google CloudStorage
    - Download images locally
    - Process data
    """

    print("Starting preprocessing")

    df = load_annotations_csv()

    df = normalize_data(df)

    print("Data has been normalized")

    df = aggregate_boxes(df)

    data = add_image_path_to_bbox(df)

    data = load_dataset(data)

    print("Data has been normalized and processed")

    return data


def train(data):
    """
    - Train on the preprocessed dataset
    - Store training results and model weights
    - Return loss as a float
    """

    print("Starting training")

    train_ds, val_ds, test_data = splitting_data(data)

    history = fit_model(train_ds, val_ds)

    print("Training done")

    return history


def evaluate():
    """
    Evaluate the performance of the latest production model on processed data
    Return loss as a float
    """
    pass


def pred():
    """
    Make a prediction using the latest trained model
    """
    pass


if __name__ == "__main__":
    data = preprocess()
    history = train(data)
    # evaluate()
    # pred()
