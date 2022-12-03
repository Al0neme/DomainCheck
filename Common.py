from optparse import OptionParser
from concurrent.futures import ThreadPoolExecutor, wait
import DomainCheck


class Common:
    def getargs(self):
        usage = "python main.py -f domains.txt -t 30 -o r.txt"
        parser = OptionParser(usage=usage)
        parser.add_option("-f", "--domains-file", dest="dfile", help="path of domains.txt")
        parser.add_option("-t", "--thread", dest="thread", type=int, default=20,
                          help="threads(default 20)")
        parser.add_option("-o", "--output", dest="ofile", help="path of result file")
        return parser.parse_args()  # (options, args)

    def runcheck(self, domain, save=0, results=[]):
        check_result = DomainCheck.check_domain(domain)
        if check_result:
            if save:
                print(check_result)
                results.append(check_result)
            print(check_result)

    def runthreads(self, num, domains, save=0, results=[]):
        thread_list = []
        with ThreadPoolExecutor(max_workers=num) as executor:
            for i in domains:
                domain = str(i).strip('\n').strip('\r')
                thread_list.append(executor.submit(self.runcheck, domain, save, results))
        wait(thread_list)

    def run(self):
        (options, args) = self.getargs()
        if options.dfile:
            with open(options.dfile, "r") as fr:
                domains = fr.readlines()

            if options.thread:
                num = options.thread
                if options.ofile:
                    save = 1
                    results = []
                    self.runthreads(num, domains, save, results)
                    with open(options.ofile, "a+", encoding="utf-8") as fw:
                        for r in results:
                            fw.write(r + "\n")
                self.runthreads(num, domains)

# Common().run()
