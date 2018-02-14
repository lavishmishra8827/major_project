from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from rake_nltk import Rake

from flask import Flask, render_template, request
from werkzeug import secure_filename
import PyPDF2
import re
import nltk

class Node:
    def __init__(self,initdata1,initdata2):
        self.data1 = initdata1
        self.data2=initdata2
        self.next = None
        self.count=1

    def getData1(self):
        return (self.data1)
    def getData2(self):
        return (self.data2)
    def getCount(self):
        return (self.count)
    def incrementCount(self):
        self.count=self.count+1

    def getNext(self):
        return self.next
    
    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item1,item2):
        temp = Node(item1,item2)
        
        if self.head==None:
           self.head=temp
        else:
            
       # temp.setNext(self.head)
            current=self.head
                    
            while current.getNext()!=None:
                if item1 ==current.getData1() and item2 == current.getData2() :
                    current.incrementCount()
                    return
                current=current.getNext()
            current.setNext(temp)
        #self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def printList(self,mystopword):
        
        current=self.head
        
        while current !=None:
            if(current.getCount()==2):
                print(current.getData1()+" "+mystopword+" "+current.getData2())
                outt.append(current.getData1()+" "+mystopword+" "+current.getData2())
                #outt.append(mystopword)
                #outt.append(current.getData2())
                
                #print(current.getCount())
            current = current.getNext()

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
class Stopword:
    def __init__(self,item):
        self.stop_word_name=item
        self.listhead=None
        self.next=None
    def add(self,item1,item2):
        if self.listhead==None:
            mylist=UnorderedList()
            mylist.add(item1,item2)
            self.listhead=mylist
        else :
            self.listhead.add(item1,item2)
    def getData(self):
        return (self.stop_word_name)
    def getNext(self):
        return self.next
    
    def setNext(self,newnext):
        self.next = newnext
    def printList(self,mystopword):
        current=self.listhead
        
        current.printList(mystopword)
            
class listOfStopwords:
    def __init__(self):
        self.head=None
    def printList(self):
        current=self.head
        while current !=None:
            print(current.getData())
            current.printList(current.getData())
            current=current.getNext()

    def add(self,item,item1,item2):
        temp=Stopword(item)
        if(self.head==None):
            
            temp.add(item1,item2)
            self.head=temp
        else:
            current=self.head
            while current.getNext()!=None:
                if item == current.getData() :
                    current.add(item1,item2)
                    return
                current=current.getNext()
            current.setNext(temp)
            temp.add(item1,item2)


app = Flask(__name__)

#@app.route('/upload')
#def upload_file():
 #  return render_template('upload.html')0
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():


   if request.method == 'POST':
      f = request.files['file_input']
	  
      f.save(secure_filename(f.filename))
      pdfFileObj = open(f.filename,'rb')
      pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    #print(pdfReader.numPages)
      pageObj = pdfReader.getPage(0)
      tt=pageObj.extractText()
      pdfFileObj.close()
      outt=[]
      obj=listOfStopwords()

      text_file = open("abcde.txt", "r")
      stop_words =set(stopwords.words('english'))
      li= re.split(" |\n|\t|\.",text_file.read())
      text_file.close()
      count=0;
      k=0;
      for word in li:
          count=count +1
          if word in stop_words:
              if(li[count-2] in stop_words or li[count] in stop_words):
                  continue
              #print(li[count-2]+li[count-1]+li[count])
              obj.add(li[count-1],li[count-2],li[count])

      #obj.printList()

      r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.


      r.extract_keywords_from_text(tt)

      list2=r.get_ranked_phrases()
      list2.extend(outt)
      
      s="<html><body><ul>"
      for p in list2:
          s=s+'<li>'+p+'</li>'

      s=s+"</ul></body></html>"
      return (s)
            
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
      return (f)


@app.route('/uploader2', methods = ['GET', 'POST'])

def upload_file2():
   if request.method == 'POST':
      user = request.form['text_input']
      return (user)


	  
if __name__ == '__main__':
   app.run(debug = True)
