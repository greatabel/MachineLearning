from PIL import Image
from feature_extractor import FeatureExtractor
from pathlib import Path
import numpy as np

if __name__ == "__main__":
    fe = FeatureExtractor()

    source_image_folder = "movie/static/img/source"
    for img_path in sorted(Path(source_image_folder).glob("*.jpg")):
        print(img_path)  # e.g., ./static/img/xxx.jpg
        feature = fe.extract(img=Image.open(img_path))
        feature_path = Path("movie/static/feature") / (
            img_path.stem + ".npy"
        )  # e.g., ./static/feature/xxx.npy
        np.save(feature_path, feature)
