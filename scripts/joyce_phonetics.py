"""
GPT-SoVITS 的乔伊斯生造词近似发音与意群切分方案。
以下替换为本项目合成试验，不代表作者指定读音，也不声称出自未核学者原页。
"""
import re
from pathlib import Path

# 映射到 CMU ARPAbet 音标（注入 tools/gpt_sovits/GPT_SoVITS/text/engdict-hot.rep）
HOT_DICT_ENTRIES = {
    # 常用短词与易误拼词（长度<=3的生造词，防止被强制字母朗读）
    "GEN": "JH EH1 N",
    "IZ": "IH1 Z",
    "ALD": "AO1 L D",
    "SES": "S EH1 S",
    "MON": "M AA1 N",
    "DUD": "D AH1 D",
    "DIMB": "D IH1 M",
    "DAMB": "D AE1 M",
    "TETE": "T EH1 T",
    "ORRA": "AO1 R AH0",
    "WHYI": "W AY1",
    "DEED": "D IY1 D",
    "DIIE": "D AY1",
    "HOTH": "HH AA1 TH",
    "DUSKT": "D AH1 S K T",
    "ISEUT": "IY1 S UW1 L T",
    "PHALL": "F AO1 L",
    "PHARCE": "F AA1 R S",
    "NUNCE": "N AH1 N S",
    "PHOENISH": "F IY1 N IH0 SH",
    "ERSE": "ER1 S",
    "HUMSELF": "HH IH1 M S EH1 L F",
    "PRUMPTLY": "P R AA1 M P T L IY0",
    "UNQUIRING": "IH2 N K W AY1 R IH0 NG",
    "LIVVY": "L IH1 V IY0",
    "SHIZE": "SH AY1 Z",
    "SHEE": "SH IY1",
    "MACOOL": "M AH0 K UW1 L",
    "BREKKEK": "B R EH1 K EH0 K",
    "KEKKEK": "K EH1 K EH0 K",
    "KOAX": "K OW1 AE0 K S",
    "UALU": "W AA1 L UW0",
    "QUAOUAUH": "K W AA1 W AA1",
    "PFTJSCHUTE": "SH UW1 T",
    "MISHE": "M IH1 SH AH0",
    "TAUFTAUF": "T AO1 F T AO1 F",
    "THUARTPEATRICK": "DH AW1 AA1 R T P EY1 T R IH0 K",
    "KIDSCAD": "K IH1 D S K AE2 D",
    "BUTTENDED": "B AH1 T EH1 N D IH0 D",
    "SOSIE": "S OW1 Z IY0",
    "SESTHERS": "S IH1 S T ER0 Z",
    "TWONE": "T UW1 W AH1 N",
    "NATHANDJOE": "N EY1 TH AH0 N JH OW1",
    "ARCLIGHT": "AA1 R K L AY2 T",
    "RORY": "R AO1 R IY0",
    "REGGINBROW": "R EH1 G IH0 N B R AW1",
    "RINGSOME": "R IH1 NG S AH0 M",
    "AQUAFACE": "AA1 K W AH0 F EY1 S",
    "FINFOEFOM": "F IY1 F OW1 F AH1 M",
    "FUSH": "F AH1 SH",
    "DOBBELIN": "D AA1 B L IH0 N",
    "AYLE": "EY1 L",
    "FADOGRAPH": "F EY1 D OW0 G R AE2 F",
    "FINICHE": "F IH1 N IY0 SH",
    "DESH": "D EH1 SH",
    "WHASE": "HH UW1 Z",
    "SCUTSCHUM": "S K AH1 CH AH0 N",
    "TUMPTY": "T AH1 M P T IY0",
}

