FROM manimcommunity/manim:latest

RUN pip install --upgrade pip

RUN pip install networkx matplotlib
