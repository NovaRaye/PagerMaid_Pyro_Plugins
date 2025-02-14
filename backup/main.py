from pagermaid.listener import listener

@listener(incoming=True, outgoing=True, disable_edited=True)
async def log_all_messages(msg):
    print(f"【PagerMaid-Pyro】消息：{msg}")
