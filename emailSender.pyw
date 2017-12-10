'''
    This code present a simple application to send text mails from
    a gmail,live,yahoo and gmx accounts to any other email address,
    gmail and yahoo ask for the "Less Secure App" option to be actived but
    don't worry, the app will guide you to the right place.

    Enjoy and Leave your comments ;)
'''
import tkinter as tk
from tkinter import ttk
import os
from webbrowser import open_new_tab
import smtplib as smtp
from tkinter import messagebox


ALL_FONT = ("Verdana", 15)
serverType = ""
email = ""
password = ""
smtpObj = smtp.SMTP()


def exitApp():
    reallyTk = tk.Tk()

    lab = tk.Label(reallyTk, text="Do You Wanna Really Exit The App?", font=ALL_FONT)
    yesButt = ttk.Button(reallyTk, text="Yes", command=lambda: os._exit(0))
    noButt = ttk.Button(reallyTk, text="No", command=reallyTk.destroy)

    lab.grid(row=0, column=0, columnspan=2)
    yesButt.grid(row=1, column=0)
    noButt.grid(row=1, column=1)

    
    tk.Tk.wm_title(reallyTk, "Exit...")
    reallyTk.mainloop()

def exitApp2(contTk):
    reallyTk = tk.Tk()

    def exitIt():
        reallyTk.destroy()
        contTk.destroy()

    lab = tk.Label(reallyTk, text="Do You Wanna Really Exit?", font=ALL_FONT)
    yesButt = ttk.Button(reallyTk, text="Yes", command=exitIt)
    noButt = ttk.Button(reallyTk, text="No", command=reallyTk.destroy)

    lab.grid(row=0, column=0, columnspan=2)
    yesButt.grid(row=1, column=0)
    noButt.grid(row=1, column=1)
    
    tk.Tk.wm_title(reallyTk, "Exit...")
    reallyTk.mainloop()

def connectToServer(server):
    global smtpObj
    
    try:
        if server == "gmail":
            smtpObj = smtp.SMTP("smtp.gmail.com", 587)
        elif server == "live":
            smtpObj = smtp.SMTP("smtp.live.com", 587)
        elif server == "yahoo":
            smtpObj = smtp.SMTP("smtp.mail.yahoo.com", 465)
        elif server == "gmx":
            smtpObj = smtp.SMTP("smtp.gmx.com", 25)
        else:
            raise smtp.SMTPConnectError

        smtpObj.starttls()
        return True
    except:
        msg = messagebox.showerror("SMTPConnectError", "Error occurred during establishment of a connection with the server")
        return False
         

