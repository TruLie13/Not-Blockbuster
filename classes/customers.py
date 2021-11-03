from classes.videos import Video
import csv
import os.path


class Customer:

    def __init__(self, customer_ID, account_type, first_name, last_name, current_video_rentals=""):
        self.customer_ID = customer_ID
        self.account_type = account_type
        self.first_name = first_name
        self.last_name = last_name
        if current_video_rentals == "":
            self.current_video_rentals = []
        else:
            self.current_video_rentals = current_video_rentals.split("/")

    def rent_video(self, customer_ID, title):
        # self.display_current_video_rentals += title
        pass

    def return_video_instance(self, title):
        print(self.display_current_video_rentals.replace(str(title), ""))

    def parse_customer_videos(self, videos):
        return ", ".join(videos)

    def __str__(self):
        return f"""
        ***
        customer_ID:......... {self.customer_ID}
        customer_name:....... {self.first_name} {self.last_name}
        current_rentals:..... {self.parse_customer_videos(self.current_video_rentals)}
        ***
            """

    @classmethod
    def get_all_customers(cls):
        customers = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/customers.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(dict(row))
                customers.append(Customer(**dict(row)))

        return customers
