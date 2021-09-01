import string
import csv

precedingWords="louise terry charlie mrs mr ms fletcher charlie dan clive".lower().split(" ")

followingWords = "fisher tom democrat democratic Roberts bale henry ziege zieges Malcolm bassedas jetzlsperger wulff name diors malcolms Lacroix liaigre liaigres breitsprecher rucker horsfall califano carrere Cullen Andersen wolmar wolmars bales parenti caryl aid aids vieri zeige Edwards slater andersens stoica bob stewart vander vanders Williams labit fraser chapirononly Karen karembeu furuseth Philips goldbach kurt Louboutin friedrich neffe vinck gross garricks wolff fenouillats wardthomas tony fox Rutherford fittipaldi ingebrigtsem mr maher democraticsocialist tetzlaff thielemann immler sir adams eugenolsen david mal poell salvesen democratled ostro moueix noyer vieris sautter chazot slaters nyby brian delteil karembeus Gonzalez vieiri panucci foxs worns moore karambeu bassed Garrick dreux evans Anderson alverdi van delaosa Gabriel kracht scheider von albrechts horne Hamilton furr iv colportage clacher thielemanns strauss curnyn holden haines adine v boltanski barnard de boltanksi ix Cormack snyman alexander saverimutto owen schwaiger mayer grossdavid mathias neilson rea hefti keller mcbride bach levrings pierce Britney Jennings mcgee ngo moraga Elliott benteke bentekes jessenhealth Jessen porter eriksen siriano thorntons thornton mouysset fa seifert fuchs kabaseleshares kabasele wood pulisic horner burgess eriksens broughton trumble Koch doidge vassie vassiechair porters doidges lindmeier atsu kouame adam estrosi beneteke martin oreilly hartnagel ilic purslow gerhaher louboutins dawkins poulsen vieriggetty mike karlsson lindner stellini nguessan vieler miller jones denton millercaters drosten bouvard davies kabore Walton oliva kabaseles gentner Mitchell Austin slattery folau norgaard norgaards galani wade grey Tierney dodige6 eldershaw williamstrained burri hirte Hepburn gysin atsus metz hammer clavier sylt kraehling Laettner kurts milz coleman hartnagel brunaepa mulamba rika reyes taylor Wakeford marcolivier fennesz carino curnyns smalls salaroli namphy du Jacob alzmann uruzquieta schembri prudhomme mccaffery eide leech herff sparkes essiambre ryan schlaubitx tym crahay mccrea hartmann karagiannidis berger kawley brown bentejohn juin Matheson walzer lata odendahl stadler stokes baleera dingert nicholls trumbles waltons fischer diaz Michel mathis lumbye blackshaw Vincent james jakobssen aslundgreenpeace bunse wilcox deilmann manahl iddon nade burgesss pulisics tortu stolting hiquana pulisicstill ganczarski adel althaus maas gogos zucconi beadell fink colemans hilber canales murphy elden santos jain burton lundgaard greys malford mccaffrey Puglisi woolfenden streich jullien lealiifano svanes Wilson cole levett cowan germain dunn sirano human Huber pence Barraclough loeben imholt selinger machowski keysers turner olivas poltera tello Larsen aslundgreenpeace ii nnabugwu holtz Ã¡lvarez lanier serratos trimbles trimua ulbrich pavÃ³n petzolds ebenbauer natalehjorth schulz hogg chan mendes nÃ¸rgaard mercuri garin emmerich pÃ©rez democrats faes bourgois dalheim allhusen dafreville fassnachts lambright breyer diordries ducou agcas Pollack kasasele Härtnagel Dailly".lower().split(" ")

containingWords = "Christiansen christianfrasermirrorcouk irresponsiblechristianfrasermirrorcouk Christiane christiansens christiana Christiania willsherchristian christiani christianna collcuttchristian Christiansted hewettchristian christianedwards williamschristian muscularchristian woodwardchristian Christiana christianah christianne christianas thunbergchristiana christianalbrechtsuniversitÃ¤t choosechristiana christiansborg wwwchristianlouboutincom heinzchristian christiano Christiansburg christianshavn christianee jenschristian".lower().split(" ")

