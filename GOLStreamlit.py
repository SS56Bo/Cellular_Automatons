import streamlit as st
import threading 
from gameOfLife import *

st.title("Game of Life")
st.write("The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. It is Turing complete and can simulate a universal constructor or any other Turing machine.")

if st.button("Start Game of Life"):
    pygame_thread = threading.Thread(target=main)
    pygame_thread.start()