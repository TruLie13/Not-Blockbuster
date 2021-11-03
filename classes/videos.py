import csv
import os.path


class Video:

    def __init__(self, video_ID, title, rating, release_year, copies_available):
        self.video_ID = video_ID
        self.title = title
        self.rating = rating
        self.release_year = release_year
        self.copies_available = int(copies_available)

    def __str__(self):
        return f"""
        ***
        title: {self.title} ({self.release_year})
        rated: {self.rating}, video_ID: {self.video_ID}
        copies_available: {self.copies_available}
        ***
            """

    @classmethod
    def get_all_videos(cls):
        videos = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/videos.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                video_instance = Video(**dict(row))
                print(video_instance)
                videos.append(video_instance)

        return videos