# 文本预处理音标转写词典（针对乔伊斯复合词、法语/德语/爱尔兰语双关词）
JOYCE_TRANSCRIPTIONS = [
    # I.1 段落 1
    (r"\briverrun\b", "river-run"),
    (r"\bcommodius\b", "commodious"),
    (r"\bvicus\b", "vee-cus"),

    # I.1 段落 2
    (r"\bvioler d'amores\b", "violer dah-mor"),
    (r"\bfr'over\b", "from over"),
    (r"\bpassencore\b", "pass-on-core"),
    (r"\brearrived\b", "re-arrived"),
    (r"\bNorth Armorica\b", "North Armor-i-ca"),
    (r"\bwielderfight\b", "wielder-fight"),
    (r"\bpenisolate\b", "pen-isolate"),
    (r"\btopsawyer's\b", "top-sawyer's"),
    (r"\bthemselse\b", "themselves"),
    (r"\bgorgios\b", "gor-joss"),
    (r"\bdoublin\b", "Dublin"),
    (r"\bavoice\b", "a voice"),
    (r"\bafire\b", "a-fire"),
    (r"\bbellowsed\b", "bellowed"),
    (r"\bmishe mishe\b", "mish-uh mish-uh"),
    (r"\btauftauf\b", "toff-toff"),
    (r"\bthuartpeatrick\b", "thou-art-Patrick"),
    (r"\bvenissoon\b", "venison"),
    (r"\bkidscad\b", "kids-cad"),
    (r"\bbuttended\b", "butt-ended"),
    (r"\bvanessy\b", "van-ess-ee"),
    (r"\bsosie sesthers\b", "so-zee sisters"),
    (r"\btwone\b", "two-one"),
    (r"\bnathandjoe\b", "Nathan-Joe"),
    (r"\bpa's\b", "pah's"),
    (r"\bJhem or Shen\b", "Jem or Shem"),
    (r"\barclight\b", "arc-light"),
    (r"\brory\b", "roar-ee"),
    (r"\bregginbrow\b", "reggin-brow"),
    (r"\bringsome\b", "ring-some"),
    (r"\baquaface\b", "aqua-face"),

    # I.1 段落 3 (雷言与倒坍)
    (r"bababadalgharaghtakamminarronnkonnbronntonner-ronntuonnthunntrovarrhounawnskawntoohoohoordenenthur-nuk",
     "ba-ba-bad-al-ga-ragh-ta-kam-min-ar-ron-kon-bron-ton-ner, ron-tu-on-thun-tro-var-houn-awn-skawn-too-hoo-hoo-den-en-thur-nook"),
    (r"\bwallstrait\b", "wall-strait"),
    (r"\boldparr\b", "old-parr"),
    (r"\bretaled\b", "re-told"),
    (r"\boffwall\b", "off-wall"),
    (r"\bpftjschute\b", "shoot"),
    (r"\berse\b", "Erse"),
    (r"\bhumptyhillhead\b", "Humpty-hill-head"),
    (r"\bhumself\b", "himself"),
    (r"\bprumptly\b", "promptly"),
    (r"\bunquiring\b", "inquiring"),
    (r"\btumptytumtoes\b", "tumpty tum toes"),
    (r"\bupturnpikepointandplace\b", "up-turnpike-point-and-place"),
    (r"\bdevlinsfirst\b", "devils-first"),
    (r"\blivvy\b", "Livvy"),

    # I.1 段落 4 (蛙鸣与战阵)
    (r"\bgen\b", "jen"),
    (r"\boystrygods\b", "oyster-gods"),
    (r"\bgaggin\b", "gagging"),
    (r"\bfishygods\b", "fishy-gods"),
    (r"\bBrékkek\b", "Breck-ek"),
    (r"\bKékkek\b", "Keck-ek"),
    (r"\bKóax\b", "Co-ax"),
    (r"\bUalu\b", "Wah-loo"),
    (r"\bQuaouauh\b", "Kwah-wah"),
    (r"\bBaddelaries\b", "Bad-el-aries"),
    (r"\bmathmaster\b", "math-master"),
    (r"\bMicgranes\b", "Mick-granes"),
    (r"\bVerdons\b", "Ver-dons"),
    (r"\bcatapelting\b", "catapulting"),
    (r"\bcamibalistics\b", "cannibalistics"),
    (r"\bWhoyteboyce\b", "White-boys"),
    (r"\bAssiegates\b", "Assie-gates"),
    (r"\bboomeringstroms\b", "boomerang-stroms"),
    (r"\bSanglorians\b", "San-glorians"),
    (r"\bapeal\b", "appeal"),
    (r"\blarms\b", "alarms"),
    (r"\bKillykillkilly\b", "Killy-kill-killy"),
    (r"\bcuddleys\b", "cuddles"),
    (r"\bcashels\b", "cash-els"),
    (r"\bbidimetoloves\b", "biddy-me-to-loves"),
    (r"\bsinduced\b", "sin-duced"),
    (r"\btegotetabsolvers\b", "te-got-et-absolvers"),
    (r"\bhayair\b", "hay-air"),
    (r"\bstrawng\b", "strong"),
    (r"\bjiccup\b", "hiccup"),
    (r"\bhoth\b", "Hoth"),
    (r"\bsprowled\b", "sprawled"),
    (r"\bduskt\b", "dusked"),
    (r"\bfanespanned\b", "fane-spanned"),
    (r"\bskysign\b", "sky-sign"),
    (r"\biz\b", "is"),
    (r"\bIseut\b", "Ee-soolt"),
    (r"\bald\b", "auld"),
    (r"\baskes\b", "ashes"),
    (r"\bPhall\b", "Fall"),
    (r"\bpharce\b", "farce"),
    (r"\bnunce\b", "nonce"),
    (r"\bsetdown\b", "set-down"),
    (r"\bphoenish\b", "phoenix"),

    # I.1 段落 5 (营造师芬尼根)
    (r"\bBygmester\b", "Byg-mester"),
    (r"\bmaurer\b", "mow-rer"),
    (r"\bimmarginable\b", "im-margin-able"),
    (r"\brushlit\b", "rush-lit"),
    (r"\btoofarback\b", "too-far-back"),
    (r"\bjoshuan\b", "Josh-u-an"),
    (r"\bHelviticus\b", "Hel-vit-i-cus"),
    (r"\byeastyday\b", "yeasty-day"),
    (r"\bsternely\b", "sternly"),
    (r"\bstruxk\b", "struck"),
    (r"\btete\b", "tait"),
    (r"\bwatsch\b", "watch"),
    (r"\bstook\b", "stuck"),
    (r"\beviparated\b", "evaporated"),
    (r"\bguenneses\b", "Guinness-es"),
    (r"\bpentschanjeuchy\b", "pen-shan-jook-ee"),
    (r"\bbuildung\b", "building"),
    (r"\bSoangso\b", "Song-so"),
    (r"\baddle liddle phifie\b", "addle little wifie"),
    (r"\bugged\b", "hugged"),
    (r"\bcraythur\b", "creature"),
    (r"\bhayre\b", "hair"),
    (r"\bhonds\b", "hands"),
    (r"\binher\b", "in her"),
    (r"\bOftwhile\b", "Oft-while"),
    (r"\bbalbulous\b", "bal-bu-lous"),
    (r"\bmithre\b", "mitre"),
    (r"\bivoroiled\b", "ivory-oiled"),
    (r"\bhabitacularly\b", "habitu-acularly"),
    (r"\bfondseed\b", "fond-seed"),
    (r"\bChilderic Eggeberth\b", "Childeric Egbert"),
    (r"\bcaligulate\b", "cal-ig-u-late"),
    (r"\balltitude\b", "altitude"),
    (r"\bmalltitude\b", "multitude"),
    (r"\bneatlight\b", "neat-light"),
    (r"\bwheretwin\b", "where-twin"),
    (r"\bmaisonry\b", "masonry"),
    (r"\bupstanded\b", "up-standed"),
    (r"\bjoygrantit\b", "joy-granted"),
    (r"\bwaalworth\b", "Wool-worth"),
    (r"\bskyerscape\b", "sky-scraper"),
    (r"\bhoyth\b", "Howth"),
    (r"\bentowerly\b", "entirely"),
    (r"\berigenating\b", "originating"),
    (r"\bcelescalating\b", "celestial-escalating"),
    (r"\bhimals\b", "Him-als"),
    (r"\bhierarchitectitiptitoploftical\b", "hier-archi-tecti-tipti-top-loftical"),
    (r"\babob\b", "a-bob"),
    (r"\bbaubletop\b", "bauble-top"),
    (r"\blarrons o'toolers\b", "lar-rons O'Toolers"),
    (r"\btombles\b", "tumbles"),
    (r"\ba'buckets\b", "a-buckets"),
    (r"\bclottering\b", "clattering"),

    # I.1 段落 6
    (r"\bWassaily Booslaeugh\b", "Vas-sil-y Boos-lock"),
    (r"\bRiesengeborg\b", "Ree-zen-ge-borg"),
    (r"\bhuroldry\b", "heraldry"),
    (r"\bancillars\b", "an-cil-lars"),
    (r"\btroublant\b", "troo-blant"),
    (r"\bhegoak\b", "he-goat"),
    (r"\bpoursuivant\b", "poor-swee-vant"),
    (r"\bscutschum\b", "escutcheon"),

    # I.1 段落 7
    (r"\bHootch\b", "Hooch"),
    (r"\bHohohoho\b", "Ho ho ho ho"),
    (r"\bFinnagain\b", "Finn-again"),
    (r"\bComeday\b", "Come-day"),
    (r"\bmorm\b", "morn"),
    (r"\bSendday's\b", "Sunday's"),
    (r"\bHahahaha\b", "Ha ha ha ha"),
    (r"\bFunn\b", "Fun"),

    # I.1 段落 8
    (r"\btragoady\b", "tragedy"),
    (r"\bthundersday\b", "Thunders-day"),
    (r"\bcubehouse\b", "cube-house"),
    (r"\barafatas\b", "Ar-a-fat-as"),
    (r"\bshebby\b", "shabby"),
    (r"\bchoruysh\b", "chorus"),
    (r"\bunkalified\b", "unqualified"),
    (r"\bmuzzlenimiissilehims\b", "muzzle-missile-hims"),
    (r"\bblackguardise\b", "blackguard-ize"),
    (r"\bwhitestone\b", "white-stone"),
    (r"\bhurtleturtled\b", "hurtle-turtled"),
    (r"\btighteousness\b", "righteousness"),
    (r"\btoothmick\b", "tooth-pick"),
    (r"\bupown\b", "upon"),
    (r"\bleatherbed\b", "leather-bed"),
    (r"\bnabir\b", "neigh-bor"),
    (r"\bwabsanti\b", "wab-san-ti"),
    (r"\bOtherways\b", "Other-ways"),
    (r"\bwesways\b", "west-ways"),
    (r"\bbedoueen\b", "Bedouin"),
    (r"\bjebel\b", "jeh-bel"),
    (r"\bjpysian\b", "joy-sian"),
    (r"\bCropherb\b", "Crop-herb"),
    (r"\bcrunchbracken\b", "crunch-bracken"),
    (r"\bflyday\b", "Friday"),
    (r"\ballcasually\b", "all-casually"),
    (r"\bansars\b", "answers"),
    (r"\bdreamydeary\b", "dreamy-deary"),

    # I.1 段落 9
    (r"\bhalf been\b", "have been"),
    (r"\bmissfired\b", "mis-fired"),
    (r"\bmought\b", "might"),
    (r"\bcollupsus\b", "collapse"),
    (r"\bextand\b", "extend"),
    (r"\babe ite\b", "Adam ate"),
    (r"\bivvy's\b", "Eve's"),
    (r"\bholired abbles\b", "holy-red apples"),
    (r"\bwallhall's\b", "Val-halla's"),
    (r"\brollsrights\b", "Rolls-Royces"),
    (r"\bcarhacks\b", "car-hacks"),
    (r"\bstonengens\b", "Stone-henges"),
    (r"\bkisstvanes\b", "kist-vaens"),
    (r"\btramtrees\b", "tram-trees"),
    (r"\bfargobawlers\b", "far-go-bawlers"),
    (r"\bautokinotons\b", "auto-kino-tons"),
    (r"\bhippohobbilies\b", "hippo-hobbies"),
    (r"\bstreetfleets\b", "street-fleets"),
    (r"\btournintaxes\b", "turning-taxis"),
    (r"\bmegaphoggs\b", "mega-fogs"),
    (r"\bwardsmoats\b", "wards-moats"),
    (r"\bbasilikerks\b", "basili-kerks"),
    (r"\baeropagods\b", "aero-pagodas"),
    (r"\bhoyse\b", "house"),
    (r"\bjollybrool\b", "jolly-brawl"),
    (r"\bmecklenburk\b", "Mecklen-burg"),
    (r"\bmerlinburrow burrocks\b", "Merlin-burrow bur-rocks"),
    (r"\bporecourts\b", "four-courts"),
    (r"\bblightblack\b", "blight-black"),
    (r"\btwelvepins\b", "twelve-pins"),
    (r"\bnoobibusses\b", "omni-busses"),
    (r"\bsleighding\b", "sliding"),
    (r"\bderryjellybies\b", "derry-jelly-bies"),
    (r"\bstrupithump\b", "strupi-thump"),
    (r"\bromekeepers\b", "rome-keepers"),
    (r"\bhomesweepers\b", "home-sweepers"),
    (r"\bdomecreepers\b", "dome-creepers"),
    (r"\bthurum and thurum\b", "thrum and thrum"),
    (r"\bfancymud murumd\b", "fancy-mud mud"),
    (r"\buproor\b", "uproar"),
    (r"\baufroofs\b", "off-roofs"),
    (r"\bfilt\b", "felt"),
    (r"\bhowd\b", "head"),
    (r"\bhoddit\b", "hod-it"),
    (r"\bDimb\b", "Dim"),
    (r"\bstottered\b", "tottered"),
    (r"\blatter\b", "ladder"),
    (r"\bDamb\b", "Damn"),
    (r"\bdud\b", "dead"),
    (r"\bDumb\b", "Dumb"),
    (r"\bMastabatoom, mastabadtomm\b", "Mas-ta-ba-tomb, mas-ta-bad-tomb"),
    (r"\bmon merries\b", "man marries"),

    # I.1 段落 10
    (r"\bShize\b", "Shize"),
    (r"\bshee\b", "see"),
    (r"\bMacool\b", "Mac-Cool"),
    (r"\borra whyi deed ye diie\b", "or-ra why did you die"),
    (r"\bthirstay mournin\b", "Thursday morning"),
    (r"\bsighdid\b", "sigh-did"),
    (r"\bFillagain's\b", "Finnegan's"),
    (r"\bchrissormiss\b", "Christmas"),
    (r"\bhoolivans\b", "Hooligans"),
    (r"\bduodisimally\b", "duo-decimally"),
    (r"\bgianed\b", "joined"),
    (r"\bshout-most shoviality\b", "ut-most jo-vi-al-ity"),
    (r"\bAgog and magog\b", "Gog and Magog"),
    (r"\bagrog\b", "a-grog"),
    (r"\bHanandhunigan's\b", "Han-and-Hun-i-gan's"),
    (r"\bkinkin corass\b", "kin-kin chorus"),
    (r"\bkankan keening\b", "can-can keening"),
    (r"\bPriam Olim\b", "Pree-am Oh-lim"),
    (r"\bdacent gaylabouring\b", "decent gay-laboring"),
    (r"\bpillowscone\b", "pillow-scone"),
    (r"\bE'erawhere\b", "Everywhere"),
    (r"\bwhorl\b", "world"),
    (r"\bsich a din\b", "such a din"),
    (r"\bdeepbrow fundigs\b", "deep-brow fun-digs"),
    (r"\bfidelios\b", "fi-del-i-os"),
    (r"\bbrawdawn\b", "broad-down"),
    (r"\balanglast\b", "a-long-last"),
    (r"\bbockalips\b", "boc-ka-lips"),
    (r"\bfinisky\b", "whiskey"),
    (r"\bguenesis\b", "Guinness-es"),
    (r"\bhoer\b", "over"),
    (r"\btootal\b", "total"),
    (r"\btwoddle\b", "twaddle"),
    (r"\btautaulogically\b", "tautologically"),

    # I.1 段落 11
    (r"\bbabeling\b", "babe-ling"),
    (r"\bpeegee\b", "P. G."),
    (r"\bShopalist\b", "Chapelizod"),
    (r"\bBailywick\b", "Baily-wick"),
    (r"\bashtun\b", "Ashtown"),
    (r"\bbaronoath\b", "baron-oath"),
    (r"\bBuythebanks\b", "Buy-the-banks"),
    (r"\bRoundthehead\b", "Round-the-head"),
    (r"\bireglint's\b", "Ire-glint's"),
    (r"\bextensolies\b", "extensively lies"),
    (r"\bfjord to fjell\b", "fjord to fell"),
    (r"\boboboes\b", "oboes"),
    (r"\bswimswamswum\b", "swim-swam-swum"),
    (r"\blivvylong\b", "livelong"),
    (r"\bdelldale dalppling\b", "dell-dale dappling"),
    (r"\bbluerybells\b", "blue-bells"),
    (r"\bflittaflute\b", "flitter-flute"),
    (r"\btrochees\b", "tro-chees"),
    (r"\bcarina\b", "ca-ree-na"),
    (r"\bissavan essavans\b", "is-a-van es-a-vans"),
    (r"\bpatterjackmartins\b", "patter-jack-martins"),
    (r"\bteel of a tum\b", "tale of a tub"),
    (r"\bturty Taubling\b", "thirty Dublin"),
    (r"\bgifs à gross\b", "gives a gross"),
    (r"\bcrawsake\b", "Christ's sake"),
    (r"\bGrampupus\b", "Grandpa-pus"),
    (r"\bsprids the boord\b", "spreads the board"),
    (r"\bWhase\b", "Whose"),
    (r"\bwhase\b", "whose"),
    (r"\bdesh\b", "dish"),
    (r"\bFinfoefom the Fush\b", "Fee-fo-fum the Fish"),
    (r"\bbaken\b", "baked"),
    (r"\bSingpantry's\b", "Saint Patrick's"),
    (r"\btayle\b", "tail"),
    (r"\bDobbelin ayle\b", "Dublin ale"),
    (r"\bquaffoff\b", "quaff-off"),
    (r"\bfraudstuff\b", "fraud-stuff"),
    (r"\bpyth\b", "pith"),
    (r"\bflowerwhite bodey\b", "flower-white body"),
    (r"\bnoewhemoe\b", "no-where-more"),
    (r"\bFiniche\b", "Fin-eesh"),
    (r"\bfadograph\b", "fade-o-graph"),
    (r"\byestern\b", "yester"),
]


