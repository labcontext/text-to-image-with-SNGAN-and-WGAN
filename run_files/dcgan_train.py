import os
import sys
import numpy as np
from random import shuffle


def main():
    seed = 42

    np.random.seed(seed)

    current_dir = os.path.dirname(__file__)
    sys.path.append(os.path.join(current_dir, '..'))
    current_dir = current_dir if current_dir is not '' else '.'

    #img_dir_path = current_dir + '/data/demoset/img'
    img_dir_path = '/home/rd/recognition_reaserch/IMAGE_CAPTION/DATASET/val2014'
    txt_dir_path = '/home/rd/recognition_reaserch/IMAGE_CAPTION/DATASET/captions'
    model_dir_path = current_dir + '/models'

    img_width = 64
    img_height = 64

    stage_width = 128
    stage_height = 128

    img_channels = 3

    from TXT2IMAGE.library.dcgan_v3 import DCGanV3
    from TXT2IMAGE.library.utility.img_cap_loader import load_normalized_img_and_its_text

    image_label_pairs = load_normalized_img_and_its_text(img_dir_path, txt_dir_path, img_width=img_width, img_height=img_height)
    shuffle(image_label_pairs)

    gan = DCGanV3()
    gan.img_width = img_width
    gan.img_height = img_height

    gan.img_channels = img_channels
    gan.random_input_dim = 80
    gan.glove_source_dir_path = './very_large_data'

    batch_size = 8
    epochs = 50000
    gan.fit(model_dir_path=model_dir_path, image_label_pairs=image_label_pairs,
            snapshot_dir_path=current_dir + '/data/snapshots',
            snapshot_interval=100,
            batch_size=batch_size,
            epochs=epochs)


if __name__ == '__main__':
    main()
