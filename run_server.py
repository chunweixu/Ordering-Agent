# run_server.py

from agent.agents import recognize_intent, guide_user, handle_faq, handle_order, confirm_order
import sys

def main():
    print("欢迎来到美味之家的AI点餐服务系统！请使用'退出', 'exit', 'quit'退出对话")
    history = []  # 用于保存对话历史
    
    while True:
        try:
            # 获取用户输入
            user_input = input("User: ").strip()
            
            # 检查退出条件
            if user_input.lower() in ["退出", "exit", "quit"]:
                print("感谢使用，再见！")
                break
            
            # 调用意图识别函数
            intent = recognize_intent(user_input, history[-2:])
            response = ""
            
            # 根据识别的意图调用相应的函数
            if "问答" in intent:
                response = handle_faq(user_input)
            elif "点餐" in intent:
                response = handle_order(user_input)
            elif "确认订单" in intent:
                response = confirm_order(user_input, history)
            else:
                response = guide_user(user_input, history[-4:])
            
            # 输出响应
            print(f"AI: {response}")
            
            # 更新对话历史
            history.append({"User": user_input, "AI": response})
        
        except KeyboardInterrupt:
            print("\n感谢使用，再见！")
            sys.exit(0)
        except Exception as e:
            print(f"发生错误: {str(e)}")
            continue

if __name__ == "__main__":
    main()