def cleanFile(file, cleanFile):
    readFile = open(file)
    CleanFile = open(cleanFile, "w")

    articles = readFile.read().split("Load-Date:")
    if True:
        article = articles[0]
        fixedArticle = ""
        tempLines = []
        storeTemp = True
        bodyPassed = False
        for line in article.split("\n"):
            if line:
                if "Copyright" == line[:9] and storeTemp:
                    storeTemp = False
                    if "Edition" in tempLines[-1]:
                        tempLines = tempLines[:len(tempLines) - 3]
                    else:
                        tempLines = tempLines[:len(tempLines) - 2]
                    for tempLine in tempLines:
                        fixedArticle += tempLine
                        fixedArticle += "\n"
                    fixedArticle += "\n\n"
                if storeTemp:
                    tempLines.append(line)
                if bodyPassed:
                    fixedArticle += line
                    fixedArticle += "\n"
                if "Body" == line:
                    bodyPassed = True
        fixedArticle += "\n\n\n\n"
        CleanFile.write(fixedArticle)
    for article in articles[1:-1]:
        fixedArticle = ""
        tempLines = []
        storeTemp = True
        bodyPassed = False
        for line in article.split("\n"):
            if line:
                if "Copyright" == line[:9] and storeTemp:
                    storeTemp = False
                    if "Edition" in tempLines[-1]:
                        tempLines = tempLines[1:len(tempLines) - 3]
                    else:
                        tempLines = tempLines[1:len(tempLines) - 2]
                    for tempLine in tempLines:
                        fixedArticle += tempLine
                        fixedArticle += "\n"
                    fixedArticle += "\n\n"
                if storeTemp:
                    tempLines.append(line)
                if bodyPassed:
                    fixedArticle += line
                    fixedArticle += "\n"
                if "Body" == line:
                    bodyPassed = True
        fixedArticle += "\n\n\n\n"
        CleanFile.write(fixedArticle)

def splitYears(allArticlesFile, year2000File, year2020File):
    readFile = open(allArticlesFile)
    File2000 = open(year2000File, "w")
    File2020 = open(year2020File, "w")

    articles = readFile.read().split("END OF DOCUMENT")
    Articles2000 = 0
    Articles2020 = 0
    for article in articles[:-1]:
        publishDate = article.split("Load-Date:")[1]
        if "2020" in publishDate:
            Articles2020 += 1
            File2020.write(article)
        else:
            Articles2000 += 1
            File2000.write(article)
    File2000.close()
    File2020.close()

def removeBlockTimeLines(file, cleanFile):
    readFile = open(file)
    data = readFile.readlines()
    writeFile = open(cleanFile, "w")
    count = 0
    for line in data:
        if "block-time" in line:
            count += 1
        else:
            writeFile.write(line)
    writeFile.close()

def removeFilterArticles(file, cleanFile, precedingWordsFilter, followingWordsFilter, containingWordsFilter):
    readFile = open(file, encoding='UTF-8')
    writeFile = open(cleanFile, "w")
    articles = readFile.read().split("End of Document")
    titles = []

    for article in articles:
        if "Section: AUSTRALIA NEWS" in article:
            continue
        title = article.split("\n")[5]
        if title in titles:
            continue
        titles.append(title)
        articleCopy = article.translate(str.maketrans('', '', string.punctuation))
        articleCopy = articleCopy.replace("\n", " ")
        articleCopy = articleCopy.lower()
        articleCopy = articleCopy.split(" ")
        allowed = True
        if "christian" in articleCopy:
            x = 0
            for word in articleCopy:
                if word == "christian":
                    followingWord = articleCopy[x + 1]
                    if followingWord in followingWordsFilter:
                        allowed = False
                        break
                    precedingWord = articleCopy[x - 1]
                    if precedingWord in precedingWordsFilter:
                        allowed = False
                        break
                x += 1
        else:
            for word in articleCopy:
                if "christian" in word:
                    if word in containingWordsFilter:
                        allowed = False
                        break
        if allowed:
            writeFile.write(article)
            writeFile.write("END OF DOCUMENT")

    writeFile.close()

    finalOutput = open(cleanFile)

