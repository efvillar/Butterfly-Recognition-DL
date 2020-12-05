
from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the streamlit app"""
    Popen(
        [
            "streamlit", 
            "run", 
            "fish_app.py", 
            "--browser.serverAddress=0.0.0.0", 
            "--server.enableCORS=False",
            "--server.enableWebsocketCompression=false",
            "--server.enableXsrfProtection=false",
        ]
    )
