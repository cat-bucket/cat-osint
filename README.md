termux-change-repo
换源，选择一个国内的可以更快下载
pkg install git && pkg install python && git clone https://github.com/AdminWhaleFall/SMSBoom.git/ && cd SMSBoom && pip install -r requirements.txt && smsboom.py run -t 64 -p （替换你要的电话） -f 60