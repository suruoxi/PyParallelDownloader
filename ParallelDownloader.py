import sys
import multiprocessing 
import os
import wget
import ssl
import tqdm

def retryer():
    def wraps(func):
        request_exceptions = (
            IOError,
            IndexError,
            ssl.CertificateError,
            ValueError
        )
        def inner(*args, **kwargs):
            for i in range(4):
                if i > 0:
                    print "%d try" % (i + 1)
                try:
                    result = func(*args, **kwargs)
                except request_exceptions:
                    #time.sleep(timeout)
                    continue
                else:
                    return result
            else:
                return None
        return inner
    return wraps


def empty(rec):
    print 'empty'

@retryer()
def getimg(rec):
    #print rec
    try:
        url,dst = rec
    except IndexError:
        return None
    dir, _ = os.path.split(dst)
    if not os.path.exists(dir):
        os.makedirs(dir)
    #print url
    if not os.path.exists(dst):
        try:
            wget.download(url, dst, None) # quiet mode
        except Exception, e:
            sys.stderr.write(e)
        return rec

# to avoid multiprocessing's pickle error
# functions must be top-level
def worker_func(*args, **kwargs):
    return getimg(*args, **kwargs)



def parallel_download(data,threads=10):
    pool = multiprocessing.Pool(processes = threads,)
    #pool_outputs = pool.map(getimg, img_urls)

    # show progress bar
    for _ in tqdm.tqdm(pool.imap_unordered(worker_func,data), total=len(data)):
        pass
    #pool.imap_unordered(worker_func,data):
    #pool_outputs = pool.map(worker_func, data)
    #pool.close()
    #pool.join()


if __name__ == "__main__":
    outdir = 'test_parallel_download/'
    num_worker = 3
    data = [ ('http://img3.tbcdn.cn/tfscom/TB19J9dGVXXXXcWaXXXSutbFXXX.jpg', outdir+ str(i)) for i in range(10000)]

    import os
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    parallel_download(data, num_worker)

