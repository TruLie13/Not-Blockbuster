from classes.customers import Customer
from classes.store import Store
from classes.videos import Video


class Interface:

    def __init__(self, store__name):
        self.store = Store(store__name)

    @property
    def menu(self):
        return f'''
       == Welcome to Not Blockbuster! ==

        1. View store video inventory
        2. View customer account
        3. Add new customer
        4. Rent video
        5. Return video
        6. Exit

        '''

    def run(self):

        while True:
            mode = input(self.menu)

            if mode == "1":
                for video in Video.get_all_videos():
                    print(video)
            elif mode == "2":
                customer_ID = input("Enter Customer ID: ")
                print(self.store.get_customer(customer_ID))
            elif mode == "3":
                self.store.set_customer()
            elif mode == "4":
                self.store.rent_video()
            elif mode == "5":
                self.store.return_video()
            elif mode == "6":
                break
            # secret: list all customer option
            elif mode == "all":
                for customer in Customer.get_all_customers():
                    print(customer)
            else:
                print('''
            *please enter valid menu option*
                ''')
