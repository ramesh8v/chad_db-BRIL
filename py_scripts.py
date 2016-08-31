import psycopg2 as pg2
def db(marker, chrome, dist_min, dist_max):
    conn = pg2.connect(database='chad_db',user='ubuntu', password='hello')
    cur = conn.cursor()
    if marker == 'all' and chrome == 'all':
        cur.execute("SELECT marker,  chromosome , distance FROM final WHERE distance BETWEEN %s AND %s;" % (dist_min, dist_max))
    elif marker == 'all':
        cur.execute("SELECT marker,  chromosome , distance FROM final WHERE chromosome = '%s' AND distance BETWEEN %s AND %s;" % (chrome,dist_min, dist_max))
    elif chrome == 'all':
        cur.execute("SELECT marker,  chromosome , distance FROM final WHERE marker = '%s' AND distance BETWEEN %s AND %s;" % (marker, dist_min, dist_max))
    
    else:
        cur.execute("SELECT marker,  chromosome , distance FROM final WHERE marker = '%s' AND chromosome = '%s' AND distance BETWEEN %s AND %s;" % (marker,chrome, dist_min, dist_max))
    dat = cur.fetchall()
    conn.close ()
    return dat

def listtodict(indat):
    dict = {}
    i = 0
    for lists in indat:
        dict[i] = list(lists)
        i+=1
    return dict
    
def initaldbcall():
    conn = pg2.connect(database='chad_db',user='ubuntu', password='hello')
    cur = conn.cursor()
    cur.execute("SELECT marker,  chromosome , distance FROM final;")
    dat = cur.fetchall()
    conn.close ()
    return dat
    
def fetchdbsd(marker):
    dict = {}
    conn = pg2.connect(database='chad_db',user='ubuntu', password='hello')
    cur = conn.cursor()
    cur.execute("SELECT * FROM final WHERE marker = '%s'" % (marker))
    dat = cur.fetchall()
    heads = ['NUll', 'Marker','Chromosome','Distance','19999','20000','20001','20002','20004','20005','20006','20007','20008','20009','20010','20011','20013','20014','20015','20016','20018','20020','20021','20022','20023','20024','20025','20026','20027','20030','20031','20032','20033','20034','20035','20036','20038','20039','20040','20041','20042','20043','20044','20045','20046','20047','20048','20049','20050','20051','20052','20054','20055','20056','20057','20058','20059','20060','20061','20062','20063','20064','20065','20066','20067','20068','20069','20070','20071','20072','20073','20074','20075','20076','20077','20078','20079','20080','20081','20082','20083','20084','20085','20086','20087','20088','20089','20091','20092','20093','20094','20095','20096','20097','20098','20099','20100','20101','20102','20103','20105','20106','20107','20108','20109','20110','20111','20112','20113','20114','20115','20116','20117','20118','20119','20120','20121','20122','20123','20124','20126','20127','20128','20129','20131','20132','20133','20134','20136','20137','20139','20140','20142','20143','20144','20145','20146','20147','20148','20149','20150','20152','20153','20154','20156','20157','20158','20159','20160','20161','20162','20163','20164','20165','20166','20167','20168','20169','20170','20171','20172','20173','20174','20175','20176','20177','20178','20179','20180','20181','20182','20183','20184','20186','20187','20188','20189','20190','20191','20192','20193','20194','20195','20196','20197','20198','20199','20201','20203','20205','20206','20207','20209','20210','20211','20212','20213','20214','20215']
    dat= list(dat[0])
    dict['DIC_g'], dict['LGD_g'] = [], []
    for i in range(0, (len(heads)-1)):
        if i <= 3:
            dict[heads[i]] = dat[i]
        else:
            if dat[i] == 'G':
                dict['DIC_g'].append(heads[i])
            if dat[i] == 'L':
                dict['LGD_g'].append(heads[i])
        
    dict['leng'] = max(len(dict['DIC_g']), len(dict['LGD_g']))
    #print(dict)
    conn.close ()
    return dict
    
def fetchdbseq(marker):
    dict = {}
    conn = pg2.connect(database='chad_db',user='ubuntu', password='hello')
    cur = conn.cursor()
    cur.execute("SELECT * FROM seq WHERE marker = '%s'" % (marker))
    dat = cur.fetchall()
    heads = ['NUll','Marker','Sequence']
    dat= list(dat[0])
    conn.close ()
    return dat