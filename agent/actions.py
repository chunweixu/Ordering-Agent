# actions.py

import yaml
from utils import call_llm_api

# 加载prompts.yaml
with open("data/prompts.yaml", 'r', encoding='utf-8') as file:
    prompts = yaml.safe_load(file)

def intent_recognition_action(user_input, history=None):
    """
    调用LLM API进行意图识别，并返回结果。
    """
    prompt_template = prompts["intent_recognition"]
    prompt = prompt_template.format(
        personality=prompts["personality"],
        history=history or "无",
        user_input=user_input
    )
    return call_llm_api(prompt)

def flow_guide_action(user_input, history=None):
    """
    调用LLM API进行流程引导，并返回结果。
    """
    prompt_template = prompts["flow_guidance"]
    prompt = prompt_template.format(
        personality=prompts["personality"],
        history=history or "无",
        menu=prompts["menu"],
        user_input=user_input
    )
    return call_llm_api(prompt)

def faq_action(user_input):
    """
    调用LLM API处理FAQ请求，并返回结果。
    """
    prompt_template = prompts["faq_response"]
    prompt = prompt_template.format(
        personality=prompts["personality"],
        restaurant_info=prompts["restaurant_info"],
        menu=prompts["menu"],
        user_input=user_input
    )
    return call_llm_api(prompt)

def order_action(user_input):
    """
    调用LLM API处理订餐请求，并返回结果。
    """
    prompt_template = prompts["order_processing"]
    prompt = prompt_template.format(
        personality=prompts["personality"],
        menu=prompts["menu"],
        user_input=user_input
    )
    return call_llm_api(prompt)

def confirm_order_action(user_input, history=None):
    """
    调用LLM API处理订单确认请求，并返回结果。
    """
    prompt_template = prompts["order_confirmation"]
    prompt = prompt_template.format(
        personality=prompts["personality"],
        history=history or "无",
        menu=prompts["menu"],
        user_input=user_input
    )
    return call_llm_api(prompt)
