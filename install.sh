cd $HOME
pkg update
pkg upgrade
pkg install toilet
cd TST
pip install -r requirements.txt
python tst.py
