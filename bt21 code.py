#--------------------------------
#Writing Files
#Sydney Loerzel
#February 3, 2020
#--------------------------------


#----------------------Functions-------------------------

def write_to():
    files = open('bt21.txt', 'w')
    files.write("BT21 is BTS' character universe\n")
    files.write("Each character represents a member\n")
    files.write("Jungkook's is Cooky. A pink bunny\n")
    files.write("Taehyung's is Tata. He has a heart shaped head\n")
    files.write("Jimin's is Chimmy. A yellow dog\n")
    files.write("J-Hope's is Mang. An interesting horse\n")
    files.write("Yoongi's is Shooky. A cookie\n")
    files.write("Jin's is RJ. An alpaca\n")
    files.write("Lastly, RM's is Koya. A sleepy Koala\n")
    
    
def more():
    file = open('bt21.txt', 'a')
    file.write("\nThere is also one that represents ARMY")
    file.write("(ARMY is BTS' fanbase)")
    file.write("\nThat character is VAN. A robot that brings everyone together")
   
    
def your_own():
    file1 = open('bt21.txt', 'w')
    name = input("Name your character")
    types = input("What kind of animal or thing are they?")
    special = input("What special ability or talent do they have?")
    file1.write("Name,")
    file1.write(name +",")
    file1.write("Type,")
    file1.write(types +",")
    file1.write("Ability/Talent,")
    file1.write(special)
    file1.close()
    
def main():
    write_to()
    input("> ")
    more()
    input("> ")
    your_own()
    
main()
    
    