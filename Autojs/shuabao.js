auto.waitFor();
var appName = "刷宝短视频";
launchApp(appName);
let see_count = 100;    //设置滑动次数
// sleep(5000);
// waitForActivity("com.jm.video.ui.main.MainActivity");
sleep(3000);
console.show(); //开启日志（悬浮窗权限）


qiandao();
for (i=0; i<see_count; i++){
    toastLog(appName + i +  "次"+"总计:"+ see_count + "次");//系统自带目前我huweinova不显示还不知道为啥
    huaping()
}

function qiandao(){
    
    try{
        // 点击任务
        toastLog('查找任务页面');
        sleep(1000)
        if (id("tv_tab_title").className("android.widget.TextView").text("任务").exists()){
            id("tv_tab_title").className("android.widget.TextView").text("任务").findOnce().parent().parent().click();    
            sleep(1000)
        }
        
        // 关闭邀请红包
        if (className("android.widget.ImageView").id("imgClose").exists()){
            className("android.widget.ImageView").id("imgClose").findOnce().click();
            toastLog('关闭邀请红包');
            sleep(1000)
        }

        // 立即签到
        click(870, 565);
        sleep(1000)

        // 查看签到的视频
        click(700, 1351);
        sleep(300000);
        
        // 关闭广告
        id("tt_video_ad_close_layout").findOnce().click()
        sleep(1000)

        // 返回首页
        if (id("tv_tab_title").className("android.widget.TextView").text("首页").exists()){
            id("tv_tab_title").className("android.widget.TextView").text("首页").findOnce().parent().parent().click();    
            sleep(1000)
        }
    } catch (e) { };    
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
    var time_random=random(8,13)*1000;
    swipe(device.width/w1,h1,device.width/w2,h2,time);
    //提示等待时间。
    toast(time_random);
    sleep(time_random);
}
