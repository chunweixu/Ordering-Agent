# agents.py

from .actions import intent_recognition_action, flow_guide_action, faq_action, order_action, confirm_order_action
from utils import logger


def recognize_intent(user_input, history=None):
    """
    识别用户输入的意图，并返回意图标签或识别结果。
    """
    intent = intent_recognition_action(user_input, history)
    logger.info(f"Recognizing intent for input: {user_input} as {intent}")
    return intent

def guide_user(user_input, history=None):
    """
    引导用户完成订餐等复杂流程。
    """
    logger.info(f"Guiding user through the process for input: {user_input}")
    response = flow_guide_action(user_input, history)
    return response

def handle_faq(user_input):
    """
    处理用户的常见问题。
    """
    logger.info(f"Handling FAQ for input: {user_input}")
    response = faq_action(user_input)
    return response

def handle_order(user_input):
    """
    处理用户的订餐请求。
    """
    logger.info(f"Handling order for input: {user_input}")
    response = order_action(user_input)
    return response

def confirm_order(user_input, history=None):
    """
    处理用户的订单确认请求。
    """
    logger.info(f"Confirming order for input: {user_input}")
    response = confirm_order_action(user_input, history)
    return response
