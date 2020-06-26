auto.waitFor()
var appName = "微视";
launchApp(appName);
sleep(5000)
//waitForActivity("com.tencent.weishi.ui.main.MainActivity");
//sleep(5000)
while(true){
    huaping();
}
 
function huaping(){
    //设备宽度根据手机尺寸可调节
    var w1 = 2;
    var w2 = 2;
    //设备高度根据手机尺寸可调节
    var h1=1500;
    var h2=300;
    //上下滑动时长根据需要更改数值
    var time=2000;
    //随机等待时间random（最小值，最大值）根据需要更改数值（单位秒）
    var time_random=random(20,30)*1000;
    swipe(device.width/w1,h1,device.width/w2,h2,time);
    //提示等待时间。
    toast(time_random);
    sleep(time_random);
}