def update_engdict_hot(gpt_sovits_dir):
    """
    将乔伊斯短生造词注入 GPT-SoVITS 的 engdict-hot.rep，确保即使漏掉替换也不会拼读字母。
    """
    hot_rep_path = Path(gpt_sovits_dir) / "GPT_SoVITS/text/engdict-hot.rep"
    if not hot_rep_path.parent.exists():
        return

    existing = {}
    if hot_rep_path.exists():
        for line in hot_rep_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line:
                parts = line.split(" ")
                existing[parts[0].upper()] = " ".join(parts[1:])

    updated = False
    for word, prons in HOT_DICT_ENTRIES.items():
        if word.upper() not in existing:
            existing[word.upper()] = prons
            updated = True

    if updated:
        lines = [f"{w} {p}" for w, p in sorted(existing.items())]
        hot_rep_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        # 清除字典缓存 pickle
        cache_path = Path(gpt_sovits_dir) / "GPT_SoVITS/text/engdict_cache.pickle"
        if cache_path.exists():
            cache_path.unlink()
        print(f"已更新 engdict-hot.rep，共注入 {len(existing)} 条发音规则。")


def normalize_joyce_text(text: str) -> str:
    """
    将原文中的生造词根据研究转写为最接近发音的标准英音组合。
    保留原句骨架，消除导致 G2P 逐字母拼读的生僻组合。
    """
    result = text
    for pattern, repl in JOYCE_TRANSCRIPTIONS:
        result = re.sub(pattern, repl, result, flags=re.IGNORECASE)
    return result


