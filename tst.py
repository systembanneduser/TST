a
    �l�`�  �                   @   sF  d Z dZdZdZdZdZdZdZdZd	Z	d
Z
dZdZdZddlZddlZddlZzBddlZddlmZmZmZ ddlmZmZ ed� e�d� W nj ey�   ed� e�d� ed� e�d� ed� ddlZddlmZmZmZ ddlmZmZ Y n0 dd� Zdd� Zdd� Zdd� Zd d!� Z d"d#� Z!d$d%� Z"e�  e"�  dS )&z[0mz[31mz[1;32mz[33mz[34mz[35mz[36mz[37mz[31;1mz[32mz[33;1mz[34;1mz[35;1mz[36;1m�    N)�TelegramClient�sync�utils)�PeerFloodError�InputUserDeactivatedErrorz2[35m  [[33m*[35m][1;32m Required Modules Found�   z5[35m  [[33m*[35m][31m Required Module Not Found !z[1;32m Installing !zpip install telethon z+[35m  [[33m*[35m][35m Module Installed!c                  C   s�   t �  tj�d�rt�  n�t �  td� td� td�} td� td�}tdd��P}|�d|  d d	 | d � |�	�  td� td
� t
�d� W d   � n1 s�0    Y  t�  d S )N�
TSTlog.txtzD[35m  [[33m*[35m][1;32m Enter Your data for your Saving Process � z4[35m  [[33m*[35m][33m Enter your Telegram Id >> z6[35m  [[33m*[35m][36m Enter your Telegram Hash >> �az[*] Your Telegram Api_ID = �
z[*] Your Telegram Api_HASH = z'[35m  [[33m*[35m][34m Data Saved ! r   )�banner�os�path�isfile�menu�print�input�open�write�close�time�sleep)�api_id�api_hash�f� r   �tst.py�save+   s     (r   c                   C   s4   t d� t�d� t d� t d� t d� t�  d S )Nz0[35m  [[33m*[35m][35m Thank You . Stay Safe.r   r	   z"[35m  [[33m*[35m][31mEXPECT US)r   r   r   �quitr   r   r   r   �exit@   s    
r   c                   C   sJ   t �d� t �d� t�d� td� td� td� td� td� d S )N�clearztoilet -f mono12 -F gay " TST"r   r	   z=[1;32m         ----- TELEGRAM [35mSPAM [36mTOOL V 2.0-----z>[35m  [[33m*[35m][1;32mDEVELOPED [33mBY [36mDEVIL MASTER)r   �systemr   r   r   r   r   r   r   r   K   s    


r   c            
   
   C   s�  t �  z�t�d� td� td�} td� td�}td� | }|}td||��� }td�}td� zttd��}W n ty�   d}Y n0 td� td	�}t	|�D ]D}|�
||� tj�d
�|d |�� tj��  td� t�d� q�W n� tjjj�y   td� td� Y n� t�y4   td� t�  Y n� t�yT   td� t�  Y nt t�yt   td� t�  Y nT t�y�   td� t�  Y n4 t�y� }	 ztd� t�  W Y d }	~	n
d }	~	0 0 d S )N�cat TSTlog.txtr	   z6[35m  [[33m*[35m][1;32m Enter your Telegram Id >> z8[35m  [[33m*[35m][1;32m Enter your Telegram Hash >> �clientz=[35m  [[33m*[35m][36m TST > [33mTST > Set USERNAME/ID : z2[35m  [[33m*[35m][36m TST > [33mSet Count :  �d   z8[35m  [[33m*[35m][36mTST > [33mTST > Set Message : z0[1000D[*] [1;32mSent {} [36mmessages to {}...r   z'
[35m  [[33m*[35m][33m Done ... !!
zQ[35m  [[33m*[35m][36m The phone number is invalid (caused by SendCodeRequest)zU[35m  [[33m*[35m][33m You need to register your phone number first into Telegram
z9[35m  [[33m*[35m][37m [!] [36mClosing the program...zL[35m  [[33m*[35m][37m [!] Connection Error ! [36mClosing the program...zc[1;32mGetting Flood Error from telegram. Script is stopping now. Please try again after some time.z+The specified user was deleted. Skipping...z*[35m  [[33m*[35m][37m [!] [36mError: )r   r   r!   r   r   r   �start�int�
ValueError�rangeZsend_message�sys�stdoutr   �format�flushr   r   �telethon�errorsZrpcerrorlistZPhoneNumberInvalidError�KeyboardInterruptr   �EOFErrorr   r   �	Exception)
ZenterZrespor   r   r#   �target�countZurmsg�x�er   r   r   �mainY   sR    





r6   c                   C   sD   t �  td� t�d� td� t�d� td� td� t�  d S )Nz[31mFetching Datar   z)[36mA new Update Will Download & installzgit pullr	   z-[31m Updated ... [34m Restart The Script ! )r   r   r   r   r   r!   r   r   r   r   r   �update�   s    

r7   c                  C   s�   t �d� t�  t �d� td� td� td� td� td� td� td� td� td� td	� td� td
� td� td�} | dkr�t�  nt�  d S )Nr    z:fortune | cowsay -f eyes | toilet --metal -f term | lolcatr	   zx[35m  [[33m*[35m][1;32m 1.TST is a fully completed python based script which is made for spamming a telegram user . z@[35m  [[33m*[35m][1;32m 3.Read readme.md For More Details . zY[35m  [[33m*[35m][36m Support me & Report Bugs >> Github - https://github.com/isuruwaz^[35m  [[33m*[35m][34m          >>Facebook - https://www.facebook.com/isuru.umayanga.37819 zK[35m  [[33m*[35m][34m          >>Telegram - https://t.me/@Fsocietyadmn z9[35m  [[33m*[35m][31m -------- HELP -----------------zY[35m  [[33m*[35m][1;32m To Get Your Telegram ID & HASH Go To https://my.telegram.org z6[35m  [[33m*[35m][1;32m Press Enter To Continue : )r   r!   r   r   r   r   r   )�inpr   r   r   �about�   s(    

r9   c                  C   sx  t �d� t�  td� t �d� td� td�} t�d� t �d� t�  td� td� td� td� td� td	� td
� td� td� td� td�}|dkr�t�  |dkr�t �d� td� td� t�  |dk�rt �	d� td� t�d� t�  |dk�rt �d� |dk�r*t
�  |dk�r:t�  |dk�rJt�  |dk�r\t�  ntd� t�d� t�  d S )Nr    r	   z9cowsay -f ghostbusters DEVELOPED BY DEVIL MASTER | lolcatz5[35m  [[33m*[35m][1;32mPress Enter To Continue : r   z([35m  [[33m*[35m][34m 1.Start Bomberz([35m  [[33m*[35m][1;32m 2.Saved Logsz&[35m  [[33m*[35m][33m 3.Clear Logsz&[35m  [[33m*[35m][36m 4.More Toolsz'[35m  [[33m*[35m][35m 5.Update Toolz#[35m  [[33m*[35m][1;32m 6.Aboutz [35m  [[33m*[35m][36m 7.Exitz1[35m  [[33m*[35m][36m Enter Your Option  >>> �1�2r"   z4[35m  [[33m*[35m][34m Press Enter To Continue : �3r   z[31mLOG CLEARED �   �4zDam start -a android.intent.action.VIEW -d https://github.com/isuruwa�5�6�7z([35m  [[33m*[35m][31m Invalid Choice)r   r!   r   r   r   r   r   r6   r   �remover7   r9   r   )Zinor8   r   r   r   r   �   sZ    














r   )#�W�R�G�O�B�P�CZGR�rr
   �y�b�m�cr   r)   r   r-   r   r   r   Ztelethon.errors.rpcerrorlistr   r   r   r   �ModuleNotFoundErrorr!   r   r   r   r6   r7   r9   r   r   r   r   r   �<module>   sL   

0<