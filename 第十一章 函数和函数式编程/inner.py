def foo():
    def bar():
        print 'bar() called'
    print 'foo() called'
    bar()
foo()
bar()

def main():
    foo()

if __name__ == '__main__':
    main()
