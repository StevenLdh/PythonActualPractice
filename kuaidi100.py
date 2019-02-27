import requests
def getExpressInfo(number):
    url = 'http://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text=%s'%number
    for item in requests.get(url).json()['auto']:
        companyname=item["comCode"]
        url='http://www.kuaidi100.com/query?type=%s&postid=%s'%(companyname,number)
        for ie in requests.get(url).json()["data"]:
            print(ie)

def getExpressInfoOne(number):
    url = 'http://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text=%s'%number
    for item in requests.get(url).json()['auto']:
        companyname=item["comCode"]
        print(companyname)
        url='http://www.kuaidi100.com/query?type=%s&postid=%s'%(companyname,number)
        for ie in requests.get(url).json()["data"]:
            print(ie)

getExpressInfo("75122515334970")

getExpressInfoOne("3874380444631")