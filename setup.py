#!/usr/bin/python3

# Owen Watkins
# Script to set up a bare debian based linux environment how I want
# Initial develop on 1/18/2020

import os
from os import path


reqs = [] # Array to hold individual requirements

# Will use boolean input many times
def is_true(inp):
    if (inp.lower() != "y" and inp != ""):
        return False
    else:
        return True
# Ensuring root here will allow the script to run through
def check_if_root():
    is_root = input("Are you in root? [Y/n]")
    if (is_true(is_root)):
        print ("Your are root, installing git and continuing on...")
        return False
    else:
        print ("This should be run as root, please change to root access and rerun.")
        return True

# Get the requirements file
def get_reqs():
    with open("requirements.txt", "r+") as reqs_file:
        r_lines = reqs_file.readlines()
        for r in r_lines:
            reqs.append(r)
        for rq in reqs:
            try:
                os.system(f"apt install {rq} -y")
            except OSError:
                print (f"{rq} did NOT install")
# Install on my zsh and configure
def zsh():
    os.system("apt install zsh -y")
    os.system("curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh")
    z_file = open("~/.zshrc", "a+")
    z_file.write("alias upy='sudo apt update && sudo apt upgrade -y && sudo apt autoremove'\n")
    z_file.close()

def vim():
    v_file = open("~/.vimrc", "a+")
    v_file.write("")
    v_file.close()

# main program
def main():
    # Check if root
    check_if_root()
    # do update and upgrade
    os.system("apt update && apt upgrade -y")
    print ("Installing git...")
    os.system("apt install git -y")
    # some base applications
    print ("Installing curl...")
    os.system("apt install curl -y")
    # check if there is a requirements file
    print ("Checking for requirements.txt file...")
    f = path.exists("requirements.txt")
    # Do apt installs from reqs doc
    if (f):
        print ("Requirements file found, installing apps...")
        get_reqs()
    # Install oh my zsh and modify .zshrc
    print ("Installing Oh my zsh...")
    zsh()
    # pull dotfiles
    os.system("git pull https://github.com/ogre14t/Dotfiles ~/")