def getFilterOptions(articlesFile, csvFile):
    readFile = open(articlesFile, encoding='UTF-8')
    articles = readFile.read().split("End of Document")

    filters = {"christian": {}}

    for article in articles:
        article = article.translate(str.maketrans('', '', string.punctuation))
        article = article.replace("\n", " ")
        article = article.lower()
        article = article.split(" ")
        if "christian" in article:
            x = 0
            for word in article:
                if word == "christian":
                    word = article[x + 1]
                    if word in filters["christian"]:
                        filters["christian"][word] += 1
                    else:
                        filters["christian"][word] = 1
                x += 1
        else:
            for word in article:
                if "christian" in word:
                    if word in filters:
                        filters[word] += 1
                    else:
                        filters[word] = 1

    f = open(csvFile, 'w', newline='', encoding='utf-8')

    writer = csv.writer(f)

    writer.writerow(["Words following the word christian"])
    writer.writerow(["Word", "number of occurences"])

    for word in filters["christian"]:
        writer.writerow([word, filters["christian"][word]])

    writer.writerows([[""], [""]])
    writer.writerow(["Words containing christian"])
    for word in filters:
        if word != "christian":
            writer.writerow([word, filters[word]])

    f.close()

def getPrecedingFilter(articlesFile, csvFile):
    readFile = open(articlesFile, encoding='UTF-8')
    articles = readFile.read().split("End of Document")

    filters = {"christian": {}}

    for article in articles:
        article = article.translate(str.maketrans('', '', string.punctuation))
        article = article.replace("\n", " ")
        article = article.lower()
        article = article.split(" ")
        if "christian" in article:
            x = 0
            for word in article:
                if word == "christian" and x > 0:
                    word = article[x - 1]
                    y = 1
                    while(word == ""):
                        y += 1
                        word = article[x - y]
                    if word in filters["christian"]:
                        filters["christian"][word] += 1
                    else:
                        filters["christian"][word] = 1
                x += 1

    f = open(csvFile, 'w', newline='', encoding='utf-8')

    writer = csv.writer(f)

    writer.writerow(["Words preceding the word christian"])
    writer.writerow(["Word", "number of occurences"])

    for word in filters["christian"]:
        writer.writerow([word, filters["christian"][word]])

    f.close()

