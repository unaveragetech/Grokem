
---

# Ngrok/Pyngrok Setup GUI

This project provides a simple graphical user interface (GUI) for installing and configuring ngrok and pyngrok. Users can easily set up these tools without worrying about manual installations or configurations.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Functionality](#functionality)
- [Dependencies](#dependencies)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Features

- Choose between ngrok and pyngrok for tunneling.
- Automatic installation of required libraries.
- User-friendly prompts for auth token input.
- Links to ngrok documentation for additional support.
- Configuration files created automatically, ensuring smooth setup.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ngrok-pyngrok-setup.git
   cd ngrok-pyngrok-setup
   ```

2. **Ensure Python is installed**:
   This project requires Python 3.6 or higher. You can download it from [python.org](https://www.python.org/downloads/).

3. **Install required libraries**:
   The script will check for the `requests` library and prompt for installation if it's missing. Alternatively, you can manually install it by running:
   ```bash
   pip install --user requests
   ```

4. **Run the application**:
   ```bash
   python ngrok_pyngrok_setup.py
   ```

## Usage

1. Launch the application using the command above.
2. Select either **Ngrok** or **Pyngrok** from the radio buttons.
3. Click the **Install** button to download and install the selected service.
4. After installation, click **Enter Auth Token** to provide your ngrok auth token. The application will save this token in the appropriate configuration file.
5. For additional guidance, click the **Help** button to access ngrok's documentation.

## Functionality

- **Service Selection**: Choose between ngrok or pyngrok for your tunneling needs.
- **Installation Process**: The application downloads and installs the selected tool automatically, without requiring external commands.
- **Auth Token Configuration**: Users can easily enter their ngrok auth token, which is saved in the correct configuration directory.
- **Documentation Access**: Quick links to the official ngrok documentation for further assistance.

## Dependencies

- **Python 3.x**: Ensure Python is installed on your system.
- **Requests Library**: Automatically installed if not present.

## Troubleshooting

- **Installation Issues**: If you encounter issues during installation, make sure you have an active internet connection and the necessary permissions to install software.
- **Auth Token Not Saving**: Ensure the application has write permissions to the configuration directory (`~/.ngrok2`).

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

