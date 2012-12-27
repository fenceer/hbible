# coding:utf-8
'''
Created on 2012-12-27

@author: fenceer
'''

import re
import web

db = web.config.db

def checkChapter(ss):
    pattern = ur'^(\D{1,20})(\d{1,3})\s{0,3}(?:\/|:){0,1}\s{0,3}(\d{0,3}\s{0,3}-{0,1}\s{0,3}\d{0,3})$'
    # match = re.search(r'\d', ss)
    match = re.match(pattern, ss)
    if match:
        sn = match.group(1).strip()
        book = getBook(sn)
        chp = int(match.group(2))
        if match.group(3):
            jie = match.group(3).split('-') 
            start = int(jie[0])
            if len(jie) == 2:
                end = int(jie[1]) if jie[1] else 900
        else:
            start = 0
            end = 900
        if start > end:
            start = end
            end = start
        start = chp * 1000 + start
        end = chp * 1000 + end
        if book:
            bb = db.GB.find({'book':book, '$and':[
                                           {'index':{'$gte':start}},
                                           {'index':{'$lte':end}}]})
            text = ''
            for b in list(bb):
                text += b['text']
            return text
        else:
            return None
    else:
        return None

def getBook(sn):
    if sn == 'gen':
        return 'Gen'
    if sn in ['创世记', '创', 'GENESIS', 'Genesis', 'genesis', 'GEN', 'Gen', 'gen']:
        return 'Gen'
    elif sn in ['出埃及记', '出', '', '', '', 'EXO', 'Exo', 'exo'] :
        return 'Exo'
    
    elif sn in ['利未记', '利', '', '', '', 'LEV', 'Lev', 'lev'] :
        return 'Lev'
    
    elif sn in ['民数记', '民', '', '', '', 'NUM', 'Num', 'num'] :
        return 'Num'
    
    elif sn in ['申命记', '申', '', '', '', 'DEU', 'Deu', 'deu'] :
        return 'Deu'
    
    elif sn in ['约书亚记', '书', '', '', '', 'JOS', 'Jos', 'jos'] :
        return 'Jos'
    
    elif sn in ['士师记', '士', '', '', '', 'JUG', 'Jug', 'jug'] :
        return 'Jug'
    
    elif sn in ['路得记', '得', '', '', '', 'RUT', 'Rut', 'rut'] :
        return 'Rut'
    
    elif sn in ['撒母耳记上', '撒上', '', '', '', '1SA', '1Sa', '1sa'] :
        return '1Sa'
    
    elif sn in ['撒母耳记下', '撒下', '', '', '', '2SA', '2Sa', '2sa'] :
        return '2Sa'
    
    elif sn in ['列王记上', '列上', '', '', '', '1KI', '1Ki', '1ki'] :
        return '1Ki'
    
    elif sn in ['列王记下', '列下', '', '', '', '2KI', '2Ki', '2ki'] :
        return '2Ki'
    
    elif sn in ['历代记上', '代上', '', '', '', '1CH', '1Ch', '1ch'] :
        return '1Ch'
    
    elif sn in ['历代记下', '代下', '', '', '', '2CH', '2Ch', '2ch'] :
        return '2Ch'
    
    elif sn in ['以斯拉', '拉', '', '', '', 'EZR', 'Ezr', 'ezr'] :
        return 'Ezr'
    
    elif sn in ['尼希米', '尼', '', '', '', 'NEH', 'Neh', 'neh'] :
        return 'Neh'
    
    elif sn in ['以斯贴', '斯', '', '', '', 'EST', 'Est', 'est'] :
        return 'Est'
    
    elif sn in ['约伯记', '伯', '', '', '', 'JOB', 'Job', 'job'] :
        return 'Job'
    
    elif sn in ['诗篇', '诗', '', '', '', 'PSM', 'Psm', 'psm'] :
        return 'Psm'
    
    elif sn in ['箴言书', '箴', '', '', '', 'PRO', 'Pro', 'pro'] :
        return 'Pro'
    
    elif sn in ['传道书', '传', '', '', '', 'ECC', 'Ecc', 'ecc'] :
        return 'Ecc'
   
    elif sn in ['雅歌', '歌', '', '', '', 'SON', 'Son', 'son'] :
        return 'Son'
    
    elif sn in ['以赛亚书', '赛', '', '', '', 'ISA', 'Isa', 'isa'] :
        return 'Isa'
    
    elif sn in ['耶利米书', '耶', '', '', '', 'JER', 'Jer', 'jer'] :
        return 'Jer'
    
    elif sn in ['耶利米哀歌', '哀', '', '', '', 'LAM', 'Lam', 'lam'] :
        return 'Lam'
    
    elif sn in ['以西结书', '结', '', '', '', 'EZE', 'Eze', 'eze'] :
        return 'Eze'
    
    elif sn in ['但以理书', '但', '', '', '', 'DAN', 'Dan', 'dan'] :
        return 'Dan'
    
    elif sn in ['何西阿书', '何', '', '', '', 'HOS', 'Hos', 'hos'] :
        return 'Hos'
   
    elif sn in ['约珥书', '珥', '', '', '', 'JOE', 'Joe', 'joe'] :
        return 'Joe'
    
    elif sn in ['阿摩司书', '摩', '', '', '', 'AMO', 'Amo', 'amo'] :
        return 'Amo'
    
    elif sn in ['俄巴底亚书', '俄', '', '', '', 'OBA', 'Oba', 'oba'] :
        return 'Oba'
    
    elif sn in ['约拿书', '拿', '', '', '', 'JON', 'Jon', 'jon'] :
        return 'Jon'
    
    elif sn in ['弥迦书', '弥', '', '', '', 'MIC', 'Mic', 'mic'] :
        return 'Mic'
    
    elif sn in ['那鸿书', '鸿', '', '', '', 'NAH', 'Nah', 'nah'] :
        return 'Nah'
    
    elif sn in ['哈巴谷书', '哈', '', '', '', 'HAB', 'Hab', 'hab'] :
        return 'Hab'
    
    elif sn in ['西番雅书', '番', '', '', '', 'ZEP', 'Zep', 'zep'] :
        return 'Zep'
    
    elif sn in ['哈该书', '该', '', '', '', 'HAG', 'Hag', 'hag'] :
        return 'Hag'
    
    elif sn in ['撒迦利亚书', '亚', '', '', '', 'ZEC', 'Zec', 'zec'] :
        return 'Zec'
    
    elif sn in ['玛拉基书', '玛', '', '', '', 'MAL', 'Mal', 'mal'] :
        return 'Mal'
    
    elif sn in ['马太福音', '太', '', '', '', 'MAT', 'Mat', 'mat'] :
        return 'Mat'
    
    elif sn in ['马可福音', '可', '', '', '', 'MAK', 'Mak', 'mak'] :
        return 'Mak'
    
    elif sn in ['路加福音', '路', '', '', '', 'LUK', 'Luk', 'luk'] :
        return 'Luk'
    
    elif sn in ['约翰福音', '约', '', '', '', 'JHN', 'Jhn', 'jhn'] :
        return 'Jhn'
    
    elif sn in ['使徒行传', '徒', '', '', '', 'ACT', 'Act', 'act'] :
        return 'Act'
    
    elif sn in ['罗马书', '罗', '', '', '', 'ROM', 'Rom', 'rom'] :
        return 'Rom'
    
    elif sn in ['哥林多前书', '林前', '', '', '', '1CO', '1Co', '1co'] :
        return '1Co'
    
    elif sn in ['哥林多后书', '林后', '', '', '', '2CO', '2Co', '2co'] :
        return '2Co'
    
    elif sn in ['加拉太书', '加', '', '', '', 'GAL', 'Gal', 'gal'] :
        return 'Gal'
    
    elif sn in ['以弗所书', '弗', '', '', '', 'EPH', 'Eph', 'eph'] :
        return 'Eph'
    
    elif sn in ['腓立比书', '腓', '', '', '', 'PHL', 'Phl', 'phl'] :
        return 'Phl'
    
    elif sn in ['歌罗西书', '西', '', '', '', 'COL', 'Col', 'col'] :
        return 'Col'
    
    elif sn in ['贴撒罗尼迦前书', '贴前', '', '', '', '1TS', '1Ts', '1ts'] :
        return '1Ts'
    
    elif sn in ['贴撒罗尼迦后书', '贴后', '', '', '', '2TS', '2Ts', '2ts'] :
        return '2Ts'
    
    elif sn in ['提摩太前书', '提前', '', '', '', '1TI', '1Ti', '1ti'] :
        return '1Ti'
    
    elif sn in ['提摩太后书', '提后', '', '', '', '2TI', '2Ti', '2ti'] :
        return '2Ti'
    
    elif sn in ['提多书', '多', '', '', '', 'TIT', 'Tit', 'tit'] :
        return 'Tit'
    
    elif sn in ['腓利门书', '门', '', '', '', 'PHM', 'Phm', 'phm'] :
        return 'Phm'
    
    elif sn in ['希伯来书', '来', '', '', '', 'HEB', 'Heb', 'heb'] :
        return 'Heb'
    
    elif sn in ['雅各书', '雅', '', '', '', 'JAS', 'Jas', 'jas'] :
        return 'Jas'
    
    elif sn in ['彼得前书', '彼前', '', '', '', '1PE', '1Pe', '1pe'] :
        return '1Pe'
    
    elif sn in ['彼得后书', '彼后', '', '', '', '2PE', '2Pe', '2pe'] :
        return '2Pe'
    
    elif sn in ['约翰一书', '约一', '', '', '', '1JN', '1Jn', '1jn'] :
        return '1Jn'
    
    elif sn in ['约翰二书', '约二', '', '', '', '2JN', '2Jn', '2jn'] :
        return '2Jn'
    
    elif sn in ['约翰三书', '约三', '', '', '', '3JN', '3Jn', '3jn'] :
        return '3Jn'
    
    elif sn in ['犹大书', '犹', '', '', '', 'JUD', 'Jud', 'jud'] :
        return 'Jud'
    
    elif sn in ['启示录', '启', '', '', '', 'REV', 'Rev', 'rev'] :
        return 'Rev'
    else:
        return None
