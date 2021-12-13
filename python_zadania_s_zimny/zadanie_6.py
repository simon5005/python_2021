
import xml.dom.minidom as md
import xml.sax 
import csv
from csv import writer
from xml.sax.handler import ContentHandler
from xml.sax.saxutils import XMLFilterBase, XMLGenerator


def dom_parse():
  
    file = md.parse("library.xml")
    
    weight = file.createElement("weight")
    weight.setAttribute("val", "80 kg") 
    file.firstChild.appendChild(weight)
    clubs = ["Manchester United", "Juventus", "Real Madryt"]
    for l in clubs: 
        club = file.createElement("club")
        club.setAttribute("clb", l )
        file.firstChild.appendChild(club)
  
    delete = file.getElementsByTagName("nationality")
    for i in delete: 
  
        x = i.parentNode
        x.removeChild( i )

    file.getElementsByTagName( "age" )[ 0 ].childNodes[ 0 ].nodeValue = "34" 
  
    with open( "test.xml", "w" ) as fs: 
  
        fs.write( file.toxml() )
        fs.close() 
    print(file.toxml())


class NoteHandler(ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.firstname = ""
        self.lastname = ""
        self.work = ""
        self.age = ""
        self.gender = ""
        self.hobby = ""
        self.nationality = ""

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "note":
            print ("*****Note*****")

    def endElement(self, tag):
        if self.CurrentData == "fname":
            print("firstname:", self.firstname)
        elif self.CurrentData == "lname":
            print("lastname:", self.lastname)
        elif self.CurrentData == "work":
            print("work:", self.work)
        elif self.CurrentData == "age":
            print("age:", self.age)
        elif self.CurrentData == "gender":
            print("gender:", self.gender)
        elif self.CurrentData == "hobby":
            print("hobby:", self.hobby)
        elif self.CurrentData == "nationality":
            print("nationality:", self.nationality)
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "fname":
            self.firstname = content
        elif self.CurrentData == "lname":
            self.lastname = content
        elif self.CurrentData == "work":
            self.work = content
        elif self.CurrentData == "age":
            self.age = content
        elif self.CurrentData == "gender":
            self.gender = content
        elif self.CurrentData == "hobby":
            self.hobby = content
        elif self.CurrentData == "nationality":
            self.nationality = content

class ProjectFilter(XMLFilterBase):
    def __init__(self, newValues, parent=None):
        super().__init__(parent)
        self.newValues = newValues
        self.CurrentData = ""
        self.count = 0

    def startElement(self, tag, attrs):
        self.CurrentData = tag
        super().startElement(tag, attrs)

    def endElement(self, tag):
        super().endElement(tag)

    def characters(self, content):
        if self.CurrentData in self.newValues:
            content = self.newValues[self.CurrentData]
        super().characters(content)
        self.CurrentData = ""


def sax_parse():
    print("Read data")
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    notehandler = NoteHandler()
    parser.setContentHandler(notehandler)
    test = parser.parse("library.xml")

    newValues = {"fname":"Lionel","lname":"Messi","age":"34","nationality":"argentina"}
    reader = ProjectFilter(newValues, xml.sax.make_parser())

    print("\nEdit and save data")
    with open("output.xml", "w") as file:
        handler = XMLGenerator(file)
        reader.setContentHandler(handler)
        reader.parse('library.xml')




def read_data():
    filename = "baza_danych.csv"
    rows = []
    fields = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
    print("Total no. of rows: %d"%(csvreader.line_num))
    print('Field names are:' + ', '.join(field for field in fields))
    print('\Rows are:\n')
    for row in rows:
        for col in row:
            print("%10s"%col),
        print('\n')

def write_data():
    filename = "baza_danych.csv"
    texts = list()
    text = input("Podaj markę: ")
    texts.append(text)
    text = input("Podaj model: ")
    texts.append(text)
    text = input("Podaj rok: ")
    texts.append(text)
    text = input("Podaj kolor: ")
    texts.append(text)
    print(texts)
 
# writing to csv file"""""
    with open(filename, 'a') as csvfile:
    
      writer_object = writer(csvfile)
      writer_object.writerow(texts)
    csvfile.close() 

def delete_function():
    filename = "baza_danych.csv"
    member_name = input("Please enter a member's name to be deleted: ")

    with open(filename, 'r+') as in_file:
        reader = csv.reader(in_file)
        rows = [row for row in csv.reader(in_file) if member_name not in row]
        in_file.seek(0)
        in_file.truncate()
        writer = csv.writer(in_file)
        writer.writerows(rows)


def csv_base():

    print("1.Display \n2.Add new data \n3.Delete data")
    option = int(input())

    if option == 1:
            read_data()  # Print all content
    elif option == 2:
            write_data()
            read_data()

    elif option == 3:
            read_data()
            delete_function()
            read_data()
if __name__ == "__main__":
    #xml_func()
    #sax_func()
    #csv_base()
    sax_parse()
    #dom_parse()
