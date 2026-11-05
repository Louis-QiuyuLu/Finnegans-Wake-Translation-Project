import json,pathlib
ROOT=pathlib.Path('/private/tmp/fw-release-20261105')
def load(c):return json.loads((ROOT/f'manuscript/chapters/{c}.json').read_text())
def save(c,d):(ROOT/f'manuscript/chapters/{c}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
d=load('II-2');s=d['segments'][0]
s['translation']=s['translation'].replace('当我们玩大号衣服扮大人，向痴笑少女展示他的智者如何同叔辈黑汉绕着阴森遮篷策马飞奔，我们总是举起他的爪子，用毛茸茸的缠人臂膀紧紧拥抱他。','当我们打扑克牌、穿大衣裳扮大人，你准会喜滋滋地发现，我穿贴身衣裙能多招人爱。').replace('凯利威克，朗费罗公寓，烈火之屋，骗徒之伙，伟大的老人，普通乳司，法偿货币，老者之友，坚实大地。','凯利威克，朗费罗公寓，议论院三号，蛋糕步道，逗趣大道，盐山，桃花心木郡，伊扎隆德，坚实大地。')
a=s['translation'].index('【第262页】');b=s['translation'].index('【第263页】')
s['translation']=s['translation'][:a]+'''【第262页】
【正文】——到底，这位十足正派汉子？慢着，别急！上前领我们穿行！
【右旁注】观念实在历史的或然可然绪论。
【正文】这桥在上。跨过去。就到城堡。敲门。¹ 请说口令，谢谢。是的，皮尔斯。哎呀，全都哑住了！哦，当真？²
【左旁注】拨班卓，矮脚鸡，弹球汉子炸飞咯。
【正文】谁，地上精怪，在第一记雷声中塌陷。³ 当她，他的飞蝶，落网受名。⁴
【左旁注】见她往壶里投一盎司茶，我眼珠差点掉下来。
【正文】厄德纳克鲁沙，安息女主，叫醒他们！让幸运的纯粹乱溅、露西，安安稳稳！⁵ 归入智愚历代修起的屋宇。母猪大吃。如是如是。⁶
【右旁注】造前预定之知。造后定命之不知。
【正文】套牢拴系的桩钉，登高踏脚的石块，如皮卡兹敦的布特。那脱脂奶白马仍在地阁顶层。凌驾一切。抑或这些倚在外墙上的翼架，是鲍斯木屋、香膏木板上的兽皮战利品？⁷ 葬礼高升、巴利豪颂！那就让巴克斯也喊：进来，进来！
【左旁注】摇尾梗犬幼崽抽奖券。
【正文】进来，进来！在此。唠叨客挥笔。痛饮客灌满窝。那公民酒馆掌柜，他拿锡换十。他取自——
【原注1】祈使式坏笑，那人鱼从紧潮线下的卧谎处答道：滚地狱去！
【原注2】噢，爱沃尔，照照镜子，瞧多兹如何安放何等睡汉。（此句以倒转词形作镜像；中文保留镜子与睡意，未复制全部倒拼。）
【原注3】锡壁桶里凿刻的好乌鸦。
【原注4】蜜蜂爱祭坛。月亮读图书。小鸡觅草场。
【原注5】饭后再射暗影。
【原注6】起疱的玛丽·头疼对封美的肚子·塔尔巴特说。
【原注7】贝格。去贝格。去贝格，务必记得贝格。再会贝格，虫儿贝格。

''' + s['translation'][b:]
# 译者损失说明须在项目译注，不能插成原注正文。
s['translation']=s['translation'].replace('（此句以倒转词形作镜像；中文保留镜子与睡意，未复制全部倒拼。）','')
s['notes'].append({'id':'ii2-262-mirror-loss','lemma':'O Evol, kool in the salg and ees how Dozi pits what a drows er.','kind':'translation','certainty':'proposal','text':'本句若干词倒拼或拆拼：Evol可倒读love，kool倒读look，ees倒读see。译文只保留镜子、观看与睡意，未复造全部镜像拼写。salg与末串仍待核，不据猜读添正文。','source_ids':['joyce-fp']})
s['status']='revised';s['reviewers']=[]
save('II-2',d)
