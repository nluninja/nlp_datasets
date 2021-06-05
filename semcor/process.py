import xml.etree.ElementTree as ET



def main():
    print("Hello World!")
    tree = ET.parse('semcor.data.xml')
    root = tree.getroot()
    
    for sentence in root.iter('sentence'):
        my_sentence = ''
        for elem in sentence.iter():
            if (elem.tag == 'wf' or elem.tag == 'instance'):
                # print("token:"+ elem.text)
                if (elem.get('pos') == '.'): 
                    my_sentence = my_sentence.rstrip()
                my_sentence += str(elem.text)
                my_sentence = my_sentence + " "
        my_sentence = my_sentence.rstrip()
        print(my_sentence)

if __name__ == "__main__":
    main()