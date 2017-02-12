#"countinu" example : repeat printing "Too small" or "Input is..." according to input's lenth

while True:
        s=raw_input('Enter something: ')
        if s == 'quit' :
                break
        if len(s) <3:
                print 'Too small'
                continue
                #continue : not excute lower line, go to next loop
        print 'Input is of sufficient lenth'


