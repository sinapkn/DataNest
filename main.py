import tkinter as tk
from tkinter import messagebox
from topleveld import toplevel_1
from i18n import t, set_language, Language


class MainApp:
    """Main application window."""

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("700x400")
        self.root.title(t("app_title"))
        self.root.configure(bg="#CADEE5")
        self.root.resizable(True, True)

        # Welcome label
        self.welcome_label = tk.Label(
            self.root,
            bg="#CADEE5",
            text=t("welcome_title"),
            font=("Arial", 25, "bold"),
            pady=150,
        )
        self.welcome_label.pack(anchor=tk.CENTER)

        # Developer name label
        self.developer_label = tk.Label(
            self.root,
            bg="#CADEE5",
            text="sinapk",
            font=("Arial", 12, "italic"),
            fg="#555555",
        )
        self.developer_label.pack(anchor=tk.CENTER)

        self.menu = None
        self.build_menu()

    def change_language(self, lang: Language):
        """Change language and refresh UI."""
        set_language(lang)
        self.refresh_ui()

    def refresh_ui(self):
        """Refresh all UI elements with current language."""
        self.root.title(t("app_title"))
        self.welcome_label.config(text=t("welcome_title"))
        self.build_menu()

    def build_menu(self):
        """Build (or rebuild) the menu bar."""
        # Destroy previous menu if exists
        if self.menu:
            self.root.nametowidget(self.root.cget("menu")).destroy()

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        # File/Info menu
        filemenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label=t("menu_info"), menu=filemenu)
        filemenu.add_command(
            label=t("menu_add_info"),
            command=lambda: toplevel_1(self.root),
        )
        filemenu.add_separator()
        filemenu.add_command(label=t("menu_exit"), command=self.root.quit)

        # Language submenu
        langmenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label=t("menu_language"), menu=langmenu)
        langmenu.add_command(
            label="English",
            command=lambda: self.change_language(Language.ENGLISH),
        )
        langmenu.add_command(
            label="فارسی",
            command=lambda: self.change_language(Language.PERSIAN),
        )

    def run(self):
        """Start the application."""
        self.root.mainloop()


if __name__ == "__main__":
    app = MainApp()
    app.run()