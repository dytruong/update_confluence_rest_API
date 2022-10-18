from bs4 import BeautifulSoup


class valueBody:
    def __init__(self, HTMLcontent, table_number):
        self.HTMLcontent = HTMLcontent

        # HTML content cannot convert html.parser 2 times -> so keep HTML content original to merge
        try:
            self.soup = BeautifulSoup(self.HTMLcontent, "html.parser")
        except TypeError:
            self.soup = HTMLcontent

        # Find all tables in HTML content
        tables = self.soup.find_all("table")
        self.table = tables[table_number]

        # List headings and td to create a nested list. It will look like A = [[a, b, c], [g, e, f]]
        self.headings = [
            th.get_text().strip() for th in self.table.find("tr").find_all("th")
        ]
        self.tableList = [self.headings]
        for row in self.table.find_all("tr")[1:]:
            tdList = [td.get_text() for td in row.find_all("td")]
            self.tableList.append(tdList)

    # Find string needs to replace
    def findString(self, X_VALUE, Y_VALUE):
        for xIndex, i in enumerate(self.tableList):
            if X_VALUE in i:
                xPosition = xIndex
            for yIndex, j in enumerate(i):
                if Y_VALUE in j:
                    yPosition = yIndex

        # X and Y_POSITION will be reused in the next function.
        self.X_POSITION = xPosition
        self.Y_POSITION = yPosition
        result = self.tableList[xPosition][yPosition]
        return result

    # Replace string based on (x, y)
    def replaceString(self, strInput):
        tdTable = self.table.find_all("td")
        # Find the position of X which will be replaced
        # X = (ELEMENT_IN_HEADINGS * X_INDEX) + (Y_INDEX+1) - ELEMENT_HEADINGS - 1

        ELEMENT_HEADINGS = len(self.headings)
        X = (
            ((ELEMENT_HEADINGS * self.X_POSITION) + (self.Y_POSITION + 1))
            - (ELEMENT_HEADINGS)
            - 1
        )

        # In some case, tag <br> cannot convert to string normally, so add except case for that.
        try:
            tdTable[X].string.replace_with(strInput)
        except AttributeError:
            tdTable[X].br.replace_with(strInput)

        # Return soup that is full HTML content
        return self.soup
