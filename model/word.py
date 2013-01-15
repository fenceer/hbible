# coding:utf-8
'''
Created on 2012-12-27

@author: fenceer
'''

import re
import web

db = web.config.db

def checkChapter(ss):
    pattern = ur'^(\D{1,20})\s{0,3}(\d{1,3})\D{0,3}(\d{0,3}\s{0,3}-{0,1}\s{0,3}\d{0,3})$'
    # match = re.search(r'\d', ss)
    match = re.match(pattern, ss)
    if match:
        sn = match.group(1).strip()
        chp = int(match.group(2))
        start = 0
        end = 900
        if match.group(3):
            jie = match.group(3).split('-') 
            start = int(jie[0]) if jie[0] else 0
            end = int(jie[1]) if len(jie) == 2 and jie[1] else start
        if start > end:
            tmp = start
            start = end
            end = tmp
        start = chp * 1000 + start
        end = chp * 1000 + end
        
        book = getBook(sn)
        if book:
            text = book[1] + '\n'
            verses = db.GB.find({'book':book[0], '$and':[
                                           {'index':{'$gte':start}},
                                           {'index':{'$lte':end}}]})
            verses_list = list(verses)
            if len(verses_list) > 0:
                for v in verses_list:
                    text += v['text']
            else:
                text += '请输入正确的查询范围/可怜\n\n回复H查看使用帮助'
        else:
            text = '没有找到您要的经文/委屈\n微圣经将不断提高查询能力\n\n回复H查看使用帮助'
        return text
    else:
        return None

