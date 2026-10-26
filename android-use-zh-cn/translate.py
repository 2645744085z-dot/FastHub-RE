from pathlib import Path

root = Path("android-use")
translations = {
"Android Use":"安卓助手",
"Two things before the first task":"开始第一个任务前，请完成两项设置",
"Shizuku lets the agent touch the screen. Your ChatGPT plan is the model.":"Shizuku 允许助手操作屏幕；ChatGPT 套餐提供 AI 模型。",
"Connected.":"已连接。",
"Running, but Android Use isn't allowed to use it yet.":"Shizuku 正在运行，但尚未授权此应用使用。",
"Not running. Start it with wireless debugging or root, then come back.":"Shizuku 尚未启动，请使用无线调试或 Root 启动服务。",
"Open Shizuku":"打开 Shizuku",
"Sign in with the account whose plan should be used.":"请使用要消耗其套餐额度的 ChatGPT 账号登录。",
"Sign in":"登录",
"Sign out":"退出登录",
"Import auth.json":"导入 auth.json",
"Finish signing in in the browser. If the ChatGPT app opens instead or says your session ended, copy the link into a browser.":"请在浏览器中完成登录。如果错误跳转到 ChatGPT 应用，请复制链接在浏览器打开。",
"Link copied.":"已复制登录链接。",
"Copy link":"复制链接",
"Cancel":"取消",
"Allow":"允许",
"Approve":"批准",
"Deny":"拒绝",
"Approval needed":"需要审批",
"Try it":"试试看",
"Make default assistant":"设为默认助理",
"Change assistant":"切换助理",
"Assistant":"数字助理",
"Settings":"设置",
"New chat":"新对话",
"Chats":"聊天记录",
"Task steps":"任务步骤",
"Ask anything, or say what to do":"随便问，或告诉我想做什么",
"Finish setup first":"请先完成设置",
"Starting":"正在启动",
"Recent":"最近对话",
"Your chats will show up here.":"你的对话会显示在这里。",
"Not signed in":"未登录",
"Hi.\\nWhat's the plan?":"你好。\\n接下来要做什么？",
"Set a timer for 10 minutes":"设置一个 10 分钟计时器",
"What's the weather today?":"今天天气怎么样？",
"Turn on do not disturb":"开启勿扰模式",
"Text Anna I'm running late":"告诉安娜我会迟到",
"Close":"关闭",
"Back":"返回",
"Models":"模型",
"Main model":"主模型",
"Fast model":"快速模型",
"Both come from your ChatGPT plan.":"两个模型均使用你的 ChatGPT 套餐额度。",
"Reasoning effort":"推理强度",
"Task limits":"任务限制",
"Max steps per task":"任务最大步数",
"Sensitive actions":"敏感操作",
"Review automatically":"自动审核",
"Always ask me":"每次都先询问我",
"Reviewer model":"审核模型",
"Allow shell commands":"允许执行 Shell 命令",
"Report on WhatsApp":"WhatsApp 汇报",
"Send the outcome to a chat":"将任务结果发送到聊天",
"Chat name":"聊天名称",
"Memory":"记忆",
"Add memory":"添加记忆",
"Forget everything":"清空全部记忆",
"Forget everything?":"确定清空全部记忆？",
"Forget":"清空",
"Keep":"保留",
"Save":"保存",
"Edit":"编辑",
"Delete":"删除",
"Open in app":"在应用中打开",
"Minimize":"最小化",
"Ask anything, or say what to do on your phone.":"随便问，或者让我操作手机。",
"What's on my screen?":"当前屏幕有什么？",
"Screen attached":"已附加屏幕",
"Attach screen":"附加屏幕",
"Attach files":"添加文件",
"Copy":"复制",
"Read aloud":"朗读",
"Working on your phone":"正在操作手机",
"Done on your phone":"手机操作已完成",
"Couldn't finish":"未能完成",
"Stop":"停止",
"Hide details":"隐藏详情",
"Show details":"显示详情",
"Try again":"重试",
"What went wrong?":"哪里出了问题？",
"What did you do?":"刚才做了什么？",
"The task needs your answer":"任务需要你回答",
"Delete chat":"删除对话",
"Ask Android Use":"询问安卓助手",
"Listening…":"正在聆听…",
"Working…":"处理中…",
"Type your answer":"输入你的回答",
"Tell the agent what to change":"告诉助手要调整什么",
"Ask about this screen":"询问当前屏幕",
"Follow up or give feedback":"继续追问或反馈",
"Send":"发送",
"Speak":"语音输入",
"Shizuku connected":"Shizuku 已连接",
"Digital assistant app":"数字助理应用",
"Last screen":"最后一张屏幕截图",
"Refreshing…":"正在刷新…",
"Refresh":"刷新",
"Not loaded yet.":"尚未加载。",
"Codex usage":"Codex 使用额度",
"Limit reached. Tasks will fail until it resets.":"已达到额度上限，重置前任务无法完成。",
"This week":"本周",
"Low is fastest. Higher effort thinks longer on every step.":"低强度最快；高强度每步会思考更久。",
"Leave empty to use the main model for everything":"留空则全部使用主模型",
"Runs routine steps. The assistant chat also uses it.":"执行普通操作，助手聊天也使用此模型。",
"Takes over when a step fails or nothing changes. The only one allowed to finish a task.":"步骤失败或无进展时接管，只有主模型可以判定任务完成。",
"A step is one action on the phone. The task fails once this many are used.":"一步即一次手机操作，超过上限将终止任务。",
"You get a notification for every one and nothing happens until you answer.":"每个敏感操作都会通知你，确认前不会执行。",
"Shell commands and messages to people the task didn't name.":"Shell 命令和向任务中未指定的人发送消息。",
"Read-only queries are always allowed. This lets the agent change things with the shell after review. Destructive commands are always refused.":"只读命令始终允许；其他 Shell 命令经审批后执行，破坏性命令始终禁止。",
"Nothing yet. Tasks save what worked, and what you tell them, for next time.":"暂无记忆。助手会记住成功经验和你提供的信息。",
"Open an app":"打开应用",
"Task results":"任务结果",
"Running task":"正在执行的任务",
"Approval requests":"操作审批请求",
"Questions from tasks":"任务中的问题",
"Android Use has a question":"安卓助手有一个问题",
"Your answer":"你的回答",
"Reply":"回复",
"Answer":"回答",
"Steer":"调整任务",
"Android Use is working":"安卓助手正在运行",
"Preparing device":"正在准备设备",
"Working on task":"正在执行任务",
"Reporting to WhatsApp":"正在汇报到 WhatsApp",
"Stopped by user":"已由用户停止",
"Stopping":"正在停止",
"Done":"已完成",
"Failed":"失败",
"Stopped":"已停止",
"Saved to memory":"已保存到记忆",
"Delete memory":"删除记忆",
}
targets = [
    "ui/MainActivity.kt", "ui/Setup.kt", "ui/SettingsScreen.kt",
    "assistant/ChatUi.kt", "assistant/AssistantOverlay.kt",
    "assistant/AssistantActivity.kt", "assistant/Speech.kt",
    "assistant/Attachments.kt", "assistant/ChatEngine.kt",
    "agent/LiveNotification.kt", "agent/ResultNotification.kt",
    "agent/Approvals.kt", "agent/Questions.kt", "agent/TaskRunner.kt",
    "agent/AgentService.kt", "agent/Guard.kt"
]
src = root / "app/src/main/java/dev/pegoku/androiduse"
for rel in targets:
    path = src / rel
    data = path.read_text(encoding="utf-8")
    old = data
    for en, zh in translations.items():
        import json
        q = json.dumps(en, ensure_ascii=False)
        v = json.dumps(zh, ensure_ascii=False)
        data = data.replace(q, v)
    if rel == "ui/Setup.kt":
        data = data.replace(
            '''message = "Couldn't start sign-in: ${it.message}"''',
            '''message = if (it is java.net.BindException ||
                it.message?.contains("EADDRINUSE", ignoreCase = true) == true ||
                it.message?.contains("Address already in use", ignoreCase = true) == true
            ) {
                "登录端口 1455 已被占用。请先强制停止原版 Android Use，返回汉化版重试。如果仍失败，请重启手机。"
            } else {
                "无法启动登录：${it.message}"
            }'''
        )
        data = data.replace(
            '''"Replace Gemini: open Android Use over any app with long-press Home."''',
            '''"代替 Gemini：在任意应用中长按 Home 键即可唤出安卓助手。"'''
        ).replace(
            '''"Long-press Home to chat or ask for something over any app."''',
            '''"在任意应用中长按 Home 键，即可聊天或发出操作指令。"'''
        ).replace(
            '''if ("failed" in it || "Couldn't" in it)''',
            '''if ("失败" in it || "无法" in it || "端口" in it || "failed" in it || "Couldn't" in it)'''
        )
    if rel == "assistant/ChatEngine.kt":
        data = data.replace(
            "- Reply in the language the user writes in.",
            "- Reply in the language the user writes in, and use Simplified Chinese for Chinese messages."
        )
    if rel == "agent/Agent.kt":
        data = data.replace("Device locale: ${Locale.getDefault().toLanguageTag()}.","Device locale: ${Locale.getDefault().toLanguageTag()}. For Chinese owner instructions, respond in Simplified Chinese.")
    if data != old:
        path.write_text(data, encoding="utf-8")
        print("Translated", rel)
strings = root/"app/src/main/res/values/strings.xml"
strings.write_text('<resources>\n    <string name="app_name">安卓助手</string>\n</resources>\n', encoding="utf-8")
gradle = root/"app/build.gradle.kts"
body=gradle.read_text(encoding="utf-8").replace('applicationId = "dev.pegoku.androiduse"','applicationId = "dev.pegoku.androiduse.zhcn"')
gradle.write_text(body,encoding="utf-8")
manifest = root/"app/src/main/AndroidManifest.xml"
manifest.write_text(manifest.read_text(encoding="utf-8").replace('android:taskAffinity="dev.pegoku.androiduse.assistant"','android:taskAffinity="dev.pegoku.androiduse.zhcn.assistant"'),encoding="utf-8")
print("Done: UI translation, own app id and app label")
