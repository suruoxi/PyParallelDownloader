# PyParallelDownloader
Python script to download files with multiprocessing.  

## features
* Automatically retry for failure case.
* With a progress bar.

## Example
```python
from ParallelDownloader import *
# generate some data
data = [ ('http://img3.tbcdn.cn/tfscom/TB19J9dGVXXXXcWaXXXSutbFXXX.jpg', 'tt/'+ str(i)) for i in range(10000)]
# download with 10 processes
parallel_download(data, 10)
```

## Screen Shot

![](https://ws4.sinaimg.cn/large/006tNc79gy1fmoneq2x30j3130016q31.jpg)
