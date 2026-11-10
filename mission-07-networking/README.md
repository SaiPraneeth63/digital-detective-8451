# Mission 7 - Computer networks

## 1. Task/objective
Explain basic network types and concepts, observe network connectivity and DNS lookup information, and describe what happens step-by-step when a website opens.

## 2. Work completed
- Completed the network concepts and definitions table covering LAN, MAN, WAN, DNS, routers, and protocols.
- Performed terminal connectivity tests (`ping`) and DNS lookups (`nslookup`).
- Documented a 7-step breakdown explaining client-server communication when opening a website.

## 3. Commands / tools used
- `ping`: Tests network connectivity and reachability to a remote host.
- `nslookup`: Queries Domain Name System (DNS) servers to find IP addresses.
- Terminal and Visual Studio Code: Used for execution and documentation.

## 4. My understanding
Computer networks connect devices to share data and resources globally. Local networks (LAN) cover small spaces, while wide networks (WAN) span continents. Protocols govern how data is packaged and transmitted, and DNS translates human-readable domain names into machine-readable IP addresses so browsers can locate web servers.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- `mission-07-networking/README.md`

### Task 7.1: Network Concepts
| Concept | Explain it in your own words | Example |
| :--- | :--- | :--- |
| LAN (Local Area Network) | A network covering a small geographical area, such as a home, office, or school lab. | Home Wi-Fi network connecting laptops and phones . |
| MAN (Metropolitan Area Network) | A network spanning across a city or large campus area, larger than a LAN but smaller than a WAN. | A city-wide public Wi-Fi or cable television network. |
| WAN (Wide Area Network) | A network connecting computers across large geographical regions, countries, or globally. | The Internet. |
| DNS (Domain Name System) | Translates human-readable domain names into numerical IP addresses. | Converting `google.com` into an IP address. |
| Router | A networking device that connects different networks and forwards data packets between them. | Home router forwarding data between local devices and the ISP. |
| Protocol | A standardized set of rules and formats that devices follow to communicate successfully. | HTTP, HTTPS, or TCP/IP. |
| Packet switching | Data is broken down into small packets that travel independently across a network and reassemble at the destination. | Splitting a video stream into data packets across the internet. |
| Client-server | An architecture where a client (browser) requests a service or data, and a server provides it. | Web browser requesting a webpage from a web hosting server. |

### Task 7.3: What Happens When You Open a Website? (7-Step Breakdown)
1. User Input: The client (web browser) receives the URL entered by the user.
2. DNS Resolution: The browser queries the DNS server to translate the domain name into the server's numerical IP address.
3. Establishing Connection: Using the IP address, the client initiates a network connection request following standard communication protocols (like TCP/IP and HTTPS).
4. Routing: Network routers forward data packets across the internet from the client to the destination server.
5. Server Processing: The remote web server receives the request, processes it, and retrieves the necessary webpage assets.
6. Response Transmission: The server sends the requested data back to the client in structured packets via the network.
7. Rendering: The client browser receives, reassembles, and renders the data packets into a visual webpage displayed to the user.

## 8. Commit details
- Commit message: "Explain networking concepts and website communication"
- Pushed successfully to GitHub.