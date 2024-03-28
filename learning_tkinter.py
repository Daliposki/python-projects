import tkinter


def zacuvaj(show_hide=False):

    if show_hide:
        momentalna_sostojba = password_entri.cget("show")

        password_entri.config(show="" if momentalna_sostojba else "*")
        confirm_password_entri.config(show="" if momentalna_sostojba else "*")
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

            print("poleto za |website| e prazno. ve molime vnesete vebsite!")
        else:
            print("mestoto za website e popolneto.")
            return

        if not email_text:

            print("poleto za |email| e prazno. ve molime vnesete email!")
        else:
            print("poleto za |email| e popolneto.")
            return

        if not recovery_email_text:

            print("poleto za |recovery email| e prazno. ve molime popolnete go!")
        else:
            print("poleto za |recovery email| e popolneto.")
            return

        if password_text != confirm_password_text:

            print("|pasvordite| ne se isti. ve molime vnesete isti pasvordi!")
            return

        if not password_text and not confirm_password_text:

            print("|pasvordite| se prazni. ve molime popolnete gi! ")
        else:
            print("|pasvordite| se isti.")
            return

        with open('text.txt', 'a') as s:
            s.write(website_text + " " + email_text + " " + password_text + " " +
                    confirm_password_text + " " + recovery_email_text + "\n")
            print("informaciite se zacuvani vo fileot text.txt!")


def change_bg_color():
    for entry_widget in [website_entri, email_entri, password_entri, confirm_password_entri, recovery_email_entri]:
        entry_widget.config(bg="lightyellow")


ekran = tkinter.Tk()

ekran.geometry("400x200")


prv = tkinter.Label(text="website", fg="blue")
prv.grid(column=0, row=0, pady=5, padx=30)
website_entri = tkinter.Entry(fg="blue")
website_entri.grid(column=1, row=0)

vtor = tkinter.Label(text="email", fg="orange")
vtor.grid(column=0, row=1, pady=5, padx=30)
email_entri = tkinter.Entry(fg="orange")
email_entri.grid(column=1, row=1)

tret = tkinter.Label(text="password", fg="green")
tret.grid(column=0, row=2, pady=5, padx=30)
password_entri = tkinter.Entry(show="*", fg="green")
password_entri.grid(column=1, row=2)

cetvrt = tkinter.Label(text="confirm password", fg="black")
cetvrt.grid(column=0, row=3, pady=5, padx=30)
confirm_password_entri = tkinter.Entry(show="*", fg="black")
confirm_password_entri.grid(column=1, row=3)

petti = tkinter.Label(text="recovery email", fg="purple")
petti.grid(column=0, row=4, pady=5, padx=30)
recovery_email_entri = tkinter.Entry(fg="purple")
recovery_email_entri.grid(column=1, row=4,)

if not website_entri:
    print("полето за веб-сајтот е празно. Ве молиме внесете веб страница.")

if not password_entri:
    print("Лозинки не се совпаѓаат. Ве молиме внесете совпаѓачки лозинки.")

if not email_entri:
    print("poleto za email e prazno. ve molime vnesete email.")

if not recovery_email_entri:
    print("poleto za star email e prazno. ve molime popolnetego poleto.")


kopce1 = tkinter.Button(text="Save", command=zacuvaj, width=10, bg="blue", fg="white")
kopce1.grid(column=0, row=5, columnspan=1, pady=10)

kopce2 = tkinter.Button(text="Show/hide password", command=lambda: zacuvaj(show_hide=True), bg="green", fg="white")
kopce2.grid(column=1, row=5,  pady=10)


ekran.mainloop()
