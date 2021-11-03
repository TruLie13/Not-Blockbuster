from classes.customers import Customer
from classes.videos import Video
import csv
import os


class Store(Video):

    def __init__(self, name):
        self.name = name
        self.customers = Customer.get_all_customers()
        self.videos = Video.get_all_videos()
        self.customer_account = None

    def set_customer(self):
        customer_ID = input("Enter Customer ID: ")
        account_type = input("Enter Account Type: ")
        first_name = input("Enter Customer First Name: ")
        last_name = input("Enter Customer Last Name: ")
        customer_id = self.get_customer(customer_ID)

        account_types = ["sx", "sf", "px", "pf"]
        if customer_id != None:
            print("Failed to add new customer: ID already in use.")
            return
        elif account_type not in account_types:
            print(
                "Failed to add new customer: Account type must be either sx, sf, px, or pf")
            return
        self.customers.append(
            Customer(customer_ID, account_type, first_name, last_name))
        self.save()

    def get_customer(self, customer_ID):
        for customer in self.customers:
            if customer_ID == customer.customer_ID:
                return customer
        return None

    def get_video(self, video_ID):
        for video in self.videos:
            if video_ID == video.video_ID:
                return video
        return None

    def rent_video(self):
        customer_ID = input("Enter Customer ID: ")
        customer = self.get_customer(customer_ID)
        if customer == None:
            print("Customer ID does not exist")
            input("Press Enter to continue")
            return
        print("Available Videos:")
        for video in self.videos:
            if video.copies_available == 0:
                continue
            print(f"{video.video_ID}) {video.title}")
        video_ID = input("Enter Movie ID: ")
        video = self.get_video(video_ID)
        if video == None or video.copies_available == 0:
            print("Invalid Video ID")
            input("Press Enter to continue")
            return
        customer.current_video_rentals.append(video.title)
        video.copies_available = video.copies_available - 1
        self.save()

    def return_video(self):
        customer_ID = input("Enter Customer ID: ")
        customer = self.get_customer(customer_ID)
        if customer == None:
            print("Customer ID does not exist")
            input("Press Enter to continue")
            return
        print("Checked-out Videos:")
        for video in self.videos:
            # if video is not in customer.videos
            if video.title not in customer.current_video_rentals:
                continue
            print(f"{video.video_ID}) {video.title}")
        video_ID = input("Enter Movie ID: ")
        video = self.get_video(video_ID)
        # if video ID doesn't exist OR video not checked-out
        if video == None or video.title not in customer.current_video_rentals:
            print("Invalid Video ID")
            input("Press Enter to continue")
            return
        customer.current_video_rentals.remove(video.title)
        video.copies_available = video.copies_available + 1
        self.save()

    def save(self):
        my_path = os.path.abspath(os.path.dirname(__file__))

        path = os.path.join(my_path, "../data/customers.csv")
        with open(path, 'w') as csvfile:
            customer_csv = csv.writer(csvfile, delimiter=",")
            customer_csv.writerow(
                ['customer_ID', 'account_type', 'first_name', 'last_name', 'current_video_rentals'])
            for customer in self.customers:
                video_rentals = "/".join(customer.current_video_rentals)
                customer_csv.writerow([customer.customer_ID, customer.account_type,
                                      customer.first_name, customer.last_name, video_rentals])

        path = os.path.join(my_path, "../data/videos.csv")
        with open(path, 'w') as csvfile:
            video_csv = csv.writer(csvfile, delimiter=",")
            video_csv.writerow(
                ['video_ID', 'title', 'rating', 'release_year', 'copies_available'])
            for video in self.videos:
                video_csv.writerow(
                    [video.video_ID, video.title, video.rating, video.release_year, video.copies_available])
