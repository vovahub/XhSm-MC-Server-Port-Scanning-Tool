from mcstatus import JavaServer as java服务器, BedrockServer as 基岩服务器
import json
import threading
import time
import os
from datetime import datetime

logo = r'''
 __   __  __      ____                   
/\ \ /\ \/\ \    /\  _`\                 
\ `\`\/'/\ \ \___\ \,\L\_\    ___ ___    
 `\/ > <  \ \  _ `\/_\__ \  /' __` __`\  
    \/'/\`\\ \ \ \ \/\ \L\ \/\ \/\ \/\ \ 
    /\_\\ \_\ \_\ \_\ `\____\ \_\ \_\ \_\
    \/_/ \/_/\/_/\/_/\/_____/\/_/\/_/\/_/
     ----XhSm端口扫描工具为您服务~(´〜｀*)~zzz----

作者:Vovalu
作者b站:https://space.bilibili.com/3546654082861538?spm_id_from=333.1007.0.0
作者的qq群:971463342
如果该工具对您有用可以关注我bilibili嘛求求啦!QWQ
(该工具不是任何黑客工具,这只是一个普通服务器端口扫描工具,您只能用它来查询服务器)
'''

下载目录 = ""
try:
    下载目录 = os.path.join(os.path.expanduser("~"), "xhsm")
    os.makedirs(下载目录, exist_ok=True)
    print(f"OK数据存放文件夹检测成功/{下载目录}")
except Exception as e:
    print(f"ERROR数据存放文件夹检测失败/{e}")
    # 备用方案：使用当前目录
    下载目录 = os.getcwd()

class 服务器查询():
    # 需要: from mcstatus import JavaServer as java服务器, BedrockServer as 基岩服务器
    # 需要: import json
    # 需要: import threading
    # 需要: import time
    #列表数据格式: ["ip或者主机名","如果有端口在这里写端口"]
    # 这个函数已经写好了,可以直接复制粘贴使用(除非您不是新版python而且不是2缩进项目)
    def BE(列表数据):
        超时时长 = 5
        端口_默认_基岩 = "19132"
        if len(列表数据) == 1:
            主机 = 列表数据[0]
            服务器 = f"{主机}:{端口_默认_基岩}"
        elif len(列表数据) == 2:
            主机 = 列表数据[0]
            端口 = 列表数据[1]
            服务器 = f"{主机}:{端口}"
        try:
            服务器实例 = 基岩服务器.lookup(f"{服务器}", timeout=超时时长)
            # 基岩版只有status方法
            状态 = 服务器实例.status()
            print(f"基岩服在线: {状态.players.online}, 延迟: {状态.latency}ms")
            try:
                # 解析_解析对象
                motd_解析 = 状态.motd.parsed
                motd_原始 = 状态.motd.raw
                玩家_在线 = 状态.players.online
                玩家_最大 = 状态.players.max
                延迟 = 状态.latency
                服务器版本 = 状态.version.name
                协议版本 = 状态.version.protocol
                地图map = 状态.map_name
                游戏模式 = 状态.gamemode
                # -----------------------------
                # 解析_解析所有对象数据为json更加方便
                解析json = {
                    "sever":f"{服务器}",
                    "m":"BE",
                    "player(=)":f"{玩家_在线}",# 玩家在线值
                    "player(+)":f"{玩家_最大}",# 玩家最大值
                    "motd":f"{motd_原始}",# 原始motd数据
                    "ping":f"{延迟}",# 延迟
                    "s_v":f"{服务器版本}",# 服务器版本
                    "p_v":f"{协议版本}",# 协议版本
                    "icon":"",# 基岩没有icon
                    "map":f"{地图map}",# 地图map
                    "gm":f"{游戏模式}",# 协议版本
                }
                数据 = json.dumps(解析json, ensure_ascii=False)
                打印json = json.dumps(解析json, indent=2, ensure_ascii=False)
                print(f"解析为json成功:/n{打印json}")
                print("[OK]基岩方式查询成功")
                return 数据
            except Exception as e:
                pass # 是的仅仅抓取不处理(ps:偷点懒咋啦嘛)
        except Exception as e:
            pass
    # _________________分割_________________
    def JE(列表数据):
        超时时长 = 5
        if len(列表数据) == 1:
            主机 = 列表数据[0]
            服务器 = 主机
        elif len(列表数据) == 2:
            主机 = 列表数据[0]
            端口 = 列表数据[1]
            服务器 = f"{主机}:{端口}"
        try:
            # 获取状态信息
            服务器实例 = java服务器.lookup(f"{服务器}", timeout=超时时长)
            状态 = 服务器实例.status()
            print(f"服务器在线人数: {状态.players.online}, 延迟: {状态.latency}ms")
            # 此处把q查询给去掉了,大部分服务器不开而且查询很耗时
            try:
                # 解析_解析对象
                motd_解析 = 状态.motd.parsed
                motd_原始 = 状态.motd.raw
                玩家_在线 = 状态.players.online
                玩家_最大 = 状态.players.max
                延迟 = 状态.latency
                服务器版本 = 状态.version.name
                协议版本 = 状态.version.protocol
                favicon = 状态.raw.get('favicon')
                # -----------------------------
                print("对象解析完成,开始解析为json")
                # 解析_解析所有对象数据为json更加方便
                解析json = {
                    "sever":f"{服务器}",
                    "m":"JE",
                    "player(=)":f"{玩家_在线}",# 玩家在线值
                    "player(+)":f"{玩家_最大}",# 玩家最大值
                    "motd":f"{motd_原始}",# 原始motd数据
                    "ping":f"{延迟}",# 延迟
                    "s_v":f"{服务器版本}",# 服务器版本
                    "p_v":f"{协议版本}",# 协议版本
                    "icon":f"{favicon}"# URL格式的icon(logo)
                }
                数据 = json.dumps(解析json, ensure_ascii=False)
                打印json = json.dumps(解析json, indent=2, ensure_ascii=False)
                print(f"解析为json成功:/n{打印json}")
                print("[OK]java方式查询成功")
                return 数据
            except Exception as e:
                pass
        except Exception as e:
            pass
    # _________________分割_________________
    def 通查(列表数据):
        class 结果容器:  # 临时类当容器
            pass
        
        def JE任务():
            结果容器.JE结果 = 服务器查询.JE(列表数据)  # 存结果
        
        def BE任务():
            结果容器.BE结果 = 服务器查询.BE(列表数据)  # 存结果
        
        JE线程 = threading.Thread(target=JE任务, daemon=True)
        BE线程 = threading.Thread(target=BE任务, daemon=True)
        
        JE线程.start()
        BE线程.start()
        
        for i in range(30):  # 检查30次,3秒
            time.sleep(0.1)
            if hasattr(结果容器, 'JE结果'):  # 检查JE
                return 结果容器.JE结果
            if hasattr(结果容器, 'BE结果'):  # 检查BE
                return 结果容器.BE结果
        return None

