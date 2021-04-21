CLI Tool Readme

Capturing activity for creating this tool from a Liveproject class.

1. Create CLI Skeleton and CI/CD Pipeline
    4/7/2021
    Task: Install git
    -Required installing Homebrew
        - /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
        - brew update
        - brew doctor
        - Apple version of Git was installed. Install the full version
            - git version 2.24.3 (Apple Git-128)
            - brew install git
            - git version 2.31.1
        - Configure git and set editor and diff tool to VSCode
            - git config --list --show-origin
            - git config --global user.name "Bob Glass"
            - git config --global user.email "glassrmux@gmail.com"
            - git config --global -e
        - Install gui tools
            - brew install git-gui
Roberts-MBP:src robertglass$ git config --global core.editor "code --wait"

        - Decision: User Github or Bitbucket?
            - Looking for a free private repo
            - Choice: github since that's what I use everyday

    Task: Use Poetry to create a new project directory in Source Control
        - poetry new CLI_Tool
        - git init
        - git add .
        - git commit -m 'Initial project version'
        - git branch -M main
        - Create a personal access token and use it as your password.
            - https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token
        - git remote add origin https://github.com/<username>/CLI_Tool.git
        - git push -u origin main

RESOURCES:
    - Python Setup and Usage
        - https://docs.python.org/3/using/index.html
    - Distributing Python Applications on the Mac
        - https://docs.python.org/3/using/mac.html
    - Chapter 11: Python Programs (using argparse)
        - https://livebook.manning.com/book/the-quick-python-book-third-edition/chapter-11/44

TODO:
    - git add LICENSE
    - find GUI tools
