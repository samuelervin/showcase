# Project that Showcases Python Projects

This project is to showcase some of the projects you may be doing in python. It is written entirely in python and uses streamlit as the web framework.

The reason I engaged in building this was completing a python refresher for myself on Udemy. The course is Ardit Sulce's - Python Mega Course: Learn Python in 60 Days, Build 20 Apps. It is a fun interactive class for beginners and even us more salty developers to quickly poke about remembering things if we don't use Python daily. I also like the approach of building a useful app during learning. It reminds me of my professors way back when that gave us more fun projects than simply parsing a memory stack in a variety of ways. Ardit also operate https://pythonhow.com/ which he has a unique daily python program email where he will send you a daily project varying in complexity that just helps to keep your python wits about you and keep up a bit. It also helps you learn new things if you are not totally focused on Python in your daily walk at work. 

 To get more info on streamlit go here https://streamlit.io/


## Main Layout
- Home page
  - Picture of Owner and Brief Biography
  - Apps with Icon Pictures and source code links
- Contact Page
  - Basic Email form (Sender, Message ) using SMTP connected to a GMAIL account currently with OS ENV variables for gmail and google app password. 

## Getting Started Using
- Setup 
  - clone the repo 

    ``` 
    git clone https://github.com/samuelervin/showcase.git
    ```
- Depending on if you are using PyCharm or VSCode create a venv in python. 
  - cmd + shift + p in VSCode select Create Python Virtual Environment
  - In PyCharm I believe it creates them for you 
  - manual fun way https://docs.python.org/3/library/venv.html, it's also in the Udemy course as well 
    ```
        # navigate to the project folder in the terminal
        python -m venv /path/to/new/virtual/environment
        python -m venv /app_portfolio 

        # activate your environment
        source .venv/bin/activate  #mac 

    ```
- Install streamlit in your environment 
  ```
    pip install streamlit
  ```

- To just run it and use the contact page you will need to add the environment variables
```
    export GMAIL_EMAIL="<yourgemailaccount>@gmail.com" 
    export GMAIL_APP_PASSWORD="<your gmail app pass>"
```
- Now you can run it. 
```
    strealit run Home.py
    # or 
    streamlit run app_portfolio/Home.py
```

## Comments or Questions

- I do welcome any comments or questions if you came upon this.    
  - If you have anything helpful to make this better please share.
  - If you have trouble getting it to work I will help however I can to get it running on your machine. 
  - To make this more effective reachout through GitHub issues or email me.