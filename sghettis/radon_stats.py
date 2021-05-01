
import radon
from radon.visitors import ComplexityVisitor, HalsteadVisitor
from radon.complexity import cc_rank, cc_visit
from radon.raw import analyze
from radon.metrics import halstead_visitor_report, h_visit


class RadonStats(object):
    def __init__(self, filename=''):
        self.filename = filename
        #self.cyclo_complex = 

    def ccomplex(self):
        with open(self.filename) as f:
            results = ComplexityVisitor.from_code(f.read())
            #print('Visit: ', cc_rank(cc_visit(f.read())))
        #print(cc_rank(results))
        print(cc_rank(results.functions[0].complexity))
        return results.functions
    
    def hcomplex(self):
        with open(self.filename) as f:
            results = HalsteadVisitor.from_code(f.read())
        hreport = halstead_visitor_report(results)
        return hreport

    def analyze(self):
        with open(self.filename) as f:
            results = analyze(f.read())
        return results
