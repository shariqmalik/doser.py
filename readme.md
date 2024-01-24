# Doser.py
>A python based DoS Tool for HTTP Requests

## Description
This tool is a Denial of Service (DoS) tool designed to send a high volume of HTTP requests to a target server, causing it to become overwhelmed and unavailable to legitimate users.

## Features
- Sends a large number of HTTP requests to a target server
- Supports different types of HTTP requests (GET, POST, etc.)
- Provides options for controlling the rate and intensity of the attack

## Installation
1. Clone the repository: `git clone https://github.com/shariqmalik/doser.py.git`
2. Install the required dependencies: `pip install -r requirements.txt`

## Usage
1. Open the terminal and navigate to the project directory.
2. Run the DoS tool: `python doser.py -h`
3. Follow the on-screen instructions to configure the attack parameters.

```
 ________      ______    ________  _______   _______
|"      "\    /    " \  /"       )/"     "| /"      \
(.  ___  :)  // ____  \(:   \___/(: ______)|:        |
|: \   ) || /  /    ) :)\___  \   \/    |  |_____/   )
(| (___\ ||(: (____/ //  __/  \\  // ___)_  //      /
|:       :) \        /  /" \   :)(:      "||:  __   \
(________/   \"_____/  (_______/  \_______)|__|  \___)

                                ~> by Shariq Malik <~

usage: doser.py [-h] -u URL [-t THREADS] [-c] [-x PROXY] [-v]

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     The URL to attack
  -t THREADS, --threads THREADS
                        Number of threads to use
  -c, --continue-on-error
                        Continue on error
  -x PROXY, --proxy PROXY
                        Proxy to use e.g. http://127.0.0.1:8080
  -v, --verbose         Verbose output

usage examples:
    Start attack with 100 threads:
        python doser.py -u https://example.com

    Start attack with 1000 threads:
        python doser.py -u https://example.com -t 1000

    Start attack with continue on error":
        python doser.py -u https://example.com -c

    Start attack with proxy:
        python doser.py -u https://example.com -x http://<ip>:<port>

    Start attack with verbose output:
        python doser.py -u https://example.com -v
```

## Disclaimer
Please note that launching DoS attacks against unauthorized targets is illegal and unethical. This tool should only be used for educational purposes or with explicit permission from the target owner. The developer of this tool is not responsible for any misuse or damage caused by the tool.

## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
