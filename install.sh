cd $HOME
pkg update
pkg upgrade
cd TST
pip install -r requirements.txt
python tst.py