# DNS-and-UDP-projects

# DNS Resolver with Simple Caching

This is a Python script that resolves domain names to IP addresses using the `dnspython` library. It includes a simple caching mechanism to reduce repeated DNS lookups within a specified time period.

## Features

- Resolves A records (IPv4 addresses) for a given domain.
- Implements a file-based cache using JSON to store recent DNS query results.
- Avoids repeated lookups for the same domain within a configurable cache duration.
- Gracefully handles common DNS errors (e.g. NXDOMAIN, NoAnswer, Timeout).
- Cache duration is set to 10 seconds by default but can be adjusted.

## How It Works

1. When a domain is queried:
   - If it exists in the cache and hasn't expired, the cached result is returned.
   - If it's not cached or the cache is expired, a fresh DNS query is performed.
2. The result is printed and cached for future use.
3. Cache is stored in `dns_cache.json` in the script's directory.

## Requirements

- Python 3.x
- `dnspython` library

- About Me
I am Aiden Klassen, a Network Security and Engineering student passionate about networking, systems engineering, and automation. I enjoy applying theoretical knowledge through practical projects to build efficient and secure network solutions.


## Installation

Install the required package:

```bash

pip install dnspython

aidenklassen10@gmail.com
Linkedin: Aiden KLassen https://www.linkedin.com/in/aiden-klassen-332588331/

aidenklassen10@gmail.com