def goToGmail(contTk):
    global serverType
    global smtpObj
    serverType="gmail"

    if connectToServer(serverType):
        open_new_tab("https://accounts.google.com/ServiceLogin/signinchooser?service=accountsettings&passive=1209600&osid=1&continue=https%3A%2F%2Fmyaccount.google.com%2Flesssecureapps&followup=https%3A%2F%2Fmyaccount.google.com%2Flesssecureapps&emr=1&mrp=security&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        ConnectSendClass()

def goToLive(contTk):
    global serverType
    global smtpObj
    serverType="live"

    if connectToServer(serverType):
        ConnectSendClass()

def goToYahoo(contTk):
    global serverType
    global smtpObj
    serverType="yahoo"

    if connectToServer(serverType):
        open_new_tab("https://help.yahoo.com/kb/SLN27791.html")
        ConnectSendClass()

def goToGMX(contTk):
    global serverType
    global smtpObj
    serverType="gmx"
    
    if connectToServer(serverType):
        ConnectSendClass()

    

class EmailClass(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        globalP = tk.Frame(self)
        globalP.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.allPages = {}
        for P in (EntryPage, LessSecurePage):
            self.allPages[P] = P(globalP, self)
        self.raisePage(EntryPage)

        tk.Tk.iconbitmap(self, default=r"email_icon.ico")
        tk.Tk.wm_title(self, "Email Sender")
        tk.Tk.resizable(self, False, False)
        tk.Tk.protocol(self, "WM_DELETE_WINDOW", exitApp)
        self.mainloop()
    def raisePage(self, page):
        self.allPages[page].grid(row=0, column=0)
        self.allPages[page].tkraise()

class EntryPage(tk.Frame):
    def __init__(self, contP, contTk):
        tk.Frame.__init__(self, contP)

        message = tk.Message(self, text="""
        This App build just for educationnal purposes, it's source code is available for all users.
        If you do anything wrong with it, we aren't the ones who will pay your fault.
        Feel safe and use it.
        """, font=ALL_FONT)
        agreeButt = ttk.Button(self, text="Agree", command=lambda: contTk.raisePage(LessSecurePage))
        disagreeButt = ttk.Button(self, text="Disagree", command=lambda: os._exit(0))

        message.pack()
        agreeButt.pack()
        disagreeButt.pack()
        

class LessSecurePage(tk.Frame):
    def __init__(self, contP, contTk):
        tk.Frame.__init__(self, contP)
        
        var = tk.StringVar()
        var.set("L")

        message = tk.Message(self, text="""
        You must TURN ON the \"less secure apps\" mode for you email account.
        Please select your account type.
        NOTE: not every account has the above mode!!!
        """, font=ALL_FONT)
        gmailChoice = tk.Radiobutton(self, text="gmail(should TURN it ON)", activebackground="black", activeforeground="yellow", variable=var, value="varG", font=ALL_FONT, command=lambda: goToGmail(contTk))
        liveChoice = tk.Radiobutton(self, text="hotmail/live(shouldn't TURN it ON)", activebackground="black", activeforeground="yellow",variable=var, value="varL", font=ALL_FONT, command=lambda: goToLive(ConnectPage))
        yahooChoice = tk.Radiobutton(self, text="yahoo(should TURN it ON)", activebackground="black", activeforeground="yellow",variable=var, value="varY", font=ALL_FONT, command=lambda: goToYahoo(contTk))
        gmxChoice = tk.Radiobutton(self, text="gmx(shouldn't TURN it ON)", activebackground="black", activeforeground="yellow",variable=var, value="varGMX", font=ALL_FONT, command=lambda: goToGMX(ConnectPage))

        gmailChoice.deselect()
        liveChoice.deselect()
        yahooChoice.deselect()
        gmxChoice.deselect()

        message.pack()
        gmailChoice.pack()
        liveChoice.pack()
        yahooChoice.pack()
        gmxChoice.pack()

class ConnectSendClass(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        globalP = tk.Frame(self)
        globalP.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.allPages = {}
        for P in (ConnectPage, SendPage):
            self.allPages[P] = P(globalP, self)
        self.raisePage(ConnectPage)

        tk.Tk.iconbitmap(self, default=r"email_icon.ico")
        tk.Tk.wm_title(self, "Email Sender")
        tk.Tk.resizable(self, False, False)
        tk.Tk.protocol(self, "WM_DELETE_WINDOW", lambda: exitApp2(self))
        self.mainloop()
    def raisePage(self, page):
        self.allPages[page].grid(row=0, column=0)
        self.allPages[page].tkraise()

class ConnectPage(tk.Frame):
    def __init__(self, contP, contTk):
        tk.Frame.__init__(self, contP)

        emailL = tk.Label(self, text="Email: ")
        self.emailF = tk.Entry(self, width=40)
        passwordL = tk.Label(self, text="Password: ")
        self.passwordF = tk.Entry(self, width=40, show="*")
        exitButt = ttk.Button(self, text="Exit", command=lambda: exitApp2(contTk))
        loginButt = ttk.Button(self, text="Log In", command=lambda: self.checkLogIn(contTk))

        emailL.grid(row=0, column=0, sticky=tk.W)
        self.emailF.grid(row=0, column=1)
        passwordL.grid(row=1, column=0, sticky=tk.W)
        self.passwordF.grid(row=1, column=1)
        exitButt.grid(row=2, column=0, sticky=tk.W)
        loginButt.grid(row=2, column=1, sticky=tk.E)
    def checkLogIn(self, contTk):
        global email
        global password

        e = self.emailF.get()
        p = self.passwordF.get()
        try:
            smtpObj.login(e, p)
            email = e
            password = p
            contTk.raisePage(SendPage)
        except smtp.SMTPHeloError:
            msg = messagebox.showerror("ERROR...", "The server didn’t reply properly to the HELO greeting")
        except smtp.SMTPAuthenticationError:
            msg = messagebox.showerror("ERROR...", "The server didn’t accept the username/password combination")
        except smtp.SMTPNotSupportedError:
            msg = messagebox.showerror("ERROR...", "The AUTH command is not supported by the server")
        except smtp.SMTPException:
            msg = messagebox.showerror("ERROR...", "No suitable authentication method was found")            
        
class SendPage(tk.Frame):
    def __init__(self, contP, contTk):
        tk.Frame.__init__(self, contP)

        toL = tk.Label(self, text="To: ")
        self.toF = tk.Entry(self, width=40)
        msgL = tk.Label(self, text="Msg: ")
        self.msgF = tk.Text(self, height=10, width=70)
        sendButt = ttk.Button(self, text="Send", command=self.sendIt)

        toL.grid(row=0, column=0, sticky=tk.W)
        self.toF.grid(row=0, column=1)
        msgL.grid(row=1, column=0, sticky=tk.W)
        self.msgF.grid(row=1, column=1)
        sendButt.grid(row=2, column=0, columnspan=2)
    def sendIt(self):
        try:
            t = self.toF.get()
            m = self.msgF.get(1.0, tk.END)
            
            smtpObj.sendmail(email, t, m)

            msg = messagebox.showinfo("Mission Completed!!!", "Your Mail Has Been Successfully Sended")
        except smtp.SMTPRecipientsRefused:
            msg = messagebox.showerror("ERROR...", "All recipients were refused. Nobody got the mail. The recipients attribute of the exception object is a dictionary with information about the refused recipients (like the one returned when at least one recipient was accepted)")
        except smtp.SMTPHeloError:
            msg = messagebox.showerror("ERROR...", "The server didn’t reply properly to the HELO greeting")
        except smtp.SMTPSenderRefused:
            msg = messagebox.showerror("ERROR...", "The server didn’t accept the from_addr")
        except smtp.SMTPDataError:
            msg = messagebox.showerror("ERROR...", "The server replied with an unexpected error code (other than a refusal of a recipient)")
        except smtp.SMTPNotSupportedError:
            msg = messagebox.showerror("ERROR...", "SMTPUTF8 was given in the mail_options but is not supported by the server")        
        


ec = EmailClass()