服务器数据列表 = []
def 查询进程(目标,端口):
    global 服务器数据列表,查询_在线端口数量,查询_符合过滤的端口数量
    查询列表数据 = [目标,端口]
    返回数据 = 服务器查询.通查(查询列表数据)
    if 返回数据 != None:
        try:
            返回数据 = json.loads(返回数据)
            
            解析_服务器地址 = 返回数据["sever"]
            解析_服务器类型 = 返回数据["m"]
            解析_玩家在线数 = 返回数据["player(=)"]
            解析_motd = 返回数据["motd"]
            解析_服务器版本 = 返回数据["s_v"]
            数据编译 = {
                "sever":解析_服务器地址,
                "m":解析_服务器类型,
                "v":解析_服务器版本,
                "player":解析_玩家在线数,
                "motd":解析_motd
            }
            # 数据编译_json = json.dumps(数据编译,ensure_ascii=False)
            数据编译_json = 数据编译
            
            # 过滤
            if 过滤方法 == 0: # 直接记录
                服务器数据列表.append(数据编译_json)
                查询_符合过滤的端口数量 += 1
            elif 过滤方法 == 1: # 有人的记录
                if int(数据编译["player"]) != 0:
                    服务器数据列表.append(数据编译_json)
                    查询_符合过滤的端口数量 += 1
            elif 过滤方法 == 2: # 包含版本的记录
                if 过滤方法_版本过滤 in 数据编译["v"]:
                    服务器数据列表.append(数据编译_json)
                    查询_符合过滤的端口数量 += 1
            elif 过滤方法 == 3: # 包含版本的并且有人的记录
                if 过滤方法_版本过滤 in 数据编译["v"]:
                    if int(数据编译["player"]) != 0:
                        服务器数据列表.append(数据编译_json)
                        查询_符合过滤的端口数量 += 1
                        
            print(f"查询到数据!{数据编译}")
            查询_在线端口数量 += 1
        except Exception as e:
            print(f"出现错误,如果这是偶尔的事情大可放心{e}")

def 停止函数():
    global 查询_继续查询
    input("")
    查询_继续查询 = False

# 主程序-----------------------------------------------------------------------------------------
print(logo)

