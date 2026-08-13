#!/usr/bin/env python3
# ZANZY OTP SPAMMER v3.1 - BY @violexzy

import os, sys, time, random, threading, platform
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

BANNER = f"""
{Fore.RED}╔══════════════════════════════════════════════════════════════╗
{Fore.RED}║{Fore.WHITE}   ███████╗ █████╗ ███╗   ██╗███████╗██╗   ██╗     {Fore.RED}║
{Fore.RED}║{Fore.WHITE}   ╚══███╔╝██╔══██╗████╗  ██║╚══███╔╝╚██╗ ██╔╝     {Fore.RED}║
{Fore.RED}║{Fore.WHITE}     ███╔╝ ███████║██╔██╗ ██║  ███╔╝  ╚████╔╝      {Fore.RED}║
{Fore.RED}║{Fore.WHITE}    ███╔╝  ██╔══██║██║╚██╗██║ ███╔╝    ╚██╔╝       {Fore.RED}║
{Fore.RED}║{Fore.WHITE}   ███████╗██║  ██║██║ ╚████║███████╗   ██║        {Fore.RED}║
{Fore.RED}║{Fore.WHITE}   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝        {Fore.RED}║
{Fore.RED}║                                                          {Fore.RED}║
{Fore.RED}║   {Fore.YELLOW}>> ZANZY OTP SPAMMER v3.1 <<{Fore.RED}               ║
{Fore.RED}║   {Fore.GREEN}>> BY @violexzy <<{Fore.RED}                           ║
{Fore.RED}╚══════════════════════════════════════════════════════════════╝
{Fore.RESET}"""

print(BANNER)
print(f"{Fore.GREEN}[+] ZANZY OTP SPAMMER READY{Style.RESET_ALL}")
