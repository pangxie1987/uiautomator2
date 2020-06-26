// 快逗短视频
auto.waitFor();
app.launchApp('快逗短视频');
sleep(8000);
console.show();
try {
    try {
       
        if (className("android.widget.ImageView").id("img_close").exists()) {
            className("android.widget.ImageView").id("img_close").findOnce().click();
        }
        let bottomMenus = className("android.widget.RelativeLayout").find();
        if (bottomMenus.length > 2) {
            bottomMenus[bottomMenus.length - 2].click();
            sleep(3000);
            let hongBaoList=className("android.widget.RelativeLayout").id("item_content").find();
            if(hongBaoList.length>1){
                toastLog("有红包")
                swipe(device.width / 2, device.height - device.height * 0.2, device.width / 2, device.height * 0.1, 300);
                toastLog("滑动屏幕")
                sleep(3000);
            }
        }
        sleep(3000);
        if (className("android.widget.TextView").text("立即签到").exists()) {
            toastLog("立即签到");
            className("android.widget.TextView").text("立即签到").findOnce().click();
            sleep(32000);
            className("android.widget.TextView").text("关闭广告").waitFor();
 
            className("android.widget.TextView").text("关闭广告").findOnce().click();
        }
        if (className("android.widget.TextView").text("已签到").exists()) {
            toastLog("已签到");//手动签到做个记录就好
        }
        sleep(3000);
        if (className("android.widget.TextView").text("首页").exists()) {
            toastLog("返回首页");
            let b=className("android.widget.TextView").text("首页").findOnce().bounds();
            click(b.centerX(),b.centerY());
        }
        toastLog("结束");
 
    } catch (e) { }
} catch (error) {
    console.error(error);
}
/**
 *点击一下屏幕
 */
function clickScreen() {
    var x =  device.width /4;
    var y = device.height /4;
    toastLog("点击屏幕" + x + ":" + y);
    let clickResult = click(x, y);
    toastLog(clickResult);
}
