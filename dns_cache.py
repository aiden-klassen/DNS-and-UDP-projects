import dns.resolver
import time
import json
import os

class DNSSimpleCache:
    def __init__(self, cache_file='dns_cache.json', cache_duration=10):
        self.cache_file = cache_file
        self.cache_duration = cache_duration  # Cache duration in seconds
        self.cache = self.load_cache()

    def load_cache(self):
        if os.path.exists(self.cache_file):
            with open(self.cache_file, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return {}
        return {}

    def save_cache(self):
        with open(self.cache_file, 'w') as f:
            json.dump(self.cache, f)

    def get(self, domain):
        if domain in self.cache:
            cached_data, timestamp = self.cache[domain]
            if time.time() - timestamp < self.cache_duration:
                return cached_data
            else:
                del self.cache[domain]  # Cache expired
        return None

    def set(self, domain, data):
        self.cache[domain] = (data, time.time())
        self.save_cache()

def query_dns(domain, cache):
    print(f"Current cache contents: {cache.cache}")  # Debugging cache before query
    cached_result = cache.get(domain)
    if cached_result:
        print(f"Using cached result for {domain}: {cached_result}")
        return cached_result

    print(f"Querying DNS for {domain}")
    resolver = dns.resolver.Resolver()
    try:
        answer = resolver.resolve(domain, 'A')
        ip_addresses = [str(ip) for ip in answer]
        print(f"Caching result for {domain}: {ip_addresses}")  # Debugging the result before caching
        cache.set(domain, ip_addresses)  # Cache the result
        print(f"Updated cache contents: {cache.cache}")  # Debugging cache after updating
        return ip_addresses
    except dns.resolver.NXDOMAIN:
        return f"Error: The domain {domain} does not exist."
    except dns.resolver.NoAnswer:
        return f"Error: No answer received for {domain}."
    except dns.resolver.Timeout:
        return f"Error: DNS query timed out."
    except dns.exception.DNSException as e:
        return f"DNS error: {e}"

if __name__ == "__main__":
    cache = DNSSimpleCache(cache_duration=10)  # Cache duration of 10 seconds for testing
    domain_name = input("Enter a domain to resolve: ")
    result = query_dns(domain_name, cache)
    print(f"Resolved IP(s) for {domain_name}: {result}")
