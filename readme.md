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

    Task: Configure "poetry run" for executing python scripts
        - Also finish configuration of poetry 
            - https://python-poetry.org/docs/
                - Enable tab completions
                    - poetry completions bash > $(brew --prefix)/etc/bash_completion.d/poetry.bash-completion
                    - but then switched to zsh so had to run this instead
                        - poetry completions zsh > ~/.zfunc/_poetry
        - Resource: https://python-poetry.org/docs/pyproject/#scripts
            - added this to ~/src/CLI_Tool/pyproject.toml
                    [tool.poetry.scripts]
                    poetry = 'poetry.console:run'
        - Found that adding execute permission to my .py script was needed.
            - chmod +x ./klickbrick.py

    Task: Write this program, poetry run klickbrick hello
        - should print “Hello World".
    Task: modify program to take parameters, poetry run klickbrick hello --name Ole
        - should print “Hello Ole”.
            Tip: Think of “Klickbrick” as the program, “hello” as the command, and “–name” as a flag which takes the argument “Ole.” 

    Task: write a unit test
        - Resource: https://docs.python.org/3/library/unittest.html#basic-example
RESOURCES:
    - Python Setup and Usage
        - https://docs.python.org/3/using/index.html
    - Poetry for dependecy management and packaging
        - https://python-poetry.org/docs/
    - Distributing Python Applications on the Mac
        - https://docs.python.org/3/using/mac.html
    - Chapter 11: Python Programs (using argparse)
        - https://livebook.manning.com/book/the-quick-python-book-third-edition/chapter-11/44

TODO:
    - git add LICENSE
    - investigate need for she-bang need, #!/usr/bin/env python
    -
  

Cards:
Linting
poetry
bash
zsh
