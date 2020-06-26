auto.waitFor()
var appName = "拼多多";
launchApp(appName);
sleep(10000)
console.show(); //开启日志（悬浮窗权限）


// 关闭刚进入页面的弹窗
function kuaishouclosetips(){
    try{
        if(className('android.widget.TextView').id("az3").exists()){
            className('android.widget.TextView').id("az3").findOnce().click();
            toast('关闭弹框成功')
        }
    }
    catch(e) { }
    
}