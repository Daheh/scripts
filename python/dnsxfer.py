#!/usr/bin/python3
import sys, argparse
import dns.query
import dns.zone
import dns.resolver
from colorama import Fore, Style

bracket = f"{Fore.BLUE}[{Fore.GREEN}*{Fore.BLUE}]{Style.RESET_ALL} "
bracket_err = f"{Fore.BLUE}[{Fore.RED}*{Fore.BLUE}]{Style.RESET_ALL} "

def resolveDNS(system):
    resolver = dns.resolver.Resolver()
    results = resolver.query(system , "A")
    return results
domain = 'megacorpone.com'
zone = dns.zone.from_xfr(dns.query.xfr('ns2.megacorpone.com', 'megacorpone.com'))
for host in zone:
    if str(host) != '@':
        A_records = resolveDNS(str(host) + "." + domain)
        for item in A_records:
            answer = ','.join([str(item)])
        print(bracket, "{:30}".format(str(host) + "." + domain), answer)
