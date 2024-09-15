import socket
import argparse

def connect_to_server(host='localhost', port=5000, command=''):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
            
            # Invia il comando al server
            s.sendall(command.encode())
            
            # Ricevi la risposta dal server
            data = s.recv(1024)
            if not data:
                print("No response from server. Exiting...")
                exit()
            
            print(data.decode())
        
        except ConnectionRefusedError:
            print(f"Unable to connect to the server at {host}:{port}. Ensure the server is running.")

if __name__ == "__main__":
    # Configurazione dell'analisi degli argomenti
    parser = argparse.ArgumentParser(description='Client to connect to server and send commands.')
    parser.add_argument('command', type=str, help='The command to send to the server.')
    parser.add_argument('--host', type=str, default='localhost', help='The host of the server. Default is localhost.')
    parser.add_argument('--port', type=int, default=5000, help='The port of the server. Default is 5000.')

    # Analisi degli argomenti
    args = parser.parse_args()

    # Connessione al server con i parametri specificati
    connect_to_server(host=args.host, port=args.port, command=args.command)
