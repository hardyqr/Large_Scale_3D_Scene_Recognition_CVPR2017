# Markdown Preview Test
#LSTM/RNN Model
[*Understanding LSTM Networks*,by *colah*](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)

To start the Preview, press "shift+control+M "


##Recurrent Neural Networks
（recurrent, adj.周期性的）

- RNN-rolled

![](https://github.com/hardyqr/Large_Scale_3D_Scene_Recognition_CVPR2017/blob/master/RNN-rolled.png?raw=true)

- RNN-unrolled

![](https://github.com/hardyqr/Large_Scale_3D_Scene_Recognition_CVPR2017/blob/master/RNN-unrolled.png?raw=true)


[RNN's Applications:*The Unreasonable Effectiveness of Recurrent Neural Networks*,by *Andrej Karpathy*](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)


##The Problem of Long-Term Dependencies

- RNN Short-Term Dependencies

![](https://github.com/hardyqr/Large_Scale_3D_Scene_Recognition_CVPR2017/blob/master/RNN-shorttermdepdencies.png?raw=true)

- RNN Long-Term Dependencies

![](https://github.com/hardyqr/Large_Scale_3D_Scene_Recognition_CVPR2017/blob/master/RNN-longtermdependencies.png?raw=true)

Sometimes, near words(the last few) are enough to predict the next one. This is short-term dependency. Other times,we need more information which maybe several words we used few sentences before. This is called long-term dependency.

#LSTM Networks

Long Short Term Memory networks don't have this kind of problems. This is the kind of RNN that can learn long-term dependencies.

They were introduced by Hochreiter & Schmidhuber in 1997.[LONG SHORT-TERM MEMORY](http://deeplearning.cs.cmu.edu/pdfs/Hochreiter97_lstm.pdf)


- Simple RNN

![](https://github.com/hardyqr/Large_Scale_3D_Scene_Recognition_CVPR2017/blob/master/LSTM3-SimpleRNN.png?raw=true)


- RNN with internal chain structure (LSTMs unit)

![](https://github.com/hardyqr/Large_Scale_3D_Scene_Recognition_CVPR2017/blob/master/LSTM3-chain.png?raw=true)




Now we try to build model for language (some sentences).

We have a list of words that appear in those sentences.

$$w_1,w_2,...,w_T$$

We define the probability of each word that appears like：



$$P(w_1,w_2,...,w_T) = \prod_{t=1}^T P(w_t | w_{1:(t-1)})$$


其中 $1 : (t - 1)$ 表示从 $1$ 到 $t-1$。因此我们希望模型能够给高的概率给更加合理的字符序列，而非乱序的组合。



##Input Gate
输入门：控制当前输入 $x_t$ 和前一步输出 $h_{t-1}$ 进入新的 cell 的信息量：

##Forget Gate
##Output Gate
##