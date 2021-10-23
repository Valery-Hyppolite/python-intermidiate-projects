from json.decoder import JSONDecodeError
from tkinter import *
from tkinter import messagebox
from collections import OrderedDict
import pyperclip
import json

# -------------------------------CLEAR SCREEN---------------------------
def clear_creen():
    web_name_entry.delete(0, END)
    pass_word_entry.delete(0, END)
    user_name_entry.delete(0, END)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_psw():
    import generate
    psw = generate.password_generator()
    pass_word_entry.insert(0, psw)  # populate the pwsd when user click the generate psw button
    #pyperclip.copy(psw)






# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_info():
    # get text entries:
    website = web_name_entry.get().lower()
    email = user_name_entry.get()
    psw = pass_word_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': psw,
        }
    }

    # check if entry are empty:
    if len(website) == 0 or len(email) == 0 or len(psw) == 0:
        messagebox.showerror(title='Warning', message='Please do not leave any fields empty!')
    else:
        try:
            with open('psw_data.json', mode='r') as json_file:
                # READ DATA IN FILE
                data = json.load(json_file)
        except FileNotFoundError:
            with open('psw_data.json', mode='w') as json_file:
                json.dump(new_data, json_file, indent=4)
                print('there no such file, file will be created')
        else:
            # check if name already exit. if name exist,  cancel or add new change to specific data name based on user response
            if website in data:
                resp = messagebox.askquestion(title='warning', message='WEBSITE NAME ALREADY EXIST\n Would you like to update its info?')
                if resp == 'no':
                    messagebox.showinfo(title='MESSAGE', message='NO CHANGE WAS MADE!')
                else:
                    for webname in data.copy():  # data.copy helps to iterate over a dict and ovoid the 'RuntimeError: dictionary changed size during iteration”
                        if webname == website:
                            data.update(new_data)
                            with open('psw_data.json', mode='w') as json_file:
                                json.dump(data, json_file,  indent=4)
                                messagebox.showinfo(title='UPDATED', message=f'{website} has been updated')
            else:
                # if name not in database, add new data to file.
                data.update(new_data)
                with open('psw_data.json', mode='w') as json_file:
                    json.dump(data, json_file, indent=4)
                    messagebox.showinfo(title='NEW ITEM', message=f'{website} has been added')

        # CLEAR THE SCREEN
        finally:
            web_name_entry.delete(0, END)
            pass_word_entry.delete(0, END)





# -----------------------------------------SEARCH ----------------------------------#
def find_password():
    search_text = web_name_entry.get().lower()
    try:
        with open('psw_data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='NO DATA FILE FOUND')
    else:
        if search_text not in data:
            messagebox.showinfo(title=f"{search_text}", message=f'WEBSITE {search_text} NOT FOUND')
        else:
            user_name_entry.delete(0, END)
            email = data[search_text]['email']
            password = data[search_text]['password']
            user_name_entry.insert(0, email)
            pass_word_entry.insert(0, password)




#---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
canvas_img = PhotoImage(file='lock-and-key-icon-17.jpg')
canvas.create_image(100, 100, image=canvas_img)
canvas.grid(column=1, row=0, columnspan=2)


web_name = Label(text='Website:')
web_name.grid(column=0, row=1)
web_name_entry = Entry(text='Inter website name ', width=35)
web_name_entry.grid(column=1, row=1, columnspan=2)
web_name_entry.focus()

user_name = Label(text='Email/Username: ')
user_name.grid(column=0, row=2)
user_name_entry = Entry(text='Inter email or username', width=35)
user_name_entry.grid(column=1, row=2, columnspan=2, padx=10)
user_name_entry.insert(0, "myemail@gmail.com")


pass_word = Label(text='Password:')
pass_word.grid(column=0, row=3)
pass_word_entry = Entry(tex='Write your psw or generate one ', width=35)
pass_word_entry.grid(column=1, row=3, columnspan=2, pady=10)

#buttons
psw_generator = Button(text='Generate password', command=generate_psw, width=15)
psw_generator.grid(column=3, row=3)

search = Button(text='Search', width=10, command=find_password)
search.grid(column=3, row=1)

add = Button(text="ADD", bg='#010101', fg='white', width=35, command=add_info)
add.grid(column=1, row=4, columnspan=2, pady=10)

clear_button = Button(text="CLEAR", width=35, bg='#010101', fg='#FFFFFF', command=clear_creen)
clear_button.grid(column=1, row=5, columnspan=2)


window.mainloop()