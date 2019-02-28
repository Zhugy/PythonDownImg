import requests, os, pprint, bs4, re

class DownLoadBaiduGirl():

    def loadHtml(self, url):
        req = requests.get(url)
        req.encoding = 'utf-8'
        l = self.getImageUrlList(req.text)
        self.saveImages(l)

    def getImageUrlList(self, htmls):
        group = bs4.BeautifulSoup(htmls, 'html.parser')
        list = group.find_all('li')

        imagStrArr = []

        for item in list:
            if item.img == None:
                continue
            img = item.img
            imagStrArr.append(img.get('src'))
        return imagStrArr


    def saveImages(self, imagStrArr):

        filePath = '/Users/xxxxx/xxxxxx/Python/PythonDownImg/BaiduGirl'

        if not os.path.isdir(filePath):

            os.mkdir(filePath)

        for index in range(len(imagStrArr)):
            imaD = requests.get(imagStrArr[index])

            fileName = imagStrArr[index].split('/')
            fileName = fileName.pop()
            pprint.pprint('开始下载第%s张'%(str(index)))
            imagePathStr = 'BaiduGirl/' + fileName
            with open(imagePathStr, 'wb') as fileP:
                for chunk in imaD.iter_content(1024):
                    fileP.write(chunk)


download = DownLoadBaiduGirl()
download.loadHtml('https://www.2717.com/tag/625.html')
