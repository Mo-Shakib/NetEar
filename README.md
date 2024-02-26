# NetEar: Network Device Monitor with Sound Alerts

NetEar is a simple Python script that monitors devices on your local network and plays different sounds when a device gets connected or disconnected. It uses ARP (Address Resolution Protocol) to detect devices and alerts the user in real-time.

## Features

- Scans the local network for connected devices using ARP.
- Plays a sound when a new device is detected.
- Plays a different sound when a device is disconnected.
- Customizable scan interval.

## Requirements

- Python 3.x
- Required Python packages (install using `pip install -r requirements.txt`):
- scapy

## Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/mo-shakib/NetEar.git
   ```

2. Navigate to the project directory:

   ```bash
   cd NetEar
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the script:

   ```bash
   python netear.py
   Press Ctrl + C to stop the script.
   ```

5. Configuration

   You can adjust the scan interval in the script (time.sleep()).
   You can change the sound files for connected and disconnected devices by replacing "connected_sound.mp3" and "disconnected_sound.mp3" respectively.

## Contributing
Contributions are welcome! If you have suggestions, feature requests, or found a bug, please open an issue or submit a pull request.

