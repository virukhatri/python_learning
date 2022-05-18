from asyncio import constants


class Employee:
    company="Google"

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    def wish(self,signature):
        print(f"I wish, {signature}")


viru= Employee()

viru.greet()

viru.wish("Thank You!")