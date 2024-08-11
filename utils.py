import logging
import config
from http import HTTPStatus
import dashscope

dashscope.api_key = config.LLM_KEY

# 日志工具
def setup_logger(name, log_file, level=logging.INFO):
    """创建并配置日志工具"""
    handler = logging.FileHandler(log_file)        
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    
    return logger

# 创建一个全局日志器实例
logger = setup_logger('data/logs', 'project.log')

def call_llm_api(content):
    messages = [{'role': 'user', 'content': content}]
    responses = dashscope.Generation.call(
        "qwen2-7b-instruct",
        messages=messages,
        result_format='message',  # set the result to be "message" format.
        stream=True,  # set streaming output
        incremental_output=True  # get streaming output incrementally
    )
    
    response_content = ""  # 初始化一个空字符串来收集输出
    
    for response in responses:
        if response.status_code == HTTPStatus.OK:
            output_text = response.output.choices[0]['message']['content']
            response_content += output_text  # 将内容追加到response_content中
        else:
            error_message = (
                'Request id: %s, Status code: %s, error code: %s, error message: %s' % (
                response.request_id, response.status_code,
                response.code, response.message)
            )
            logger.error(error_message)  # 记录错误信息到日志
            print(error_message)
    
    # logger.info(f"API call completed with content: {response_content}")  # 记录成功信息到日志
    return response_content  # 返回生成的内容
