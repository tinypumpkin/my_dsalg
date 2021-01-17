import re,collections
class Formulas:
    def __init__(self):
        self.NWORDS=''

    '''
    贝叶斯公式:(求逆向概率)
    p(A|B)=p(B|A)*p(A)/p(B)
    在B发生时A发生的概率=A发生时B发生的概率*A单独发生的概率/B单独发生的概率
    '''
    def byeas(self,pri_a,pri_b,pos_a_to_b):
        b=pos_a_to_b*pri_a/pri_b
        return b

    def test1(self):
        pri=0.01331
        pos_b=0.0003
        bta=0.0035
        p=self.byeas(pri,pos_b,bta)
        print(p)

 # 把语料中的单词全部抽取出来, 转成小写, 并且去除单词中间的特殊符号
    def words(self,text): return re.findall('[a-z]+', text.lower()) 
 
    def train(self,features):
        model = collections.defaultdict(lambda: 1)
        for f in features:
            model[f] += 1
        return model
 # 统计每个单词出现的频率，字典形式
    def extra(self,file):
        w=self.train(self.words(open(file).read()))
        self.NWORDS=w
        return w
 # 词频先验
    def pri_word(self):
        pass
 #编辑距离 P(错误|正确)
    def edit_dis(self,word):  
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        n=len(word)
        return set([word[0:i]+word[i+1:] for i in range(n)] +                     # deletion
                    [word[0:i]+word[i+1]+word[i]+word[i+2:] for i in range(n-1)] + # transposition
                    [word[0:i]+c+word[i+1:] for i in range(n) for c in alphabet] + # alteration
                    [word[0:i]+c+word[i:] for i in range(n+1) for c in alphabet])  # insertion
    
    def edit_dis2(self,word):
        return set(e2 for e1 in self.edit_dis(word) for e2 in self.edit_dis(e1) if e2 in self.NWORDS)

    
    def known(self,words): 
        # 判断用户输入单词是否在词库里
        return set(w for w in words if w in self.NWORDS)

    def correct(self,word):
        # known([word]) = edit0_set ; known(edits1(word))  = edit1_set；known_edits2(word) = edit2_set
        candidates = self.known([word]) or self.known(self.edit_dis(word)) or self.edit_dis2(word) or [word]
        return max(candidates, key=lambda w: self.NWORDS[w])

if __name__ == "__main__":
    f=Formulas()
    file="F://M//dataset//all.al"
    f.extra(file)
    print(f.correct("foob"))