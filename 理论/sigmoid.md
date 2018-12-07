# 1 sigmoid 函数的损失函数与参数更新

逻辑回归对应线性回归，但旨在解决分类问题，即将模型的输出转换为 $[0, 1]$ 的概率值。逻辑回归直接对分类的可能性进行建模，无需事先假设数据的分布。最理想的转换函数为单位阶跃函数（也称 Heaviside 函数），但单位阶跃函数是不连续的，没法在实际计算中使用。故而，在分类过程中更常使用对数几率函数（即 sigmoid 函数）：

$$
\sigma(x) = \frac{1}{1+e^{-x}}
$$

易推知，$\sigma(x)' = \sigma(x)(1- \sigma(x))$.

假设我们有 $m$ 个样本 $D = \{(x_i, y_i)\}_i^m$, 令 $X = (x_1, x_2, \cdots, x_m)^T, y = (y_1, y_2, \cdots, y_m)^T$, 其中 $x_i \in \mathbb{R}^n, y_i \in \{0, 1\}$, 关于参数 $w \in \mathbb{R}^n, b \in \mathbb{R}$, ($b$ 需要广播操作)，我们定义正例的概率为

$$
P(y_j=1|x_j;w,b) = \sigma(x_j^Tw +b) =  \sigma(z_j)
$$

这样属于类别 $y$ 的概率可改写为

$$
P(y_j|x_j;w,b) = \sigma(z_j)^{y_j}(1-\sigma(z_j))^{1-y_j}
$$

令 $z = (z_1, \cdots, z_m)^T$, 则记 $h(z) = (\sigma(z_1), \cdots, \sigma(z_m))^T$, 且 Logistic Regression 的损失函数为

$$
\begin{aligned}
L(w, b) =& - \displaystyle \frac{1}{m} \sum_{i=1}^m (y_i \log (\sigma(z_i)) +(1-y_i) \log (1 - \sigma(z_i)))\\
=& - \frac{1}{m} (y^T\log (h(z)) + (\mathbf{1}-y)^T\log(\mathbf{1}- h(z))), \text{ 此时做了广播操作}
\end{aligned}
$$

这样，我们有

$$
\begin{cases}
\nabla_w L(w,b) = \frac{\text{d}z}{\text{d}w} \frac{\text{d}L}{\text{d}z} = - \frac{1}{m}X^T(y-h(z))\\
\nabla_b L(w,b) =  \frac{\text{d}z}{\text{d}b} \frac{\text{d}L}{\text{d}z} = - \frac{1}{m}\mathbf{1}^T(y-h(z))
\end{cases}
$$

其中，$\mathbf{1}$ 表示全一列向量。这样便有参数更新公式 （$\eta$ 为学习率）：

$$
\begin{cases}
w \leftarrow w - \eta \nabla_{w} L(w,b)\\
b \leftarrow b - \eta \nabla_b L(w,b)
\end{cases}
$$

更多机器学习中的数见：[机器学习中的数学](https://www.jianshu.com/c/596533617cb8?utm_source=desktop&utm_medium=notes-included-collection)