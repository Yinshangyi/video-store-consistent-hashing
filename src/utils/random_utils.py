import random
import string
from typing import List

random.seed(10)


def generate_random_video_name(length: int, extension='.mp4') -> str:
    name = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return name + extension


def generate_n_videos(num_videos: int) -> List[str]:
    return [generate_random_video_name(10) for n in range(num_videos)]


def get_n_videos_indexes(num_videos: int, min_index: int, max_index: int) -> List[int]:
    return random.sample(range(min_index, max_index), k=num_videos)
