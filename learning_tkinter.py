import tkinter


def save(show_hide=False):

    if show_hide:
        current_state = password_entri.cget("show")

        password_entri.config(show="" if current_state else "*")
        confirm_password_entri.config(show="" if current_state else "*")
    else:
        website_text = website_entri.get()
        print(website_text)
        email_text = email_entri.get()
        print(email_text)
        password_text = password_entri.get()
        print(password_text)
        confirm_password_text = confirm_password_entri.get()
        print(confirm_password_text)
        recovery_email_text = recovery_email_entri.get()
        print(recovery_email_text)

        if not website_text:

            print("The WEBSITE field is empty. Please enter a website!")
        else:
            print("The WEBSITE field is filled.")
            return

        if not email_text:

            print("The EMAIL field is empty. Please enter an email!")
        else:
            print("The EMAIL field is filled.")
            return

        if not recovery_email_text:

            print("The RECOVERY EMAIL field is empty. Please enter an email!")
        else:
            print("The RECOVERY EMAIL field is filled.")
            return

        if password_text != confirm_password_text:

            print("The PASSWORDS are not the same. Please enter the same passwords!")
            return

        if not password_text and not confirm_password_text:

            print("PASSWORDS are empty. Please fill in!")
        else:
            print("The PASSWORDS are the same.")
            return

        with open('text.txt', 'a') as s:
            s.write(website_text + " " + email_text + " " + password_text + " " +
                    confirm_password_text + " " + recovery_email_text + "\n")
            print("The INFORMATION is stored in the text.txt file!")


def change_bg_color():
    for entry_widget in [website_entri, email_entri, password_entri, confirm_password_entri, recovery_email_entri]:
        entry_widget.config(bg="lightyellow")


screen = tkinter.Tk()

screen.geometry("400x200")


first = tkinter.Label(text="website", fg="blue")
first.grid(column=0, row=0, pady=5, padx=30)
website_entri = tkinter.Entry(fg="blue")
website_entri.grid(column=1, row=0)

second = tkinter.Label(text="email", fg="orange")
second.grid(column=0, row=1, pady=5, padx=30)
email_entri = tkinter.Entry(fg="orange")
email_entri.grid(column=1, row=1)

third = tkinter.Label(text="password", fg="green")
third.grid(column=0, row=2, pady=5, padx=30)
password_entri = tkinter.Entry(show="*", fg="green")
password_entri.grid(column=1, row=2)

fourth = tkinter.Label(text="confirm password", fg="black")
fourth.grid(column=0, row=3, pady=5, padx=30)
confirm_password_entri = tkinter.Entry(show="*", fg="black")
confirm_password_entri.grid(column=1, row=3)

fifth = tkinter.Label(text="recovery email", fg="purple")
fifth.grid(column=0, row=4, pady=5, padx=30)
recovery_email_entri = tkinter.Entry(fg="purple")
recovery_email_entri.grid(column=1, row=4,)

if not website_entri:
    print("The WEBSITE field is empty. Please enter a website!")

if not password_entri:
    print("PASSWORDS do not match. Please enter matching passwords!")

if not email_entri:
    print("Тhe EMAIL field is empty. Please enter an email!")

if not recovery_email_entri:
    print("Тhe OLD EMAIL field is empty. Please enter an old email!")


button_1 = tkinter.Button(text="Save", command=save, width=10, bg="blue", fg="white")
button_1.grid(column=0, row=5, columnspan=1, pady=10)

button_2 = tkinter.Button(text="Show/hide password", command=lambda: save(show_hide=True), bg="green", fg="white")
button_2.grid(column=1, row=5,  pady=10)


screen.mainloop()
