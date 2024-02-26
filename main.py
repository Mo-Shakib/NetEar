import scapy.all as scapy
import time
import subprocess

def scan_and_alert(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def play_sound(sound_file):
    subprocess.run(["afplay", sound_file])

if __name__ == "__main__":
    ip_range = "192.168.0.1/24"   
    known_devices = set()  # Store MAC addresses of known devices

    connected_sound = "connected_sound.mp3"
    disconnected_sound = "disconnected_sound.mp3"

    while True:
        try:
            print("Scanning...")
            results = scan_and_alert(ip_range)

            # Check for new devices
            for client in results:
                if client['mac'] not in known_devices:
                    print(f"[=] New device detected! IP: {client['ip']}\t MAC: {client['mac']}")
                    known_devices.add(client['mac'])
                    play_sound(connected_sound)

            # Check for disconnected devices
            disconnected_devices = known_devices - {client['mac'] for client in results}
            for mac in disconnected_devices:
                print(f"[!] Device disconnected! MAC: {mac}")
                known_devices.remove(mac)
                play_sound(disconnected_sound)

            time.sleep(3)  # Adjust scan interval (in seconds)

        except KeyboardInterrupt:
            print("\nExiting...")
            break