def getBook(sn):
    if sn in ['创世记', '创', 'GENESIS', 'Genesis', 'genesis', 'GEN', 'Gen', 'gen', '创世纪', 'csj']:
        return 'Gen', '创世记'
    
    elif sn in ['出埃及记', '出', '', '', '', 'EXO', 'Exo', 'exo', 'cajj'] :
        return 'Exo', '出埃及记'
    
    elif sn in ['利未记', '利', '', '', '', 'LEV', 'Lev', 'lev', '利未', 'lwj'] :
        return 'Lev', '利未记'
    
    elif sn in ['民数记', '民', '', '', '', 'NUM', 'Num', 'num', 'msj'] :
        return 'Num', '民数记'
    
    elif sn in ['申命记', '申', '', '', '', 'DEU', 'Deu', 'deu', 'smj'] :
        return 'Deu', '申命记'
    
    elif sn in ['约书亚记', '书', '', '', '', 'JOS', 'Jos', 'jos', 'ysyj'] :
        return 'Jos', '约书亚记'
    
    elif sn in ['士师记', '士', '', '', '', 'JUG', 'Jug', 'jug', 'ssj'] :
        return 'Jug', '士师记'
    
    elif sn in ['路得记', '得', '', '', '', 'RUT', 'Rut', 'rut', 'ldj'] :
        return 'Rut', '路得记'
    
    elif sn in ['撒母耳记上', '撒上', '', '', '', '1SA', '1Sa', '1sa', 'smejs', 'smej1'] :
        return '1Sa', '撒母耳记上'
    
    elif sn in ['撒母耳记下', '撒下', '', '', '', '2SA', '2Sa', '2sa', 'smejx', 'smej2'] :
        return '2Sa', '撒母耳记下'
    
    elif sn in ['列王纪上', '列上', '', '', '', '1KI', '1Ki', '1ki', '列王记上', 'lwjs', 'lwj1'] :
        return '1Ki', '列王纪上'
    
    elif sn in ['列王纪下', '列下', '', '', '', '2KI', '2Ki', '2ki', '列王记下', 'lwjx', 'lwj2'] :
        return '2Ki', '列王纪下'
    
    elif sn in ['历代志上', '代上', '', '', '', '1CH', '1Ch', '1ch', 'ldzs', 'ldz1'] :
        return '1Ch', '历代志上'
    
    elif sn in ['历代志下', '代下', '', '', '', '2CH', '2Ch', '2ch', 'ldzx', 'ldz2'] :
        return '2Ch', '历代志下'
    
    elif sn in ['以斯拉记', '拉', '', '', '', 'EZR', 'Ezr', 'ezr', 'yslj'] :
        return 'Ezr', '以斯拉记'
    
    elif sn in ['尼希米记', '尼', '', '', '', 'NEH', 'Neh', 'neh', 'nxmj'] :
        return 'Neh', '尼希米记'
    
    elif sn in ['以斯帖记', '斯', '', '', '', 'EST', 'Est', 'est', '以斯贴记', 'ystj'] :
        return 'Est', '以斯帖记'
    
    elif sn in ['约伯记', '伯', '', '', '', 'JOB', 'Job', 'job', 'ybj'] :
        return 'Job', '约伯记'
    
    elif sn in ['诗篇', '诗', '', '', '', 'PSM', 'Psm', 'psm', 'sp'] :
        return 'Psm', '诗篇'
    
    elif sn in ['箴言', '箴', '', '', '', 'PRO', 'Pro', 'pro', '箴言书', 'zy'] :
        return 'Pro', '箴言'
    
    elif sn in ['传道书', '传', '', '', '', 'ECC', 'Ecc', 'ecc', 'cds'] :
        return 'Ecc', '传道书'
   
    elif sn in ['雅歌', '歌', '', '', '', 'SON', 'Son', 'son', 'yg'] :
        return 'Son', '雅歌'
    
    elif sn in ['以赛亚书', '赛', '', '', '', 'ISA', 'Isa', 'isa', 'ysys'] :
        return 'Isa', '以赛亚书'
    
    elif sn in ['耶利米书', '耶', '', '', '', 'JER', 'Jer', 'jer', 'ylms'] :
        return 'Jer', '耶利米书'
    
    elif sn in ['耶利米哀歌', '哀', '', '', '', 'LAM', 'Lam', 'lam', 'ylmag'] :
        return 'Lam', '耶利米哀歌'
    
    elif sn in ['以西结书', '结', '', '', '', 'EZE', 'Eze', 'eze', 'yxjs'] :
        return 'Eze', '以西结书'
    
    elif sn in ['但以理书', '但', '', '', '', 'DAN', 'Dan', 'dan', 'dyls'] :
        return 'Dan', '但以理书'
    
    elif sn in ['何西阿书', '何', '', '', '', 'HOS', 'Hos', 'hos', 'hxas'] :
        return 'Hos', '何西阿书'
   
    elif sn in ['约珥书', '珥', '', '', '', 'JOE', 'Joe', 'joe', 'yes'] :
        return 'Joe', '约珥书'
    
    elif sn in ['阿摩司书', '摩', '', '', '', 'AMO', 'Amo', 'amo', 'amss'] :
        return 'Amo', '阿摩司书'
    
    elif sn in ['俄巴底亚书', '俄', '', '', '', 'OBA', 'Oba', 'oba', 'ebdys'] :
        return 'Oba', '俄巴底亚书'
    
    elif sn in ['约拿书', '拿', '', '', '', 'JON', 'Jon', 'jon', 'yns'] :
        return 'Jon', '约拿书'
    
    elif sn in ['弥迦书', '弥', '', '', '', 'MIC', 'Mic', 'mic', 'mjs'] :
        return 'Mic', '弥迦书',
    
    elif sn in ['那鸿书', '鸿', '', '', '', 'NAH', 'Nah', 'nah', 'nhs'] :
        return 'Nah', '那鸿书'
    
    elif sn in ['哈巴谷书', '哈', '', '', '', 'HAB', 'Hab', 'hab', 'hbgs'] :
        return 'Hab', '哈巴谷书'
    
    elif sn in ['西番雅书', '番', '', '', '', 'ZEP', 'Zep', 'zep', 'xfys'] :
        return 'Zep', '西番雅书'
    
    elif sn in ['哈该书', '该', '', '', '', 'HAG', 'Hag', 'hag', 'hgs'] :
        return 'Hag', '哈该书'
    
    elif sn in ['撒迦利亚书', '亚', '', '', '', 'ZEC', 'Zec', 'zec', 'sjlys'] :
        return 'Zec', '撒迦利亚书'
    
    elif sn in ['玛拉基书', '玛', '', '', '', 'MAL', 'Mal', 'mal', 'mljs'] :
        return 'Mal', '玛拉基书'
    
    elif sn in ['马太福音', '太', '', '', '', 'MAT', 'Mat', 'mat', 'mtfy'] :
        return 'Mat', '马太福音'
    
    elif sn in ['马可福音', '可', '', '', '', 'MAK', 'Mak', 'mak', 'mkfy'] :
        return 'Mak', '马可福音'
    
    elif sn in ['路加福音', '路', '', '', '', 'LUK', 'Luk', 'luk', 'ljfy'] :
        return 'Luk', '路加福音'
    
    elif sn in ['约翰福音', '约', '', '', '', 'JHN', 'Jhn', 'jhn', 'yhfy'] :
        return 'Jhn', '约翰福音'
    
    elif sn in ['使徒行传', '徒', '', '', '', 'ACT', 'Act', 'act', 'stxz'] :
        return 'Act', '使徒行传'
    
    elif sn in ['罗马书', '罗', '', '', '', 'ROM', 'Rom', 'rom', 'lms'] :
        return 'Rom', '罗马书'
    
    elif sn in ['哥林多前书', '林前', '', '', '', '1CO', '1Co', '1co', 'gldqs', 'gld1'] :
        return '1Co', '哥林多前书'
    
    elif sn in ['哥林多后书', '林后', '', '', '', '2CO', '2Co', '2co', 'gldhs', 'gld2'] :
        return '2Co', '哥林多后书'
    
    elif sn in ['加拉太书', '加', '', '', '', 'GAL', 'Gal', 'gal', 'jlts'] :
        return 'Gal', '加拉太书'
    
    elif sn in ['以弗所书', '弗', '', '', '', 'EPH', 'Eph', 'eph', 'yfss'] :
        return 'Eph', '以弗所书'
    
    elif sn in ['腓立比书', '腓', '', '', '', 'PHL', 'Phl', 'phl', 'flbs'] :
        return 'Phl', '腓立比书'
    
    elif sn in ['歌罗西书', '西', '', '', '', 'COL', 'Col', 'col', 'glxs'] :
        return 'Col', '歌罗西书'
    
    elif sn in ['贴撒罗尼迦前书', '贴前', '', '', '', '1TS', '1Ts', '1ts', 'tslnjqs', 'tslnj1'] :
        return '1Ts', '贴撒罗尼迦前书'
    
    elif sn in ['贴撒罗尼迦后书', '贴后', '', '', '', '2TS', '2Ts', '2ts', 'tslnjhs', 'tslnj2'] :
        return '2Ts', '贴撒罗尼迦后书'
    
    elif sn in ['提摩太前书', '提前', '', '', '', '1TI', '1Ti', '1ti', 'tmtqs', 'tmt1'] :
        return '1Ti', '提摩太前书'
    
    elif sn in ['提摩太后书', '提后', '', '', '', '2TI', '2Ti', '2ti', 'tmths', 'tmt2'] :
        return '2Ti', '提摩太后书'
    
    elif sn in ['提多书', '多', '', '', '', 'TIT', 'Tit', 'tit','tds'] :
        return 'Tit', '提多书'
    
    elif sn in ['腓利门书', '门', '', '', '', 'PHM', 'Phm', 'phm', 'flms'] :
        return 'Phm', '腓利门书'
    
    elif sn in ['希伯来书', '来', '', '', '', 'HEB', 'Heb', 'heb','xbls'] :
        return 'Heb', '希伯来书'
    
    elif sn in ['雅各书', '雅', '', '', '', 'JAS', 'Jas', 'jas','ygs'] :
        return 'Jas', '雅各书'
    
    elif sn in ['彼得前书', '彼前', '', '', '', '1PE', '1Pe', '1pe','bdqs'] :
        return '1Pe', '彼得前书'
    
    elif sn in ['彼得后书', '彼后', '', '', '', '2PE', '2Pe', '2pe','bdhs'] :
        return '2Pe', '彼得后书'
    
    elif sn in ['约翰一书', '约一', '', '', '', '1JN', '1Jn', '1jn','yhys'] :
        return '1Jn', '约翰一书'
    
    elif sn in ['约翰二书', '约二', '', '', '', '2JN', '2Jn', '2jn','yhes'] :
        return '2Jn', '约翰二书'
    
    elif sn in ['约翰三书', '约三', '', '', '', '3JN', '3Jn', '3jn','yhss'] :
        return '3Jn', '约翰三书'
    
    elif sn in ['犹大书', '犹', '', '', '', 'JUD', 'Jud', 'jud','yds'] :
        return 'Jud', '犹大书'
    
    elif sn in ['启示录', '启', '', '', '', 'REV', 'Rev', 'rev', 'qsl'] :
        return 'Rev', '启示录'
    else:
        return None
