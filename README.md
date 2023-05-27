# Rzhomba  
pip install pyaudio pyautogui  

(optional)  
pip install pyinstaller  
  
# Build package
pyinstaller --name=main --add-data="wouea.wav;." --add-data="ico.ico;." --ico "ico.ico" --onefile--windowed main.py