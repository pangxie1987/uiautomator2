auto.waitFor();
app.launchApp('快逗短视频');
//console.show(); //开启日志（悬浮窗权限）
console.info("快逗短视频提现");
sleep(10000);

try {
    if(className("android.widget.TextView").text("我").exists()){
        let b=className("android.widget.TextView").text("我").findOne().parent().bounds();
        click(b.centerX(),b.centerY());
    }
    cashOut();
} catch (error) {
    console.error(error);
}
//home();//关闭当前程序

function cashOut() {
    
    if(className("android.widget.TextView").text("现金账户(元)").exists()){
        let b = className("android.widget.TextView").text("现金账户(元)").findOne().bounds();
        let clickResult = click(b.centerX(), b.centerY());

        className("android.widget.TextView").text("去提现").waitFor();
        if (className("android.widget.TextView").text("去提现").exists()) {
            className("android.widget.TextView").text("去提现").findOne().click();
            text("立即提现").waitFor();
            if (className("android.widget.TextView").text("立即提现").exists()) {
                let b = className("android.widget.TextView").text("立即提现").findOne().bounds();
                let clickResult = click(b.centerX(), b.centerY());
                if (clickResult) {
                    console.show(); //开启日志（悬浮窗权限）
                    toastLog("点击提现按钮成功");
                }
            }
        }
    }

}