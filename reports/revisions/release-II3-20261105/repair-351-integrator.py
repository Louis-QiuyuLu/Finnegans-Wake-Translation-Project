import pathlib,json
R=pathlib.Path('/private/tmp/fw-release-20261105');p=R/'manuscript/chapters/II-3.json';d=json.loads(p.read_text());actions=[]
def e(i,a,b,issue):
 s=d['segments'][i];assert a in s['translation'],a;s['translation']=s['translation'].replace(a,b,1);s['status']='revised';s['reviewers']=[];actions.append({'issue':issue,'segment_id':s['id'],'old':a,'new':b})
s=d['segments'][5];i=s['translation'].index('然，我认罪，我见全俄罗斯');s['translation']=s['translation'][:i]+'可是，我的罪，埃尔泽鲁姆的阿拉姆，正如我爱我们的鹿迪鲁希，我承认，毫无偏见：看着那全俄罗斯的沙尔，腹中劳作把大号的重量压在身上，认出老板的命数，我怕的是努阿达众子对他下手；他对我实在沉重——'
e(7,'伴随颂歌与勃朗宁手枪赐予吾等之胜利','——给我们胜利，伴着诺埃尔颂歌与勃朗宁','N-II3-345-351-seam')
e(7,'我乃赤膊列兵，未带狗腿军衔条/无拐腿','我是赤膊列兵，没带我的狗腿','R-II3-18')
e(7,'彼等向彼示爱而彼夺走吾人阵线；','她们给他爱，他从我们手里夺走话（他那他与她的飞飞调情，真可恶！简直人鱼疯逗！）；','N-II3-351-parenthesis')
e(7,'上校，四星俄国巨汉，多姆·阿拉夫·奥霍尔万！','船长（回瞄他的赤身！），肚满救护尊驾，受挫的四星俄斯卡克鲁斯卡姆，多姆·阿拉夫·奥霍尔万，谜鼓喷气。','N-II3-351-title-stage')
e(7,'类似景象在火奴鲁鲁、布拉瓦约与雅典同步上演','类似场景也从胡卢卢卢、巴拉瓦约、天上的拉乌姆与摩登阿特姆斯投射而来','N-II3-351-four-sites')
e(7,'若彼心爱颅骨而我吞食烦忧','若他爱他脑袋的性，我吃他裤子的渗睡','N-II3-351-troublers')
e(7,'彼将以丝绸与蜂蜜诱买少年','他将用咒魅丝絮、芝麻丝蜜买男孩、骗姑娘','N-II3-351-boys-girls')
e(7,'掌柜提威利先生，守候在库默-费特，其配偶乃安娜·利菲','提威利·斯皮利特肖普斯先生，守候在库默—费特，其配偶名安—利夫','N-II3-351-name-not-identity')
e(7,'提供初始动力，来自四方之首度蠕动','提供第一贵动与否，从无处不在而来的初次蠕动','N-II3-351-ubivence')
e(7,'然而我已读尽其文，如同我至亲好友','然而我已读够了，如同我至亲好友','N-II3-351-enough-not-all')
e(7,'在这位早期木刻家、微型画大师之文字技艺面前。','在这早期木刻家、微景雕刻大师的造词术之前——','N-II3-351-357-seam')
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');(R/'reports/revisions/release-II3-20261105/351-integrator-actions.json').write_text(json.dumps(actions,ensure_ascii=False,indent=2)+'\n');print('Saved',len(actions),'corrections and removed duplicated tail clause.')
