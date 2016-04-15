from book import Book
book1 = Book("physics","steve",1,323,True)
book2 = Book("c++","thomas",2,211,True)
book3 = Book("english","david",4,111,True)

book_detail1 = " ".join(book1.get_detail())
book_detail2 = " ".join(book2.get_detail())
book_detail3 = " ".join(book3.get_detail())

fh = open("book.txt","a+w")
fh.write("%s\n%s\n%s\n" %(book_detail1,book_detail2,book_detail3))
fh.close()

book_name = raw_input("enter book name: ")
fh = open("book.txt","a+")
flag = False
for line in fh.readlines():
    if book_name in line:
        flag = True
        print line

if not flag:
    book_author = raw_input("enter book author: ")
    book_self =raw_input("enter book self: ")
    book_serial = raw_input("enter book serial: ")
    fh.write("%s,%s,%s,%s\n" %(book_name,book_author,book_self,book_serial))
    perm = raw_input("do u want to place in self: ")
    if perm == "yes" or "y":
        print "you can borrow the book"
fh.close()

