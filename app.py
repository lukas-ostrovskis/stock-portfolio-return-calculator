from tkinter import *
import logic

class Application(Frame):
    def buttonClick(self):
        # Parse submitted text into input string
        input = self.text.get("1.0", "end-1c")

        # Get the start and end dates
        start = self.startDate.get()
        end = self.endDate.get()

        # Send data to the logic layer
        returns = logic.returns(input, start, end)

        # Update the Total return label with returns in %
        self.result.config(text = "Total return:\n" + ('%.2f' % returns[0]) + "%")
        # Update the Invalid tickers label with tickers that were not found
        self.invalidTickers.config(text = "Tickers not found:\n" + "\n".join(returns[1]))

    def createWidgets(self):
        # Label describing how to input stock info
        self.label = Label(self, text="Input your shares in format:\n'Ticker' 'Target percentage'", bg='#2e313b', fg='white')
        self.label.grid(column=0, row=0)

        # Text area for inputting stock info
        self.text = Text(self, width=19, height=10)
        self.text.configure(bg='#5F626B')
        self.text.grid(column=0, rowspan=10)

        # Submit button
        self.btn = Button(self, command=self.buttonClick, text="Submit")
        self.btn.grid(column=0, row=12)

        # Start date label
        self.labelSD = Label(self, text="Start Date (yyyy-mm-dd):", bg='#2e313b', fg='white')
        self.labelSD.grid(column=0, row=13)
        # Start date entry box
        self.startDate = Entry(self)
        self.startDate.grid(column=1, row=13)

        # End date label
        self.labelED = Label(self, text="End Date (yyyy-mm-dd):", bg='#2e313b', fg='white')
        self.labelED.grid(column=0, row=14)
        # End date entry box
        self.endDate = Entry(self)
        self.endDate.grid(column=1, row=14)

        # Total return label
        self.result = Label(self, text="", font=("Roboto", 16), bg='#2e313b', fg='white')
        self.result.grid(columnspan=3, row=16)

        # Invalid tickers label
        self.invalidTickers = Label(self, text="", font=("Roboto", 8), bg='#2e313b', fg='white')
        self.invalidTickers.grid(column=1, row=0, rowspan=10)

    # Initialize the main frame of application
    def __init__(self, master=None):
        Frame.__init__(self, master, bg='#2e313b')
        root.geometry('300x350')
        root.configure(bg='#2e313b')
        self.pack()
        self.createWidgets()

# Start application
root = Tk()
root.title("Portfolio Returns")
app = Application(master = root)
app.mainloop()




