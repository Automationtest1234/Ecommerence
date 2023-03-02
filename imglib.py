import time
import warnings
from bs4 import BeautifulSoup
import matplotlib

matplotlib.use('Agg')
from matplotlib import pyplot as plt
import pyautogui
from PIL import Image
import shutil
import os
import matplotlib

matplotlib.use('Agg')
final = "Test_report/Final_Report.html"
flag = False
flag_1 = False


# Opening and reading the html file
def my_function(passCount, failCount, total, curr_time, today, tem,
                note, count, f_name, report_path, version):
    global pageTemplate
    if version is "NO VERSION IN INPUTS":
        version = "NO VERSION IN INPUTS"
    else:
        print("VERSION IS FOUND IN INPUTS")
    Note = note
    name = ""
    r_path = report_path
    if flag is True:
        # pie chart
        # noinspection SpellCheckingInspection
        name = r"%s\chart\piechart%s.png" % (r_path, f_name)
        labels = ["PASS", "FAIL"]
        colors = ['green', 'red']
        sizes = [passCount, failCount]
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', )
        plt.legend(title="RESULT:")
        plt.savefig(name, dpi=90)
        image = Image.open(name)
        new_image = image.resize((430, 330))
        chart_name = r"%s" % name
        new_image.save(chart_name)
        plt.close()
        name = r"chart\piechart%s.png" % f_name
    try:
        pageTemplate = open(r"Images\pageTemp.html", "r")
        warnings.filterwarnings('ignore')
    except:
        note.write(">> There is no pageTemp.html in your folder ")

    templatecontents = pageTemplate.read()
    soup = BeautifulSoup(templatecontents, "html")
    htmlcontent = BeautifulSoup("<br>", "html")
    soup.append(htmlcontent)
    htmlcontent = BeautifulSoup(f"<body><center><b>SOFTWARE VERSION :  {version}<br></center></b>", "html")
    soup.append(htmlcontent)
    img = BeautifulSoup(f'<img  align=right  src="{name}" />', 'html')
    soup.append(img)
    htmlcontent = BeautifulSoup("<br>", "html")
    soup.append(htmlcontent)
    htmlcontent = BeautifulSoup("<br>", "html")
    soup.append(htmlcontent)
    htmlcontent = BeautifulSoup(f"<b>TOTAL NO OF TEST CASE : {total}<br></b>", "html")
    soup.append(htmlcontent)
    htmlcontent = BeautifulSoup("<br>", "html")
    soup.append(htmlcontent)
    htmlcontent = BeautifulSoup(f"<b>TOTAL NO OF PASS : {passCount} <br><b>", "html")
    soup.append(htmlcontent)
    htmlcontent = BeautifulSoup("<br>", "html")
    soup.append(htmlcontent)
    htmlcontent = BeautifulSoup(f"<b>TOTAL NO OF FAIL : {failCount}<br><b>", "html")
    soup.append(htmlcontent)
    htmlcontent = BeautifulSoup("<br>", "html")
    soup.append(htmlcontent)
    htmlcontent = BeautifulSoup(f"<b><right>TIME : {curr_time}</right><br><b>", "html")
    soup.append(htmlcontent)
    htmlcontent = BeautifulSoup("<br>", "html")
    soup.append(htmlcontent)
    htmlcontent = BeautifulSoup(f"<b>DATE : {today}<br><b>", "html")
    soup.append(htmlcontent)
    htmlcontent = BeautifulSoup("</body>", "html")
    soup.append(htmlcontent)
    report = open(tem, "r")
    reportcontents = report.read()
    reportsoup = BeautifulSoup(reportcontents, "html")
    soup.append(reportsoup)
    report.close()

    # Code to save the changes in 'output.html' file
    save_changes = soup.prettify("utf-8")
    report_name = "%s/%s_Final_Report.html" % (r_path, f_name)
    new_report = "%s/Final_Report%s.html" % (r_path, count)

    with open(report_name, "wb") as file:
        file.write(save_changes)

    if flag_1 is True:
        report.close()
        pageTemplate.close()
        file.close()
        shutil.rmtree(r"%s\table" % r_path)
        shutil.rmtree(r"Images\Input")
        shutil.rmtree(r"Images\Cropped_pre_defined")
        shutil.rmtree(r"Images\Cropped_Input")
        shutil.rmtree(r"Images\Output")
        shutil.rmtree(r"Images\Captured")
        # shutil.rmtree(r"Images\pageTemp.html")
        try:
            os.remove(r"Images\pageTemp.html")
        except:
            pass
        try:
            os.remove(r"Images\black.png")
        except:
            pass
        try:
            os.remove(r"Images\no_image.PNG")
        except:
            pass
        try:
            os.remove(r"Images\NOT_RECEIVED.PNG")
        except:
            pass

        time.sleep(1)
        Note.write(">> >> AUTOMATION IS COMPLETED AND HTML IS GENERATED SUCCESSFULLY...! :) ")
        Note.close()
        print(">> >> AUTOMATION IS DONE AND HTML IS GENERATED SUCCESSFULLY...! :) ")
        alert = pyautogui.alert(text="AUTOMATION IS COMPLETED AND HTML IS GENERATED SUCCESSFULLY",
                                title=" SUCCESS MESSAGE! ")
