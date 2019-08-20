from config import Config
import mosspy

userid = Config.userid

m = mosspy.Moss(userid, "python")
m.addBaseFile("submission/base.py")
m.addFilesByWildcard("submission/std*_quiz02.py")

url = m.send()
print("Report Url: " + url)
m.saveWebPage(url, "submission/report.html")
mosspy.download_report(url, "submission/report/", connections=8)