# 开始获取用户参数
while True:
    过滤方法描述 = [
        "__选择您要用的过滤方法(填入数字)__",
        "0--全都不要,全部记录",
        "1--仅保存有至少1人的(过滤掉0人服,但此方法仅适合在白天扫描)",
        "2--版本过滤,写入您的版本比如'1.21.8'这样只会让1.21.8的版本被记录",
        "3--两者兼有"
    ]
    过滤方法描述 = '\n'.join(过滤方法描述)
    try:
        目标 = input("写入目标ip或域名:")
        端口_位数 = int(input("输入端口位数:"))
        端口_开始端口 = int(input("输入开始端口:"))
        端口_结束端口 = int(input("输入结束端口:"))
        延迟 = float(input("输入线程调度延迟(推荐0.2):")) # 就是一个线程启动后到下一个线程启动的延迟
        print(过滤方法描述)
        过滤方法 = int(input("请输入选择:"))
        if 过滤方法 == 2 or 过滤方法 == 3:
            过滤方法_版本过滤 = input("|--版本过滤_输入一个游戏版本:")
        break
    except Exception as e:
        表情 = r"¯\(ツ)/¯"
        print(f"奇怪捏{表情},您的输入似乎有错误,或许你看不懂但可以看一下错误或者报告给我哦:{e}")

# 展示用户参数
端口总数 = 端口_结束端口 - 端口_开始端口

参数 = [
    f"扫描目标:{目标}",
    f"端口位数:{端口_位数}",
    f"开始端口:{端口_开始端口}",
    f"结束端口:{端口_结束端口}",
    f"总共{端口总数}需要查询"
]
参数 = '--'.join(参数)
print(f"参数返回\n{参数}")

# 确定
print("开始扫描后你可以再次回车结束扫描直接保存")
input("回车开始扫描↩︎")
print("~~开始扫描~~")
time.sleep(0.2)

查询_继续查询 = True
# 停止函数,其实只是一个线程检测用户回车罢了
threading.Thread(target=停止函数, daemon=True).start()

查询_在线端口数量 = 0
查询_总共端口数量 = 0
查询_符合过滤的端口数量 = 0

开始时间 = time.time()
for i in range(端口总数):
    if 查询_继续查询:
        time.sleep(延迟)
        查询_总共端口数量 += 1
        循环_现在被查询端口 = 端口_开始端口 + i
        循环_现在被查询端口 = str(循环_现在被查询端口).zfill(端口_位数)
        print(f"现查询端口:{循环_现在被查询端口} | 共查询{查询_总共端口数量}个端口 | 在线端口{查询_在线端口数量}个 | 穿过过滤端口有{查询_符合过滤的端口数量}个")
        threading.Thread(target=查询进程, args=(目标, 循环_现在被查询端口), daemon=True).start()
    else:
        break
结束时间 = time.time()
扫描耗时 = 结束时间 - 开始时间
扫描耗时_分钟 = round(扫描耗时 / 60, 3) # 计算为分钟
扫描耗时_小时 = round(扫描耗时 / 60 / 60, 3) # 计算为小时

print("停止成功")
time.sleep(3)

print(服务器数据列表)

if 过滤方法 != 2 or 过滤方法 != 3:
    过滤方法描述 = f"使用了过滤方法{过滤方法}"
else:
    过滤方法描述 = f"使用了过滤方法{过滤方法},版本过滤参数:{过滤方法_版本过滤}"

文本 = [
    f"扫描目标:{目标}|端口位数:{端口_位数}|开始端口:{端口_开始端口}|结束端口:{端口_结束端口}|总共{端口总数}需要查询",
    f"{过滤方法描述}",
    f"扫描耗时:{扫描耗时_分钟}分钟({扫描耗时_小时}小时)",
    f"总共查询了{查询_总共端口数量}个端口,在线的端口有{查询_在线端口数量}个,符合要求的在线端口有{查询_符合过滤的端口数量}个ㄟ(≧^≦)ㄏ"
]
文本 = 文本 + 服务器数据列表
文本 = json.dumps(文本,indent=4,ensure_ascii=False)
print(文本)

try:
    时间戳 = datetime.now().strftime("%Y%m%d_%H%M%S")
    文件名 = f"服务器扫描结果_{时间戳}.txt"
    文件路径 = os.path.join(下载目录, 文件名)
    
    with open(文件路径, "w", encoding="utf-8") as f:
        f.write(文本)
    print(f"[OK]写入成功！路径:{文件路径}")
except Exception as e:
    print(f"[ERROR]写入失败! 错误:{e}")

print(f"总共查询了{查询_总共端口数量}个端口,在线的端口有{查询_在线端口数量}个,符合要求的在线端口有{查询_符合过滤的端口数量}个ㄟ(≧^≦)ㄏ")
print(f"扫描耗时:{扫描耗时_分钟}分钟({扫描耗时_小时}小时)")

# ____________________________________
while True:
    pass