a
    �.*`
  �                   @   s<  d dl Z d dlmZ d dlmZ d dlmZmZmZ d dl	m
Z
mZ d dlmZ d dlZd dlZd dlZd dlZd dlZd dlmZmZ d dlmZ d dlZd dlZd	Zd
ZdZeeee�Ze��  dd� Zdd� Zdd� Zdd� Zdd� Z dd� Z!dd� Z"dd� Z#e� ej$�%e#� � W d  � n1 �s.0    Y  dS )�    N)�TelegramClient)�GetDialogsRequest)�InputPeerEmpty�InputPeerChannel�InputPeerUser)�PeerFloodError�UserPrivacyRestrictedError)�InviteToChannelRequest)�events�	functions)�JoinChannelRequesti�a9 Z 83a57e2b73cf0182db5e1f056c717eb7� c                   �   s   t d� d S )Na:  
 _       _             _           _     _
| |_ ___| | ___     __| |_ __ ___ (_) __| |
| __/ _ \ |/ _ \   / _` | '__/ _ \| |/ _` |
| ||  __/ |  __/  | (_| | | | (_) | | (_| |
 \__\___|_|\___|___\__,_|_|  \___/|_|\__,_|
              |_____|

         >>>> By client [xTx] <<<<
        [ https://t.me/Client558  ]
)�print� r   r   �../../tele_droid.py�bunner!   s    r   c                  �   st   t d�} tt d��}tt d��}t�d� t�d� d}td|�D ],}t�	| |�I d H  t
d�|�� |d7 }qBd S )N�1give me id or user name or phone number with + : zthe message : �number of messages : �   �clearr   �sending ... [{}])�input�str�int�time�sleep�os�system�range�client�send_messager   �format)�usZnum2�o�ir   r   r   r    0   s    

r    c                  �   s\   t d�} t d�}tt d��}d}td|�D ],}t�| |�I d H  td�|�� |d7 }q*d S )Nr   z'give me location file in your sdcard : r   r   r   r   )r   r   r   r   �	send_filer   r!   )ZtarZtar_fileZnum_smr$   r   r   r   r%   =   s    r%   c                  �   s4   t d�} t�| �2 z3 d H W }t|j|j� q6 d S )NzBfor see messages in on chat give me id or user or number with + : )r   r   Ziter_messagesr   �id�text)Ztar1�messager   r   r   �see_messageH   s    r)   c               
   �   s�  g } d }d}g }t t|dt� |dd��I d H }| �|j� | D ].}z|jdkrX|�|� W q>   Y q>Y q>0 q>td� d}|D ]*}tdt|� d d |j	 � |d	7 }q~td
� t
d�}|t|� }	td� t�d	� g }
t j|	dd�I d H }
td� t�d	� tdddd���}tj|ddd�}|�g d�� |
D ]p}|j�rH|j}nd
}|j�r\|j}nd
}|j�rp|j}nd
}|d | �� }|�||j|j||	j	|	jg� �q4W d   � n1 �s�0    Y  td� d S )N��   r   )Zoffset_dateZ	offset_idZoffset_peer�limit�hashTz'[+] Choose a group to scrape members : �[�]z - r   r   z[+] Enter a Number : z[+] Fetching Members...)Z
aggressivez[+] Saving In file...zmembers.csv�azUTF-8)�encoding�,�
)Z	delimiterZlineterminator)�usernamezuser idzaccess hash�name�groupzgroup id� z![+] Members scraped successfully.)r   r   r   �extend�chatsZ	megagroup�appendr   r   �titler   r   r   r   Zget_participants�open�csv�writerZwriterowr3   �
first_name�	last_name�stripr&   Zaccess_hash)r8   Z	last_dateZ
chunk_size�groups�resultZchatr$   �gZg_indexZtarget_groupZall_participants�fr=   �userr3   r>   r?   r4   r   r   r   �save_memO   s`    �



BrF   c                  �   s   t d�} tt| ��I d H  d S )Nzuser channel :)r   r   r   )Zchannelr   r   r   �ser�   s    rG   c                   C   s   t �d� t �d� d S )Nr   z�
pip3 install cython numpy pandas
python3 -m pip install python numpy pandas	
pip3 install telethon requests configparser
python3 -m pip install telethon requests configparser
touch config.data
	)r   r   r   r   r   r   �install�   s    
rH   c                  �   s�  �z�t �d� d} d}td�| |�� td�}|dk�r�t� I d H  td� ttd��}t�d	� t �d� |d	kr�t	� I d H  t�d
� t �d� q8|dkr�t
� I d H  t�d
� t �d� q8|d
kr�t� I d H  q8|dkr�t�  t �d� q8|dk�rrt �d� td� ttd��}|d	k�r:t� I d H  t �d� n6|dk�r�t� I d H  t �d� t� I d H  t �d� q8|dk�r�td� t�d� t �d� q8|dkr8t��  q8ntd� td� W n t�y�   td� Y n0 d S )Nr   zhttps://t.me/TOSYNTzhttps://t.me/Client558zV
first follow this channel [{}]	
after that talk with me to give you password [{}]	
		zinput password : Z b447f475f3d915ee09061c12e12265f4a  
		[1] for send spam messages .
		[2] for send files or media (spam or not ).
		[3] for see messages from any chat .
		[4] fot install pakages [important for add or save] .
		[5] for saving users from chat .
		[6] for add members to chat .
		[10] for exit .			
		z	choose : r   �   �   �   �   z?[1] if you in chat . 
[2] if you not in chat  (for join now) : z>>>>	�   z0this part not aviliable now 
coming soon ......!�
   zwrong passwordz'subscripe the bot now and chek passwordznooooo try again)r   r   r   r!   r   r   r   r   r   r    r%   r)   rH   rF   rG   �sys�exit�KeyboardInterrupt)�q�rZkkkZinpuZrewr   r   r   �all�   sb    
�
	










rT   )&r<   Ztelethon.syncr   Ztelethon.tl.functions.messagesr   Ztelethon.tl.typesr   r   r   Ztelethon.errors.rpcerrorlistr   r   Ztelethon.tl.functions.channelsr	   r   rO   Zconfigparserr   Ztelethonr
   r   r   ZasyncioZapi_idZapi_hashZphoner   �startr   r    r%   r)   rF   rG   rH   rT   ZloopZrun_until_completer   r   r   r   �<module>   s8   @
F