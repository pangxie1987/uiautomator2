auto.waitFor();//判断和等待开启无障碍
let see_count =100;// rawInput('请输入滑动次数','1000');//手动输入滑动次数默认是1000次。
appName = "快手极速版"
app.launchApp(appName);//只有一个快手极速版所以直接Launch就可以，不用包名
sleep(10000);//等待splash时间
console.show(); //开启日志（悬浮窗权限）


for (var i = 1; i < see_count; i++) {
    toastLog(appName + i +  "次"+"总计:"+ see_count + "次");//系统自带目前我huweinova不显示还不知道为啥
    slideScreenDown(device.width / 2, device.height - device.height * 0.2, device.width / 2, device.height * 0.1, 600);
}

/**
 * 屏幕向下滑动并延迟8至12秒
 */
function slideScreenDown(startX, startY, endX, endY, pressTime) {
    swipe(startX, startY, endX, endY, pressTime);
    let delayTime = random(8000, 12000);
    toast(delayTime);//提示等待时间
    sleep(delayTime);//模仿人类随机时间
}