def countArticlesByPaper(articlesFile, csvFile):
    readFile = open(articlesFile)
    articles = readFile.read().split("Load-Date:")

    results = {"The Guardian": 0, "The Independent": 0, "Daily Star": 0, "The Mirror": 0, "The Telegraph": 0, "The Times": 0, "The Mail": 0, "The Sun": 0, "The Observer": 0, "The Express": 0}

    resultsWordCount = {"The Guardian": 0, "The Independent": 0, "Daily Star": 0, "The Mirror": 0, "The Telegraph": 0, "The Times": 0, "The Mail": 0, "The Sun": 0, "The Observer": 0, "The Express": 0}
    
    for article in articles[:-1]:
        article = article.split("\n")
        if article[0] != '':
            article.pop(0)
        article = list(filter(checkEmpty, article))
        if article[0][-1] == ';' or len(article[1]) == 1 or 'body last year failed to reveal whether he had conquered Everest 75 years ago. Now the team searching for his partner Sandy Irvine are determined to find the final proof' in article[1]:
            paper = article[2]
        else:
            paper = article[1]
        if "Guardian".lower() in paper.lower():
            results["The Guardian"] += 1
            resultsWordCount["The Guardian"] += len(''.join(article))
        elif "Independent".lower() in paper.lower():
            results["The Independent"] += 1
            resultsWordCount["The Independent"] += len(''.join(article))
        elif "Star".lower() in paper.lower():
            results["Daily Star"] += 1
            resultsWordCount["Daily Star"] += len(''.join(article))
        elif "Mirror".lower() in paper.lower():
            results["The Mirror"] += 1
            resultsWordCount["The Mirror"] += len(''.join(article))
        elif "Telegraph".lower() in paper.lower():
            results["The Telegraph"] += 1
            resultsWordCount["The Telegraph"] += len(''.join(article))
        elif "Times".lower() in paper.lower():
            results["The Times"] += 1
            resultsWordCount["The Times"] += len(''.join(article))
        elif "Mail".lower() in paper.lower():
            results["The Mail"] += 1
            resultsWordCount["The Mail"] += len(''.join(article))
        elif "Observer".lower() in paper.lower():
            results["The Observer"] += 1
            resultsWordCount["The Observer"] += len(''.join(article))
        elif "Express".lower() in paper.lower():
            results["The Express"] += 1
            resultsWordCount["The Express"] += len(''.join(article))
        elif "Sun".lower() in paper.lower():
            results["The Sun"] += 1
            resultsWordCount["The Sun"] += len(''.join(article))
        else:
            print("ERROR")
            print(article[0][-1] == ';', len(article[1]))
            print(paper, paper == article[2])
            print(article)

    f = open(csvFile, 'w', newline='', encoding='utf-8')

    writer = csv.writer(f)

    writer.writerow(["Articles by each paper"])
    writer.writerow(["Paper", "number of articles"])

    for paper in results:
        writer.writerow([paper, results[paper]])

    writer.writerow(["Words by each paper"])
    writer.writerow(["Paper", "number of word"])

    for paper in resultsWordCount:
        writer.writerow([paper, resultsWordCount[paper]])

    f.close()

def checkEmpty(line):
    return line != '' and line != '\xa0'

def oldMethod():
    files_to_read = []
    files_to_write = []
    x = 0
    words = 0
    for file in files_to_read:
        tempFile = open(file, "r")
        articles = tempFile.read().split("End of Document")
        titles = []
        for article in articles:
            if article == articles[0]:
                article = articles[0].split("\n\n\n\n")[1]
            articleLines = article.split("\n")
            skipArticle = False
            for line in articleLines:
                if line != "":
                    if line in titles:
                        skipArticle = True
                        break
                    else:
                        titles.append(line)
                        words += len(line.split(' '))
                        for writeFile in files_to_write[x]:
                            writeFile.write(line)
                        break
            if skipArticle:
                continue
            writeBody = False
            writeBodyContent = False
            for writeFile in files_to_write[x]:
                writeFile.write("\n")
                writeFile.write("\n")
            for line in articleLines:
                if line != "" and writeBody:
                    writeBodyContent = True
                    words += len(line.split(' '))
                    for writeFile in files_to_write[x]:
                        writeFile.write(line)
                if line == "" and writeBodyContent:
                    break
                if line == "Body":
                    writeBody = True
            writeGraphic = False
            writeGraphicDone = False
            for line in articleLines:
                if (line != "" and line != " ") and writeGraphic:
                    writeGraphicDone = True
                    words += len(line.split(' '))
                    for writeFile in files_to_write[x]:
                        writeFile.write("\n")
                        writeFile.write("\n")
                        writeFile.write(line)
                if line == "" and writeGraphicDone:
                    break
                if line == "Graphic":
                    writeGraphic = True
            for writeFile in files_to_write[x]:
                writeFile.write("\n")
                writeFile.write("\n")
                writeFile.write("\n")
        x += 1

"""
removeFilterArticles("All.txt", "FilterArticles.txt", precedingWords, followingWords, containingWords)
removeBlockTimeLines("FilterArticles.txt", "BlockRemovedFilterArticles.txt")
splitYears("BlockRemovedFilterArticles.txt", "2000DataOutput.txt", "2020DataOutput.txt")
cleanFile("2000DataOutput.txt", "2000DataOutputClean.txt")
cleanFile("2020DataOutput.txt", "2020DataOutputClean.txt")
"""

countArticlesByPaper("2020DataOutput.txt", "2020PaperData.csv")
countArticlesByPaper("2000DataOutput.txt", "2000PaperData.csv")