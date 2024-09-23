import tkinter as tk
from tkinter import messagebox, simpledialog
import requests
import os
import zipfile
import subprocess
import webbrowser

class NgrokSetupApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ngrok/Pyngrok Setup")
        
        self.selected_service = tk.StringVar(value="ngrok")

        # Service Selection
        tk.Label(root, text="Choose Ngrok or Pyngrok:").pack()
        tk.Radiobutton(root, text="Ngrok", variable=self.selected_service, value="ngrok").pack()
        tk.Radiobutton(root, text="Pyngrok", variable=self.selected_service, value="pyngrok").pack()

        # Install Button
        tk.Button(root, text="Install", command=self.install_service).pack(pady=10)

        # Token Input
        tk.Button(root, text="Enter Auth Token", command=self.enter_token).pack(pady=10)

        # Help Button
        tk.Button(root, text="Help", command=self.open_help).pack(pady=10)

        # Check for requests installation
        self.check_requests()

    def check_requests(self):
        try:
            import requests  # Try to import requests to check if it's installed
        except ImportError:
            messagebox.showinfo("Requests Not Found", "Installing requests library...")
            subprocess.run(["pip", "install", "--user", "requests"], check=True)
            messagebox.showinfo("Success", "Requests library installed.")

    def install_service(self):
        service = self.selected_service.get()
        if service == "ngrok":
            self.install_ngrok()
        else:
            self.install_pyngrok()

    def install_ngrok(self):
        try:
            # Download ngrok
            ngrok_url = "https://bin.equinox.io/c/111111/ngrok-stable-linux-amd64.zip"  # Update with the latest URL
            response = requests.get(ngrok_url)
            zip_path = "ngrok.zip"

            with open(zip_path, 'wb') as f:
                f.write(response.content)

            # Unzip ngrok
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall()
            
            # Move ngrok to a user directory
            ngrok_path = os.path.expanduser("~/ngrok")
            os.rename("ngrok", ngrok_path)
            os.chmod(ngrok_path, 0o755)
            messagebox.showinfo("Success", "Ngrok installed successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def install_pyngrok(self):
        try:
            # Install pyngrok via pip
            subprocess.run(["pip", "install", "--user", "pyngrok"], check=True)
            messagebox.showinfo("Success", "Pyngrok installed successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def enter_token(self):
        token = simpledialog.askstring("Auth Token", "Enter your ngrok auth token:")
        if token:
            # Create the ngrok configuration directory if it doesn't exist
            config_dir = os.path.expanduser("~/.ngrok2")
            os.makedirs(config_dir, exist_ok=True)

            # Save the auth token
            config_path = os.path.join(config_dir, "ngrok.yml")
            with open(config_path, 'a') as f:
                f.write(f"\nauthtoken: {token}")
            messagebox.showinfo("Success", "Auth token saved successfully.")

    def open_help(self):
        help_url = "https://ngrok.com/docs"
        webbrowser.open(help_url)

if __name__ == "__main__":
    root = tk.Tk()
    app = NgrokSetupApp(root)
    root.mainloop()
