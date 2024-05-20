import tkinter as tk
from tkinter import messagebox
from resources import hash
from resources import results


# Create class
class CheckSomeGui:
    # Define __init__
    def __init__(self):
        # Create main window
        self.main_window = tk.Tk()

        # Set the window size
        self.main_window.geometry("720x400")

        # Set the window title
        self.main_window.title("Check Some Checksum Calculator")

        # Create frame for CheckSome logo
        self.logo_frame = tk.Frame(
            self.main_window,
            relief=tk.GROOVE,
            borderwidth=5
        )
        self.logo_frame.pack(fill=tk.X)

        # Add to logo_frame
        photo = tk.PhotoImage(file="resources/checksome_logo.png")
        self.image_label = tk.Label(
            self.logo_frame,
            image=photo,
            width=200,
            height=112,
            background="#5948f8"
        )
        self.image_label.pack(fill=tk.X)

        # Create frame for developer checksum
        self.dev_checksum_frame = tk.Frame(
            self.main_window,
            relief=tk.GROOVE,
            background="#dedcf1",
            borderwidth=5
        )
        self.dev_checksum_frame.pack(fill=tk.X)

        # Add to dev_checksum_frame
        self.dev_checksum_label = tk.Label(
            self.dev_checksum_frame,
            text="Enter provided checksum: ",
            font=("arial", 14),
            background="#dedcf1",
            foreground="#282540"
        )
        self.dev_checksum_label.pack(side="left")

        self.dev_checksum_entry = tk.Entry(
            self.dev_checksum_frame,
            width=45,
            font=("baskerville", 12),
            background="#f9f9fe",
            foreground="#282540"
        )
        self.dev_checksum_entry.pack(side="right")

        # Temporarily holds the dev_checksum entry
        dev_checksum = self.dev_checksum_entry.get()

        # Create frame for filename
        self.filename_frame = tk.Frame(
            self.main_window,
            relief=tk.GROOVE,
            background="#dedcf1",
            borderwidth=5
        )
        self.filename_frame.pack(fill=tk.X)

        # Add to filename_frame
        self.filename_label = tk.Label(
            self.filename_frame,
            text="Enter the exact filename: ",
            font=("arial", 14),
            background="#dedcf1",
            foreground="#282540"
        )
        self.filename_label.pack(side="left")

        self.filename_entry = tk.Entry(
            self.filename_frame,
            width=45,
            font=("baskerville", 12),
            background="#f9f9fe",
            foreground="#282540"
        )
        self.filename_entry.pack(side="right")

        # Temporarily holds the filename entry
        filename = self.dev_checksum_entry.get()

        # Create frame for algorithm selection
        self.algorithm_frame = tk.Frame(
            self.main_window,
            relief=tk.GROOVE,
            background="#dedcf1",
            borderwidth=5
        )
        self.algorithm_frame.pack(fill=tk.X)

        # Add to algorithm_frame
        self.algorithm_label = tk.Label(
            self.algorithm_frame,
            text="Select an algorithm: ",
            font=("arial", 14),
            background="#dedcf1",
            foreground="#282540"
        )
        self.algorithm_label.pack(side="left")

        # Create tuple of algorithms
        algorithms = ("md5", "sha1", "sha224", "sha256", "sha384", "sha512")

        self.algorithm_listbox = tk.Listbox(
            self.algorithm_frame,
            listvariable=tk.Variable(value=algorithms),
            height=6,
            width=45,
            font=("baskerville", 12),
            background="#f9f9fe",
            foreground="#282540",
            selectmode=tk.EXTENDED,
            exportselection=0
        )
        self.algorithm_listbox.pack(side="right")

        # Create frame for quit and check button
        self.check_frame = tk.Frame(
            self.main_window,
            relief=tk.GROOVE,
            background="#dedcf1",
            borderwidth=5
        )
        self.check_frame.pack(fill=tk.BOTH)

        # Add check button
        self.check_button = tk.Button(
            self.check_frame,
            text="Check",
            font=("arial", 14),
            height=3,
            width=6,
            background="#5948f8",
            foreground="#f9f9fe",
            command=self.check_clicked
        )
        self.check_button.pack(side="left")

        # Add quit button
        self.quit_button = tk.Button(
            self.check_frame,
            text="Quit",
            font=("arial", 14),
            height=3,
            width=6,
            background="#5948f8",
            foreground="#f9f9fe",
            command=self.quit_clicked
        )
        self.quit_button.pack(side="right")

        # Start Main Loop
        tk.mainloop()

    def check_clicked(self):
        # Create instance of results class
        check_some = results.Results()

        # Get provided checksum
        dev_checksum = self.dev_checksum_entry.get().strip().lower()
        check_some.set_dev_checksum(dev_checksum)

        # Get filename
        filename = self.filename_entry.get().strip()
        check_some.set_filename(filename)

        # Get algorithm
        algorithm_data = self.algorithm_listbox.curselection()
        algorithm = algorithm_data[0]
        check_some.set_algorithm(algorithm)

        # Get selected algorithm ("md5", "sha1", "sha224", "sha256", "sha384", "sha512")
        if algorithm == 0:
            check_some.set_algorithm("md5")
        elif algorithm == 1:
            check_some.set_algorithm("sha1")
        elif algorithm == 2:
            check_some.set_algorithm("sha224")
        elif algorithm == 3:
            check_some.set_algorithm("sha256")
        elif algorithm == 4:
            check_some.set_algorithm("sha384")
        elif algorithm == 5:
            check_some.set_algorithm("sha512")
        else:
            print("Not a valid algorithm")

        # Calculate checksum of file
        checksum = hash.hashfile(filename, check_some.algorithm).lower()
        check_some.set_checksum(checksum)

        # Check for matching checksums
        if dev_checksum == checksum:
            match = "Yes"
        else:
            match = "No"

        check_some.set_match(match)

        # Generate message box
        message = [
            f"     Provided checksum: {dev_checksum}\n",
            f"      Actual checksum: {checksum}\n",
            f"           Match: {match}"
        ]
        messagebox.showinfo(
            "CheckSome Results",
            message[0] + message[1] + message[2],
        )

        # Call to results save function
        check_some.save()

    def quit_clicked(self):
        self.main_window.destroy()


# Create instance of class
checksome_gui = CheckSomeGui()
