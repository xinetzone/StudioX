import numpy as np

class Loader(dict):
    """
    方法
    ========
    L 为该类的实例
    len(L)::返回样本数目
    iter(L)::即为数据迭代器

    Return
    ========
    可迭代对象（numpy 对象）
    """

    def __init__(self, batch_size, X, Y=None, shuffle=True, name=None):
        '''
        X, Y 均为类 numpy, 可以是 HDF5
        '''
        if name is not None:
            self.name = name
        self.X = np.asanyarray(X[:])
        if Y is None:
            # print('不存在标签！')
            self.Y = None
        else:
            self.Y = np.asanyarray(Y[:])
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.nrows = self.X.shape[0]

    def __iter__(self):
        idx = np.arange(self.nrows)

        if self.shuffle:
            np.random.shuffle(idx)

        for k in range(0, self.nrows, self.batch_size):
            K = idx[k:min(k + self.batch_size, self.nrows)]
            if self.Y is None:
                yield np.take(self.X, K, 0)
            else:
                yield np.take(self.X, K, 0), np.take(self.Y, K, 0)
                
    def __len__(self):
        return self.nrows