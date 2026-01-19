# 第一行不是import是而是我的请求,对于你们这些老手这简直是屎山,但我没有正式学过python和编程,希望不要说任何东西打击我QWQ,你只要知道他可以用这就足够了,谢谢体谅,祝您生活愉快
from mcstatus import JavaServer as java服务器, BedrockServer as 基岩服务器
import json
import threading
import time
import os
from datetime import datetime
import gc

logo = r'''
 __   __  __      ____                   
/\ \ /\ \/\ \    /\  _`\                 
\ `\`\/'/\ \ \___\ \,\L\_\    ___ ___    
 `\/ > <  \ \  _ `\/_\__ \  /' __` __`\  
    \/'/\`\\ \ \ \ \/\ \L\ \/\ \/\ \/\ \ 
    /\_\\ \_\ \_\ \_\ `\____\ \_\ \_\ \_\
    \/_/ \/_/\/_/\/_/\/_____/\/_/\/_/\/_/
     ----XhSm端口扫描工具为您服务~(´〜｀*)~zzz----
----------------------------------------------------
该项目的开源链接:
https://github.com/vovahub/XhSm-MC-Server-Port-Scanning-Tool
我的github:
https://github.com/vovahub
----------------------------------------------------
作者:Vovalu
作者b站:https://space.bilibili.com/3546654082861538
作者的qq群:971463342
如果该工具对您有用可以关注我bilibili嘛求求啦!QWQ
----------------------------------------------------
免责声明:
该工具不是任何黑客工具,这只是一个普通服务器端口扫描工具,您只能用它来扫描服务器游玩
您通过扫描完后的服务器寻找可玩服务器的时候要看MOTD选择公用的人多的公开服服,毕竟私人服务器也可能会被扫描到
即使您不小心进入了私人服务器也请您在询问过后离开
<我们不主张任何形式的入侵他人私人服awa即使你可能一进去就被ban,还可能被骂一顿>
----------------------------------------------------
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

# 日志 = []
# def addlog(str):
#     global 日志
#     now = datetime.now()
#     formatted_time = now.strftime("%H:%M:%S")
#     日志.append(f"{formatted_time}--{str}")
    
class 服务器查询():
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
            解析_玩家在线数 = int(返回数据["player(=)"])
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
            if 过滤方法 == "": # 直接记录
                服务器数据列表.append(数据编译_json)
                查询_符合过滤的端口数量 += 1
            else:
                if 1 in 过滤方法 and 数据编译_json != None: # 有人的记录
                    if not int(数据编译["player"]) != 0:
                        数据编译_json = None
                        
                if 2 in 过滤方法 and 数据编译_json != None: # 包含版本的记录
                    if not 过滤方法_版本过滤 in 数据编译["v"]:
                        数据编译_json = None
                        
                if 3 in 过滤方法 and 数据编译_json != None: # 包含MOTD的记录
                    if not 过滤方法_MOTD过滤 in 数据编译["motd"]:
                        数据编译_json = None
                
                # 最后验证并记录
                if 数据编译_json != None:
                    查询_符合过滤的端口数量 += 1
                    服务器数据列表.append(数据编译_json)
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
扫描方法 = [
    "__选择您要用的扫描方法__",
    "■>1--通过一个域名或ip扫描所有端口",
    "└───|适合扫描我的世界服务器服务商",
    "■>2--选择开始ip和结束ip,用进步式全段扫描我的世界服务器(危险)",
    "└───|适合大规模的全网寻找我的世界服务器,但这很危险极不推荐,您甚至可能收到运营商警告和流量限流",
]
print('\n'.join(扫描方法))
扫描方法 = int(input("选择您要用的扫描方法:"))
print(f"您选择了扫描方法->{扫描方法}")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if 扫描方法 == 1:
    过滤参数 = {}
    # 开始获取用户参数
    while True:
        过滤方法描述 = [
            "__选择您要用的过滤方法__",
            "■>1--过滤掉0人服",
            "└───|一般适合在白天或者希望扫描到至少有一人的服务器",
            "■>2--版本过滤--写入您的版本比如'1.21.8'这样只会让版本包含'1.21.8'的版本被记录",
            "└───|",
            "■>3--MOTD过滤--写入MOTD比如'A Minecraft Server'这样只有服务器MOTD包含'A Minecraft Server'会被记录",
            "└───|",
            "~~~___________________________________________~~分割~~_______________________________________________~~~",
            "填写您要写用的,如果您要不使用过滤直接记录直接回车即可,",
            "否则要选择要用的过滤方法,比如你要用'1'要写1,要用多个的要写'1,2'这样的",
            "其实就是选择过滤方法,用','分割"
        ]
        过滤方法描述 = '\n'.join(过滤方法描述)
        try:
            目标 = input("写入目标ip或域名:")
            端口_位数 = int(input("输入端口位数:"))
            端口_开始端口 = int(input("输入开始端口:"))
            端口_结束端口 = int(input("输入结束端口:"))
            延迟 = float(input("输入线程调度延迟(推荐0.2):")) # 就是一个线程启动后到下一个线程启动的延迟
            print(过滤方法描述)
            过滤方法 = input("输入要使用的过滤方法:")
            if 过滤方法 != "":
                过滤方法 = list(map(int, 过滤方法.split(",")))
                if 2 in 过滤方法: # 额外输入_版本过滤参数
                    过滤方法_版本过滤 = input("|--版本过滤_输入一个游戏版本:")
                    过滤参数["V"] = 过滤方法_版本过滤
                if 3 in 过滤方法: # 额外输入_MOTD过滤参数
                    过滤方法_MOTD过滤 = input("|--MOTD过滤_输入一个MOTD:")
                    过滤参数["MOTD"] = 过滤方法_MOTD过滤
            break
        except Exception as e:
            表情 = r"¯\(ツ)/¯"
            print(f"奇怪捏{表情},您的输入似乎有错误,或许你看不懂但可以看一下错误或者报告给我哦awa:{e}")
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
    # --------------------------------------------------------------------------
    print(服务器数据列表)
    # 把服务器玩家数量排序一下
    try: # 防止奇怪的错误,当然这只是让我安心罢了
        服务器数据列表_排序过的 = sorted(服务器数据列表, key=lambda x: x["player"], reverse=True)
        服务器数据列表 = 服务器数据列表_排序过的
    except Exception as e:
        服务器数据列表 = 服务器数据列表 # 感觉有点多余Omo,算了按我想的做
    
    # 计算一下百分比
    百分比_总比在线 = "ERROR"
    百分比_总比符合过滤 = "ERROR"
    try:
        百分比_总比在线 = round(int(查询_在线端口数量) / int(查询_总共端口数量) * 100, 2)
        百分比_总比符合过滤 = round(int(查询_符合过滤的端口数量) / int(查询_总共端口数量) * 100, 2)
    except Exception as e:
        pass
    过滤方法描述 = f"使用了过滤方法{过滤方法},过滤参数:{过滤参数}"
    文本 = [
        f"扫描目标:{目标}|端口位数:{端口_位数}|开始端口:{端口_开始端口}|结束端口:{端口_结束端口}|总共{端口总数}需要查询",
        f"{过滤方法描述}",
        f"扫描耗时:{扫描耗时_分钟}分钟({扫描耗时_小时}小时)",
        f"总共查询了{查询_总共端口数量}个端口,在线的端口有{查询_在线端口数量}个,符合要求的在线端口有{查询_符合过滤的端口数量}个ㄟ(≧^≦)ㄏ",
        f"在线端口占总共端口:{百分比_总比在线}%,符合要求的端口占总共端口:{百分比_总比符合过滤}%"
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
    print(f"在线端口占总共端口:{百分比_总比在线}%,符合要求的端口占总共端口:{百分比_总比符合过滤}%")

# ____________________________________
gc.collect() # 清理一下内存
while True: # 阻止程序退出,让用户可以看到最后的输出结果
    pass