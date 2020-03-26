'''
对百度的自然语言api进行测试和使用
参考 https://blog.csdn.net/cyinfi/article/details/88046887

百度API：https://console.bce.baidu.com/ai/?_=1585230913997&fromai=1#/ai/nlp/overview/index
'''

from aip import AipNlp


class baidu_nlp_ts(object):
	'''
	对百度的自然语言api进行测试和使用
	'''
	def __init__(self):
		APP_ID = 'xxx'
		API_KEY = 'xxx'
		SECRET_KEY = 'xxx'
		self.client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

	def tst_pingtai(self):
	    
	    """ 调用词法分析 """
	    text = "百度是一家高科技公司"
	    res = self.client.lexer(text);
	    print(res)

	    '''调用词向量表示'''
	    word = "张飞"
	    res = self.client.wordEmbedding(word)
	    print(res)

	    '''调用词义相似度'''
	    word1 = '海洋'
	    word2 = '天空'
	    word3 = '海'

	    res = self.client.wordSimEmbedding(word1, word2)
	    res1 = self.client.wordSimEmbedding(word1, word3)
	    print(res, res1)

	    '''调用短文本相似度'''
	    text1 = '浙富股份'
	    text2 = '万事达集团'
	    res = self.client.simnet(text1, text2)
	    print(res)

	    '''调用评论观点抽取'''
	    text = '三星电脑电池不给力'
	    options = {}
	    options["type"] = 13	# 可带参数
	    res = self.client.commentTag(text, options)
	    print(res)

	    '''调用情感倾向分析'''
	    text = '苹果是一家伟大的公司'
	    result = self.client.sentimentClassify(text)
	    print(result)
	    # 该情感搭配的积极性（0表示消极，1表示中性，2表示积极）
	    sentiment = result.get('items')[0].get('sentiment')
	    print(sentiment)


if __name__ == '__main__':
	b = baidu_nlp_ts()
	b.tst_pingtai()