def segment_into_sense_groups(text: str):
    """
    切分意群：依据文学诵读节奏将段落切分为呼吸意群单位，并返回 (意群文本, 停顿秒数)。
    完全对齐《西西弗神话》沉稳连贯的叙事节奏：完整子句一口气诵读，不作机械逗号切碎。
    覆盖换行、跨行连字符、段首及纯标点停顿，确保无标点换行不漏读正文。
    """
    text = normalize_joyce_text(text).strip()
    text = re.sub(r"(\b\w+)-\s*\n\s*(\w+\b)", r"\1\2", text)

    # 按照主要标点（句号、感叹号、问号、分号、冒号、长破折号）或换行切分出完整语法意群子句
    pattern = r"(?:[^.!?;:—\n]+(?:[.!?—;:]+[)'\"”’]*|\n+|\Z)|[.!?—;:…]+)"
    raw_clauses = re.findall(pattern, text)
    if not raw_clauses:
        raw_clauses = [text]

    groups = []
    for clause in raw_clauses:
        clause_str = clause.strip()
        if not clause_str:
            continue
        words = clause_str.split()
        last_char = clause_str[-1] if clause_str else ""

        # 若子句超长（超过 30 词）且中间包含逗号，于平衡逗号处自然换气分节
        if len(words) > 30 and ", " in clause_str:
            parts = re.split(r"(, )", clause_str)
            sub_accum = ""
            for p in parts:
                sub_accum += p
                if p == ", " and len(sub_accum.split()) >= 12:
                    groups.append((sub_accum.strip(), 0.20))
                    sub_accum = ""
            if sub_accum.strip():
                pause = 0.42 if last_char in (".", "!", "?") else 0.26
                groups.append((sub_accum.strip(), pause))
        else:
            # 句末给 0.42s 深呼吸；分号/冒号/破折号/行末给 0.26s 中级停顿
            pause = 0.42 if last_char in (".", "!", "?") else 0.26
            groups.append((clause_str, pause))

    return groups
