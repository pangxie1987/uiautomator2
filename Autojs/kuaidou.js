
auto.waitFor();//判断和等待开启无障碍
let see_count =1000;// rawInput('请输入滑动次数','1000');//手动输入滑动次数默认是1000次。
app.launchApp('快逗短视频');//只有一个快手极速版所以直接Launch就可以，不用包名
sleep(10000);//等待splash时间
console.show(); //开启日志（悬浮窗权限）

// qiandao()   //签到
for (var i = 1; i < see_count; i++) {
    toastLog("快逗短视频滑动" + i +  "次"+"总计:"+ see_count + "次");//系统自带目前我huweinova不显示还不知道为啥
    kuaiDouCloseRedFloatTip();
    randomUpSildeScreen();//模仿人类随向上滑动一次，表示对这个视频有兴趣
    randomDownSildeScreen();//模仿人类随连续下滑2次，表示对当前视频无兴趣
    randomHeart("layout_like");//模仿人类随随机点赞
    kuaiDouWaitAdForCoin();
    slideScreenDown(device.width / 2, device.height - device.height * 0.2, device.width / 2, device.height * 0.1, 600);
}
//关闭当前程序
home();//回到首页
exits();//退出js脚本
function kuaiDouWaitAdForCoin() {
    if (id("tv_timer").exists()) {
        sleep(20000);
    }
}

// 签到
function qiandao(){
    try{
        // 进入来赚钱页面
        click(539, 1863);
        sleep(1000);

        // 立即签到
        click(505, 938);
        sleep(1000);

        // 回到首页
        home()
        sleep(1000);

        //关闭广告
        className("android.widget.ImageView").findOnce().click();

    }catch(e) {};

}

/**
 * 快逗视频关闭广告
 */
function kuaiDouCloseRedFloatTip(){
    try {
        if (className("android.widget.ImageView").id("img_close").exists()) {
            className("android.widget.ImageView").id("img_close").findOnce().click();
        }
        if (className("android.widget.ImageView").id("tt_video_ad_close_layout").exists()) {
            className("android.widget.ImageView").id("tt_video_ad_close_layout").findOnce().click();
        }
        if (className("android.widget.RelativeLayout").id("tt_video_ad_close_layout").exists()) {
            className("android.widget.RelativeLayout").id("tt_video_ad_close_layout").findOnce().click();
        }
        if (className("android.widget.TextView").text("关闭广告").exists()) {
            className("android.widget.TextView").text("关闭广告").findOnce().click();
        }
    } catch (e) { }
}
/**
 * 屏幕向下滑动并延迟8至12秒
 */
function slideScreenDown(startX, startY, endX, endY, pressTime) {
    swipe(startX, startY, endX, endY, pressTime);
    let delayTime = random(20000, 40000);
    sleep(delayTime);//模仿人类随机时间
}
/**
 * 随机上滑（防止被判定是机器）上滑后停留时间至少是10S，造成假象表示是对内容感兴趣
 * 点赞和关注先不搞。
 */
function randomUpSildeScreen(){
    let randomIndex = random(1, 50);
    if(randomIndex==1){
        console.log("快手极速版随机上滑被执行了!!!");
        pressTime = random(200, 500);
        swipe(device.width / 2, 500, device.width / 2, device.height-200, 300);
        delayTime = random(10000, 15000);
        sleep(delayTime);
    }
}
/**
 * 连续下滑对上一个无兴趣
 * 其实得和上滑做个排他，既然无兴趣不要在上滑
 */
function randomDownSildeScreen(){
    let randomIndex = random(1, 50);
    if(randomIndex==1){
        console.log("连续下滑被执行了");
        swipe(device.width / 2, device.height-200, device.width / 2, 500, 300);
        sleep(2000);
        swipe(device.width / 2, device.height-200, device.width / 2, 500, 300);
        delayTime = random(8000, 10000);
        sleep(delayTime);
        
    }
}
 
/**随机点赞并休息一秒 */
function randomHeart(view_id) {
    index = random(1, 50);
    if (index == 6) {
        var target = id(""+view_id+"").findOnce();
        if (target == null) {
            return;
        } else {
            target.click();
            sleep(1000);
            console.log("随机点赞并休息一秒");
        }
    }
}
/**
 * 随机关注
 */
function randomFollow(){
    index = random(1, 100);
    if (index == 66) {
        var target = id('nebula_thanos_bottom_follow_button_layout').findOnce();
        if (target == null) {
            return;
        } else {
            target.click();
            sleep(1000);
        }
    }
}
/**
 * 随机评论（未实现）
 */
function randomComment() {
    content = "666"
    id('comment_button').findOnce().click();
    sleep(1000);//阻塞下面的动作
    id("recycler_view").className("androidx.recyclerview.widget.RecyclerView").scrollable(true).findOne().children().forEach(child => {
        var target = child.findOne(id("comment"));
        target.click();
    });
    sleep(1000);
}
