from locust import HttpLocust,TaskSet,task
 
# 集合系统 http://172.16.100.22:6002
# locust -f locust_collection.py --host=http://172.16.100.22:6002
class test_collection(TaskSet):
    # task装饰该方法为一个事务方法的参数用于指定该行为的执行权重。参数越大，每次被虚拟用户执行概率越高，不设置默认是1，
    @task()
    def test_baidu(self):
        # 定义requests的请求头
        header = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Cookie': 'SESSION=8a7a7520-a474-4e1b-bb36-d6f70759ddd0',
                'Host': '172.16.100.22:6002',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
        # r是包含所有响应内容的一个对象
        r = self.client.get("/",timeout=30,headers=header)
        # 这里可以使用assert断言请求是否正确，也可以使用if判断
        assert r.status_code == 200
 
# 这个类类似设置性能测试，继承HttpLocust
class websitUser(HttpLocust):
    # 指向一个上面定义的用户行为类
    task_set = test_collection
    #执行事物之间用户等待时间的下界，单位毫秒，相当于lr中的think time
    min_wait = 3000
    max_wait = 6000