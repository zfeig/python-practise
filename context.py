class ContextDemo(object):
    def __enter__(self):
        print "start demo!"

    def __exit__(self,*others):
        print "exit ok!"

with ContextDemo():
    print "demo running..."
