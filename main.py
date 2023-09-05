from tkinter import *
import random
from tkinter import messagebox
import json


def erase_data():
    website.delete(0, END)
    usr_mail_name.delete(0, END)
    Pass_word.delete(0, END)





# used to retrieve the previous data if it is already stored.
def info_retrieve():
    try:
        with open("db.json") as file:
            retrieved_data = json.load(file)
        search_item = website.get()
        username_email = retrieved_data[search_item]['username']
        password = retrieved_data[search_item]['password']
    # except FileNotFoundError:
    #     db_creator()
    #     info_retrieve()
    except KeyError:
        messagebox.showinfo(title=search_item, message="Searched data item not found!.")
        erase_data()
    else:
        messagebox.showinfo(title=search_item, message=f"username/email : {username_email} \nPassword : {password}")
        erase_data()

#generating an 16 digits passwords with combination of 5 x (letter,special character, numbers) + 1 x Captital at Beginning.
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u'
        , 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q'
        , 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y ', 'Z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    spl_letters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

    mylist = []
    first_char = random.choice(letters[26:])

    for i in range(5):
        mylist.append(random.choice(letters))
        mylist.append(random.choice(numbers))
        mylist.append(random.choice(spl_letters))

    random.shuffle(mylist)
    mylist.insert(0, first_char)
    mylist = "".join(mylist)
    Pass_word.delete(0, END)
    Pass_word.insert(0, mylist)


# used to add the given details into db.json.
def submitter():
    # retrieving data using get()
    Website = website.get()
    Usr_Mail_Name = usr_mail_name.get()
    Pass_Word = Pass_word.get()
    new_data = {
        Website: {'username': Usr_Mail_Name,
                  'password': Pass_Word
                  }
    }
    if Website == "" or Usr_Mail_Name == "" or Pass_Word == "":
        messagebox.showinfo(title="Alert", message="Please, fill all blanks!")
    else:
        with open("db.json") as file:
            data = json.load(file)
            data.update(new_data)
        with open("db.json", 'w') as file:
            json.dump(data, file, indent=4)
        erase_data()


# window
window = Tk()
window.title("PassWord Manager")
window.config(padx=100, pady=100)
# image
canvas = Canvas(width=200, height=200)
img_file = PhotoImage(file="logo.png")
image_file = canvas.create_image(110, 100, image=img_file)
canvas.grid(row=0, column=1)
# labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
usr_mail_name_label = Label(text="Username/Email:")
usr_mail_name_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
# Entry
website = Entry(width=28)
website.grid(row=1, column=1)
usr_mail_name = Entry(width=45)
usr_mail_name.grid(row=2, column=1, columnspan=2)
Pass_word = Entry(width=28)
Pass_word.grid(row=3, column=1)

# button
show_web = Button(text="Find Details", command=info_retrieve)
show_web.grid(row=1, column=2)
pass_gen_button = Button(text="GeneratePassword", command=gen_pass, width=13)
pass_gen_button.grid(row=3, column=2)

clicker = Button(text="Add", command=submitter, width=38)
clicker.grid(row=4, column=1, columnspan=2)
window.mainloop()
